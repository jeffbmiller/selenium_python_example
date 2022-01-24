from fastapi import FastAPI

from crop_service import CropService

app = FastAPI()


@app.get("/")
async def root():
    service = CropService()
    prices = service.fetch_crop_prices()
    return prices