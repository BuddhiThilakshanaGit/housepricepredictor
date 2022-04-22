from fastapi import FastAPI 
from model import predict_price,getLocations_dict
from fastapi.middleware.cors import CORSMiddleware
from pydantic import   BaseModel

class Item(BaseModel):
    baths: int
    beds: int
    house_size: int
    land_size: int
    city: str
    district: str 

app = FastAPI()

origins = [
    "http://127.0.0.1:10808",
    "https://houseprice.pages.dev",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/getLocations")
async def getLocations():
    return getLocations_dict()

@app.post("/predict")
async def predict(item: Item):
        return predict_price(item.baths,item.land_size,item.beds,item.house_size,item.city,item.district)

