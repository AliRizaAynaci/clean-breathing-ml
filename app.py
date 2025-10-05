from fastapi import FastAPI,Response,Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import pickle
import pandas as pd
from pydantic import BaseModel


app = FastAPI()

templates = Jinja2Templates(directory="templates")

with open("modelnasa01.pkl","rb") as f:
    saved_data = pickle.load(f)
    model = saved_data["model"]
    scaler = saved_data["scaler"]
class AirqualityFeatures(BaseModel):
    Temperature: float
    Humidity: float
    PM2_5: float
    PM10: float
    NO2: float
    SO2: float
    CO: float
    Population_Density: int

@app.get('/',response_class=HTMLResponse)
async def home(request:Request):
    return templates.TemplateResponse("index.html",{"request":request})


@app.post("/predict")
async def predict(features: AirqualityFeatures):
    model_input = features.model_dump()
    input_data = pd.DataFrame([model_input])
    print(input_data)

    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)

    return {"prediction": prediction[0]}
