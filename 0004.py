def countWords(file):
    wordsCount = 0
    with open(file, "r") as f:
        for line in f:
            words = line.split()

            wordsCount += len(words)
    print (wordsCount)
