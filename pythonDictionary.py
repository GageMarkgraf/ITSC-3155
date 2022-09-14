
dictOne = {

}
dictTwo = {

}
def combineDict(dictOne, dictTwo):
    dictCombine = {**dictOne, **dictTwo}
    for key, value in dictCombine.items():
        if key in dictOne and key in dictTwo:
            dictCombine[key] = dictOne[key] + dictTwo[key]
    print (dictCombine)

def main():
    dictionOne = input("Input first dictionary: ")
    dictionTwo = input("Input second dictionary: ")
    dictionOne = dictionOne[1:len(dictionOne) - 1]
    dictionTwo = dictionTwo[1:len(dictionTwo) - 1]
    dictionOne = dictionOne.replace(" ", "")
    dictionTwo = dictionTwo.replace(" ", "")
    dictionOne = dictionOne.replace("'", "")
    dictionTwo = dictionTwo.replace("'", "")
    oneSet = dictionOne.split(',')
    twoSet = dictionTwo.split(',')
    oneSetOne = oneSet[0].split(':')
    twoSetOne = twoSet[0].split(':')
    oneSetTwo = oneSet[1].split(':')
    twoSetTwo = twoSet[1].split(':')
    oneSetThree = oneSet[2].split(':')
    twoSetThree = twoSet[2].split(':')
    dictOne[oneSetOne[0]] = int(oneSetOne[1])
    dictOne[oneSetTwo[0]] = int(oneSetTwo[1])
    dictOne[oneSetThree[0]] = int(oneSetThree[1])
    dictTwo[twoSetOne[0]] = int(twoSetOne[1])
    dictTwo[twoSetTwo[0]] = int(twoSetTwo[1])
    dictTwo[twoSetThree[0]] = int(twoSetThree[1])
    combineDict(dictOne, dictTwo)

    
if __name__ == "__main__":
    main()