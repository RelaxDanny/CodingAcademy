import nltk

from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

import numpy
import tflearn
import tensorflow
import random
import json

with open("intents.json") as file:
    data = json.load(file)

words = []
labels = []
docs_x = []
docs_y = []



for intent in data["intents"]: 
    for pattern in intent["patterns"]:
        wrds = nltk.word_tokenize(pattern) #will give a list 
        words.extend(wrds) #extend the list -> add all the words in the list
        docs_x.append(pattern)
        docs_y.append(intent["tag"]) # greeting, goodbye, age, name

    if intent["tag"] not in labels:
        labels.append(intent["tag"])

words = [stemmer.stem(w.lower()) for w in words if w!= "?"] 
# words = []
# for w in words:
#     if w!- "?":
#         words.append(stemmer.stem(w.lower()))
words = sorted(list(set(words))) #set => 반복되는 단어만 선택해서 리스트 형성.
# built -in sorted(list) => n log n 가장빠른 quick sort list[-1] -> max list[-2] second max
# [1,5,1,6,3,7,8,9]
# sorted(list) -> 순서를 나열 해준다.
# [1,1,3,5,6,7,8,9]
labels = sorted(labels)

training = []
output = []

out_empty = [0 for _ in range(len(labels))] # label리스트의 길이만큼 [0,0,0,0,0,0,0,0,...,0]

for x, doc in enumerate(docs_x): #enumerate => 같은 리스트이지만 x에는 index -> iterator -> counter /  doc = eachNum
    #doc = pattern
    bag = []
    wrds = [stemmer.stem(w.lower) for w in doc]

    for w in words:
        if w in wrds:
            bag.append(1)
        else:
            bag.append(0)
    
    output_row = out_empty[:]
    output_row[labels.index(docs_y[x])] = 1

    training.append(bag)
    output.append(output_row)

training = numpy.array(training)
output = numpy.array(output)
#wrds = [pattern이 lowercase 된거]

#Brute-force
#Greedy algorithm

#numpy = > 인공지능이 좋아하는 공부 format 
