from tools.search_flights_amadeus import search_flights_amadeus
from agno.tools.brightdata import BrightDataTools
from agno.tools.apify import ApifyTools
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.openweather import OpenWeatherTools
from agno.tools.google_maps import GoogleMapTools

TOOLS = {
    "search_flights_amadeus": search_flights_amadeus,
    "brightdata_tools": BrightDataTools,
    "apify_tools": ApifyTools,
    "duckduckgo_tools": DuckDuckGoTools,
    "openweather_tools": OpenWeatherTools,
    "google_maps_tools": GoogleMapTools,
}
