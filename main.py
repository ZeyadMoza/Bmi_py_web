#Get Library
from fastapi import FastAPI ,Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


class BMI_out(BaseModel):
    bmi: float
    message: str
#-------------
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_methods=["*"],
    allow_headers=["*"],
)
#-------------
@app.get("/")
#------------

#------------
@app.get("/calculate_bmi")
def calculate_bmi(
    weight: float= Query(... , gt=20,lt=200, description="Weight in kilograms") ,
    height: float= Query(..., gt=1,lt=3, description="Height In metres") 
    ):
    
    bmi = weight / (height ** 2)

    if bmi < 18.5:
        message = "You are underweight, eat more."
    elif 18.5 <= bmi < 25:
        message = "You have a good weight, maintain it."
    elif 25 <= bmi < 30:
        message = "You are overweight, try to lose it and we are with you."
    else:
        message = "You are almost suffering from obesity. Try to go to the doctor."
    return BMI_out(bmi=bmi,message=message)

