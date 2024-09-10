n = int(input())
words = input().split()
count = 0
sentence = ""
i = 0
while i < len(words):
    sentence = sentence+words[i]
    count = count + len(words[i]) + 1
    if i == len(words)-1:
        print(sentence)
    if count <= 81 :
        sentence = sentence+" "
    else:
        sentence = " ".join(sentence.split()[0:-1])
        i -= 1
        print(sentence)
        sentence = ""
        count = 0
    i += 1