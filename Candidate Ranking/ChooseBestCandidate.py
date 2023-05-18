fileName1 = 'candidates.txt'
file1 = open(fileName1, 'r')
candidate = ""

file2 = open('GoldScore.txt', 'r')
sentence_dst = ""

file3 = open('BestCandidates.txt', 'w')


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

import os
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

count = 1
while True:
    candidates = readCandidates(file1)
    print(count, candidates)
    print()
    count +=1
    max_score = -1.0
    best_candidate = ""
    
    if len(candidates) == 0:
        file3.write("\n")
        

    for cand in candidates:

        score = file2.readline().strip()
        if score == "":
            file1.close()
            file2.close()
            file3.close()
            exit()
        score = float(score)
        if score > max_score:
            max_score = score
            best_candidate = cand
    file3.write(best_candidate)

    # print(f'progress: {bytes_read/file_size*100:.2f}%', end='\r')


