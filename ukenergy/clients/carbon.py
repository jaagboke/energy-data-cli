import httpx
from pydantic import BaseModel

BASE_URL = "https://api.carbonintensity.org.uk"

class CarbonIntensity (BaseModel):
    forecast: int
    actual: int | None
    index: str

class CarbonPeriod(BaseModel):
    _from: str
    _to: str
    intensity: CarbonIntensity

    model_config =  {"populate_by_name": True, "extra": "ignore"}

def get_current_intensity() -> CarbonPeriod:
    response = httpx.get(f"{BASE_URL}/intensity")
    response.raise_for_status()

    data = response.json()
    period = data["data"][0]
    period["_from"] = period.pop("from")
    return CarbonPeriod(**period)