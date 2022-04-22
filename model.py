import joblib 
import json
import numpy as np


# loading model
model=joblib.load('assets/HousePricePredict.joblib')

# loades city_ditrics
city_distics=json.load(open('assets/city_district.json'))

# loades columns
columns=json.load(open('assets/columns.json'))['data_columns']

def getLocations_dict():
  return city_distics
def predict_price(baths, land_size, beds, house_size,city,district):
    location=city+district
    location_index=columns.index(location)
    x=np.zeros(len(columns)) 
    x[0]=baths
    x[1]=land_size
    x[2]=beds
    x[3]=house_size
    x[location_index]=1
    predicted_value=model.predict([x])[0]/185*295
    return predicted_value 


# predict_price('Kothanur',1200,2,2)+7

if __name__=='__main__':
    print((predict_price(2,7,4,1700,'Angoda','Colombo'))*2)
