import string
from collections import Counter

def returnMostUsedWord(filePath):
    with open(filePath) as fileData:
        filter = string.punctuation
        data = fileData.read()
        table = data.maketrans(",", " ", string.punctuation)
        data = data.translate(table)
        all = data.split()
        result = Counter(all)
        return ((result.most_common()[0:1])[0][0])
