import random
import json

import torch

from model import NeuralNet
from nltk_utils import bag_of_words, tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intent.json', 'r',encoding='utf-8') as json_data:
    intents = json.load(json_data)

FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

def reponse_chat(sentence):
    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    tmp=X.copy()
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.80:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                max_occ=0
                index=0
                for i in range(len(intent["responses"])):
                    rep=intent['responses'][i]
                    rep=bag_of_words(tokenize(rep),all_words)
                    if count_occur(tmp,rep)>=max_occ:
                        max_occ=count_occur(tmp,rep)
                        index=i
                return intent['responses'][index]
    else:
        return "Je suis désolé je n'ai pas compris votre question ou je n'ai pas encore la réponse à celle-ci. Pouvez-vous reformuler votre question avec une phrase courte et des termes simples ?"
def count_occur(sentence,reponse):
    return sum([1 for i in range(len(sentence)) if reponse[i]==sentence[i] and reponse[i]==1])