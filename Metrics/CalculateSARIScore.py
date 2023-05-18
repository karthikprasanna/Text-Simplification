import os
from evaluate import load

fileName1 = 'data/ACL2020/train.src'
file1 = open(fileName1, 'r')
sentence1 = ""

file2 = open('data/output/BART_predicted.txt', 'r')
sentence2 = ""

file3 = open('data/ACL2020/train.dst', 'r')
sentence3 = ""

file_size = os.path.getsize(fileName1)
bytes_read = 0

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

avg_score = 0
count = 0

sari = load('sari')

print("reading the file")
sentence1 = readLine(file1)
sentence2 = readLine(file2)
sentence3 = readLine(file3)

while (sentence1 != None and sentence2 != None and sentence3 != None):
    bytes_read += len(sentence1)
    print(f"progress:{bytes_read*100/ file_size }% and avg:{avg_score}", end='\r')

    source = [sentence1]
    prediction = [sentence2]
    target = [sentence3]
    score = sari.compute(sources=source, predictions=prediction, references=[target])
    score = score['sari']

    avg_score *= count
    avg_score += score
    count += 1
    avg_score /= count

    sentence1 = readLine(file1)
    sentence2 = readLine(file2)
else:
    bytes_read = file_size

print(f"progress:{bytes_read*100/ file_size }%                    ")
print(f"avg_score: {avg_score}")

file1.close()
file2.close()
file3.close()