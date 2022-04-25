import numpy as np
import json
import torch
import torch.nn as nn
from torch.utils.data import dataset,dataloader
from neural import bag_of_words,tokenize,stem
from Brain import NeuralNet

with open('intents.json','r') as f:
    intents=json.load(f)

allwords=[]
tags=[]
xy=[]

for intent in intents['intents']:
    tag=intent['tag']
    tags.append[tag]

    for pattern in intent['patterns']:
        w=tokenize(pattern)
        allwords.extend(w)
        xy.append((w,tag))

ignore_words=[',','?','/','.','!']
allwords=[stem(w for w in allwords if w not in ignore_words)]
allwords=sorted(set(allwords))
