
import os
import requests
from typing import Optional, Dict

def search_flights_amadeus(
    origin: str, 
    destination: str, 
    departure_date: str, 
    return_date: Optional[str] = None, 
    adults: int = 1, 
    currency: str = "EUR"
) -> Dict:
    """Search flights using Amadeus API.
    
    Args:
        origin: Airport code (e.g., "PAR", "JFK")
        destination: Airport code
        departure_date: Date (YYYY-MM-DD)
        return_date: Optional return date
        adults: Number of passengers
        currency: Currency code
    """
    client_id = os.getenv("AMADEUS_CLIENT_ID")
    client_secret = os.getenv("AMADEUS_CLIENT_SECRET")
    
    if not client_id or not client_secret:
        return {"error": "Missing Amadeus credentials"}
    
    # Get token
    token = requests.post(
        "https://test.api.amadeus.com/v1/security/oauth2/token",
        data={"grant_type": "client_credentials", "client_id": client_id, "client_secret": client_secret}
    ).json().get("access_token")
    
    if not token:
        return {"error": "Auth failed"}
    
    # Search flights
    params = {
        "originLocationCode": origin.upper()[:3],
        "destinationLocationCode": destination.upper()[:3],
        "departureDate": departure_date,
        "adults": adults,
        "currencyCode": currency,
        "max": 10
    }
    if return_date:
        params["returnDate"] = return_date
    
    response = requests.get(
        "https://test.api.amadeus.com/v2/shopping/flight-offers",
        params=params,
        headers={"Authorization": f"Bearer {token}"}
    )
    
    if response.status_code != 200:
        return {"error": f"API error: {response.status_code}"}
    
    data = response.json().get("data", [])
    
    return {
        "route": f"{origin} → {destination}",
        "date": departure_date,
        "flights": [{
            "airline": f["itineraries"][0]["segments"][0]["carrierCode"],
            "price": f["price"]["total"],
            "duration": f["itineraries"][0]["duration"],
            "stops": len(f["itineraries"][0]["segments"]) - 1
        } for f in data[:10]]
    }