from __future__ import annotations

import json
from typing import Any, Dict, Optional, Tuple

from utils.logging import LOGGER


class HttpClient:
    def __init__(self, timeout_s: float = 20.0):
        self.timeout_s = timeout_s

    def get_json(self, url: str, headers: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
        status, body = self._request("GET", url, headers=headers)
        if status >= 400:
            raise RuntimeError(f"HTTP {status}: {body[:300]}")
        return json.loads(body)

    def post_json(
        self,
        url: str,
        payload: Dict[str, Any],
        headers: Optional[Dict[str, str]] = None,
    ) -> Dict[str, Any]:
        h = {"Content-Type": "application/json", **(headers or {})}
        status, body = self._request("POST", url, headers=h, data=json.dumps(payload).encode("utf-8"))
        if status >= 400:
            raise RuntimeError(f"HTTP {status}: {body[:300]}")
        return json.loads(body)

    def _request(
        self,
        method: str,
        url: str,
        headers: Optional[Dict[str, str]] = None,
        data: bytes | None = None,
    ) -> Tuple[int, str]:
        try:
            import httpx  # type: ignore
            with httpx.Client(timeout=self.timeout_s) as client:
                r = client.request(method, url, headers=headers, content=data)
                return r.status_code, r.text
        except ImportError:
            from urllib.request import Request, urlopen
            req = Request(url=url, method=method, headers=headers or {}, data=data)
            with urlopen(req, timeout=self.timeout_s) as resp:
                raw = resp.read().decode("utf-8", errors="replace")
                return resp.status, raw
        except Exception:
            LOGGER.exception("HTTP request failed: %s %s", method, url)
            raise
