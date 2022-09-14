def multiple(x, y):
    for i in range(x, y+1):
        if i % 7 == 0 and i % 5 != 0:
            print(i)
            
def main():
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    num1 = int(num1)
    num2 = int(num2)
    multiple(num1, num2)

if __name__ == "__main__":
    main()