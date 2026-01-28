from agnoprj.tools.search_flights_amadeus import search_flights_amadeus
from agno.tools.brightdata import BrightDataTools
from agno.tools.apify import ApifyTools
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.openweather import OpenWeatherTools
from agno.tools.google_maps import GoogleMapTools

TOOLS = {
    "search_flights_amadeus": search_flights_amadeus,
    # Preconfigured tool instances (safe to pass directly into agents)
    "brightdata": BrightDataTools(web_data_feed=True),
    "apify_google_places": ApifyTools(actors=["compass/crawler-google-places"]),
    "duckduckgo": DuckDuckGoTools(),
    "openweather": OpenWeatherTools(),
    "google_maps": GoogleMapTools(),
}
