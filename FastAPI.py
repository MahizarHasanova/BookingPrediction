# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 01:56:39 2023

@author: Mazi
"""

from fastapi import FastAPI
import pickle
from pydantic import BaseModel
import json

app = FastAPI()

class model_input(BaseModel):

         lead_time: float
         country:  float
         market_segment: float
         previous_cancellations: float
         deposit_type: float
         booking_season: float
         pca_column:float
         lda_column:float
         labels: float
         
 #loading model save        
model=pickle.load(open('random_forest_model.sav','rb'))         
         
         
@app.post('/model_prediction')
def model_pred(input_parameters :model_input):
    
    input_data= input_parameters.json()
    input_dictionary=json.loads(input_data)
    
    ltime=input_dictionary['lead_time']
    country=input_dictionary['country']
    mark=input_dictionary['market_segment']
    prev=input_dictionary['previous_cancellations']
    deps=input_dictionary['deposit_type']
    book=input_dictionary['booking_season']
    pca=input_dictionary['pca_column']
    lda=input_dictionary['lda_column']
    labels=input_dictionary['labels']
            
         
         
    input_list = [ltime,country,mark,prev,deps,book,pca,lda,labels]
    
    prediction = model.predict([input_list])
    
    if prediction[0]==0:
        return 'Rezerv iptal edilmir.'
    
    else:
        return 'Rezerv iptal edilir.'