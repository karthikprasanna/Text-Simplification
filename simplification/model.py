import torch, transformers
from transformers import BartTokenizer, BartForConditionalGeneration
import os
import tqdm

def getWord(word):
  # if word[0] is a-z or A-Z ror 0-9 return word
    # else return from 1 to len(word)
    if word[0] != 'Ġ':
        return word
    else:
        return word[1:]

def readLine(file):
    sentence = ""
    for line in file:
        for ch in line:
            if ch != '.':
                sentence += ch
            else:
                sentence += ch
                return sentence

fileName1 = "BestCandidates.txt"
file_size = os.path.getsize(fileName1)
bytes_read = 0
file1 = open(fileName1, 'r')

file2 = open('simplified.txt', 'w')

import json
json_file = open('./vocab.json', 'r')
vocab = json.load(json_file)
json_file.close()

vocab = list(vocab.keys())
print('loading the model and the tokenizer')
tokenizer = BartTokenizer.from_pretrained("facebook/bart-large-cnn")
model = BartForConditionalGeneration.from_pretrained("simplifier.model")

for i, text in enumerate(file1):
    print(i, text)
    inputs = tokenizer(text,padding = True, truncation = True, return_tensors='pt')
    outputs = model(**inputs)
    # shape of outputs.logits batch_size, sequence_length, config.vocab_size
    sentence = ""
    for i in range(len(outputs.logits[0])):
        idx = torch.argmax(outputs.logits[0][i])
        sentence += getWord(vocab[idx]) + " "
    file2.write(sentence + "\n")
    
file1.close()
file2.close()


