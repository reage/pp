import re

def countLines(filePath):
    codeLine = 0
    commentLine = 0
    blankLine = 0
    flag = 0
    try:
        with open(filePath) as file:
            for line in file:
                line = line.strip()
                if len(line) > 1 and line[0] == "#":
                    commentLine += 1
                elif len(line.split('"""')) == 3:
                    commentLine += 1
                elif len(line) > 1 and line.find('"""') != -1:
                    commentLine += 1
                    flag = 1
                elif flag == 1 and line.find('"""') != -1:
                    commentLine += 1
                    flag = 0
                elif line.split() == []:
                    blankLine += 1
                elif flag == 1:
                    commentLine += 1
                else:
                    codeLine += 1
    except IOError as err:
        print (str(err))
    return (codeLine, commentLine, blankLine)
