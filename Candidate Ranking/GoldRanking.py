import os
from evaluate import load
import math

fileName1 = 'candidates.txt'
file1 = open(fileName1, 'r')
candidate = ""
candidates = []

file2 = open('data/ACL2020/train.dst', 'r')
sentence_dst = ""

file3 = open('data/ACL2020/train.src', 'r')
sentence_src = ""

file4 = open('GoldScore.txt', 'w')

# read and print the first sentence in the file
def readLine(file):
    sentence = ""
    for line in file:
        for ch in line:
            if ch != '.':
                sentence += ch
            else:
                sentence += ch
                return sentence
# each sentences are seperated by <#>
# each candidate of a given sentence is seperated by <$>
# function to read all the candidates of the first sentence in the file
file_size = os.path.getsize(fileName1)
bytes_read = 0
def readCandidates(file):
    candidates = []
    marker = ""
    for line in file:
        for ch in line:
            global bytes_read
            global candidate
            bytes_read += 1

            if ch == '<' or ch == '#' or ch == '$' or ch == '>':
                marker += ch
            else:
                if marker == "<#>":
                    marker = ""
                    return candidates
                elif marker == "<$>":
                    marker = ""
                    candidates.append(candidate)
                    candidate = ""
                elif marker != "":
                    candidate += marker
                    marker = ""
                candidate += ch
    return candidates

print("loading the bertscore")
bertscore = load("bertscore") 
def BERTScore(candidate, sentence):
    prediction = [candidate]
    target = [sentence]
    score = bertscore.compute(predictions = prediction, references = target, lang = "en")
    score = score["f1"][0]
    return score

Lambda = 1
while (sentence_dst != None and candidates != None and sentence_src != None):
    sentence_dst = readLine(file2)
    candidates = readCandidates(file1)
    sentence_src = readLine(file3)


    for candidate in candidates:
        phi_y = len(sentence_dst) / len(sentence_src)
        phi_v = len(candidate) / len(sentence_src)
        length_score = math.exp(-Lambda * abs(phi_y - phi_v))
        bert_score = BERTScore(candidate, sentence_dst)
        score = length_score * bert_score
        file4.write(str(score) + "\n")
        print(f"progress:{bytes_read*100/ file_size }% score: {length_score}", end='\r')

print(f'progress:{bytes_read*100/ file_size }%                    ')



file1.close()
file2.close()
file3.close()
file4.close()