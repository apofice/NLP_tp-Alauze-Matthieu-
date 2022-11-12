# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 17:25:21 2022

@author: matth
"""

"""
import nmf_model.pkl as model



import nmf_vectorizer.pkl as vectorizer

"""


import pandas as pd

import pickle
from pickle import load
import pandas as pd
import numpy as np
import textblob 
from textblob import *


def extractionPkl():

  file1=open('https://github.com/apofice/NLP_tp-Alauze-Matthieu-/blob/main/nmf_model.pkl','rb') 
  file2=open('https://github.com/apofice/NLP_tp-Alauze-Matthieu-/blob/main/nmf_vectorizer.pkl','rb')
    
  return load(file1) ,load(file2)



extractionPkl()

def prediction(model,vectorizer,n_topic,new_reviews):
  blob=TextBlob(new_reviews)
  sentimentBlob=blob.sentiment.polarity
  new_reviews = [new_reviews]
  new_reviews_transformed=vectorizer.transform(new_reviews)

  prediction= model.transform(new_reviews_transformed)
 
  topics=['qualité service bar','qualité sauce ','Prix abordable','temps d arriver','garniture pizza','qualité nourriture restaurant','qualiter service','plat mexicain','ordre service','hestetique du lieux','organisation manager','menu poulet frit','sandwitch','burger','temp attente']
  if sentimentBlob<0 and sentimentBlob>-1:
 
    max = np.argsort(prediction)
    max_list=(list(max[0]))
    max_list.reverse()
    print(max_list)
    topic=[]
    for i in range(n_topic):
      topic.append(topics[max_list[i]])  
    return sentimentBlob,prediction,topic

  return sentimentBlob
new_reviews = "I dont like chicken "
prediction(extractionPkl()[0],extractionPkl()[1],2,new_reviews)[2]



