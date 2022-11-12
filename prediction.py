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
from textblob import TextBlob


def extractionPkl():
  """
  file1=open('nmf_model.pkl','rb') 
  file2=open('nmf_vectorizer','rb')
  """
  with (open("vectorizer", "rb")) as f:
      file2=pickle.load(f)
        
  with (open("model", "rb")) as p:
   file1=pickle.load(p)
      
  return file1 ,file2



extractionPkl()

def prediction(model,vectorizer,n_topic,new_reviews):
  blob=TextBlob(new_reviews)
  sentimentBlob=blob.sentiment.polarity
  new_reviews = [new_reviews]
  new_reviews_transformed=vectorizer.transform(new_reviews)

  prediction= model.transform(new_reviews_transformed)
 
  topics=['organisation manager','qualité sauce ','garniture pizza','Prix abordable','temps d arriver','qualité nourriture restaurant','la qualité du burger','qualiter service','qualité service bar','plat mexicain','ordre service','hestetique du lieux','menu poulet frit','qualité des sandwitchs','temp attente']
  if sentimentBlob<0 and sentimentBlob>-1:
 
    max = np.argsort(prediction)
    max_list=(list(max[0]))
    max_list.reverse()
    print(max_list)
    topic=[]
    for i in range(n_topic):
      topic.append(topics[max_list[i]])  
    return sentimentBlob,prediction,topic

  return sentimentBlob ,'text' ,'Le commentaire est plutot positif'

#prediction(extractionPkl()[0],extractionPkl()[1],2,)[2]




