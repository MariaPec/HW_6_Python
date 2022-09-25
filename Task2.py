
text = str(input("Спой, Винни: "))
textList = text.split(" ")

resultList = []
count = 0
for j in range(len(textList)):
    for item in textList[j]:
        if item == "у" or item == "е" or item == "а" or\
        item == "о" or item == "э" or item == "я" or\
        item == "и" or item == "ю":
            count += 1
    resultList.append(count)
    count = 0

if resultList.count(resultList[0]) == len(resultList):
    print("парам-пам-пам")
else: print("пам-парам")
    