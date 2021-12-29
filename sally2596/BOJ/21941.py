import sys
sentence = sys.stdin.readline().rstrip()
length = len(sentence)
num = int(sys.stdin.readline())
dic ={}
dic2={}
for i in range(num):
    lil_sentence,point = map(str,sys.stdin.readline().split())
    point = int(point)
    if len(lil_sentence)<point:
        dic[lil_sentence] = int(point)
        dic2[lil_sentence] = int(point)/len(lil_sentence)

dic2 = sorted(dic2.items(), key=lambda x:x[1], reverse=True)
cnt=0
for i in dic2:
    if i[0] in sentence:
        str_num = sentence.count(i[0])
        sentence = sentence.replace(i[0], "*")
        cnt+=str_num * dic[i[0]]
sentence = sentence.replace("*", "")
cnt+=len(sentence)
print(cnt if cnt>length else length)