from tools.search_flights_amadeus import search_flights_amadeus
from tools.brightdata_tools import BrightDataTools
from tools.apify_tools import ApifyTools
from tools.duckduckgo_tools import DuckDuckGoTools

TOOLS = {
    "search_flights_amadeus": search_flights_amadeus,
    "brightdata_tools": BrightDataTools,
    "apify_tools": ApifyTools,
    "duckduckgo_tools": DuckDuckGoTools,
}
