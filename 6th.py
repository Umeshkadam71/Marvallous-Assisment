def poneze():
    a = int(input("Please enter the number: "))

    if a > 0:
        print("Positive")
    elif a < 0:
        print("Negative")
    else: 
        print("zero")

def main():
    poneze()

if __name__ == "__main__":
    main()