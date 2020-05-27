# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



#importing libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import nltk
from bs4 import BeautifulSoup
from nltk.tokenize import RegexpTokenizer 
from keras.models import Sequential,load_model
from keras.layers.core import Dense,Activation
from keras.layers import LSTM
from keras .optimizers import RMSprop
import pickle
import heapq
import string

#importing data
train_data=pd.read_csv('train.csv',engine='python')
train_data=train_data.iloc[0:999,5].values
test_data=pd.read_csv('test.csv',engine='python')
test_data=test_data.iloc[0:999,5].values


#Removing HTML
def remove_html(text):
    soup=BeautifulSoup(text,'lxml')
    html_free=soup.get_text()
    return html_free

#Spliting sentences into words 
tokenizer=RegexpTokenizer(r'\w+')
words=[]
for i in range(0, 999):
 words.append(tokenizer.tokenize(train_data[i]))
 

#Vocabulary size
 count=0
unique_word_index=[]
unique_words=np.unique(words)
unique_word_index.append( dict((c,i)for i,c in enumerate(unique_words[0])))
for k in range (1,998):
    count+=len(unique_words[k])-1
    unique_word_index.append( dict((c,i)for i,c in enumerate(unique_words[k],count)))
    


LENGTH=4
prev_words=[]
next_words=[]

for k in range(0, 999):

  prev_words.append(words[k][i:i+LENGTH]  for i in range(len(words[k])-LENGTH))
  next_words.append(words[k][i+LENGTH]  for i in range(len(words[k])-LENGTH))



