
def stringCut(string):
    if(len(string) < 2):
        print("String is too small, minimum of two characters")
    if(len(string) >= 2):
        string = string[:2] + string[len(string) -2 :]
        print(string)
def main():
    print("String:")
    stringOne = input()
    stringCut(stringOne)


if __name__ == "__main__":
    main()