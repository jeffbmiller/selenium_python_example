from typing import Optional
from pydantic import BaseModel

class Crop(BaseModel):
    name: str
    base_grade: Optional[str]
    base_dollar_t: float
    low_price_dollar_t: float
    base_dollar_bu : float
    low_price_dollar_bu : float