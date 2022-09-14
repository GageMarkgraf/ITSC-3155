dictionary = {

}

def main():
    numItems = input("Number of items: ")
    numItems = int(numItems)
    for i in range(0, numItems):
        item = input("Input item and price: ")
        itemSep = item.split(" ")
        dictionary[itemSep[0]] = int(itemSep[1])
    sortedDict = dict(sorted(dictionary.items(), key=lambda item: item[1]))
    for i in sortedDict:
            print(i, sortedDict[i])
        

if __name__ == "__main__":
    main()
