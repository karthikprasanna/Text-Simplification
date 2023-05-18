from transformers import pipeline
import os

train_src_data_file = open('data/ACL2020/train.src', 'r')

predicted_file = open('BART_predicted.txt', 'w')

file_size = os.path.getsize('data/ACL2020/train.src')
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


summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

sentence = readLine(train_src_data_file)

print("predicting")
while (sentence != None):
    bytes_read += len(sentence)
    print(f"progress:{bytes_read*100/ file_size }%")

    predicted = summarizer(sentence, max_length=130, min_length=30, do_sample=False)
    predicted = predicted[0]['summary_text']

    predicted_file.write(predicted)
    predicted_file.write('\n')

    sentence = readLine(train_src_data_file)
else:
    bytes_read = file_size

print(f"progress:{bytes_read*100/ file_size }%                    ")

train_src_data_file.close()
predicted_file.close()