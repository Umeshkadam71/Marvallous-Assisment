def div():
    a = int(input("Enter a number which is divisible by 5: "))
    if a % 5 == 0:
        print("True")
    else:
        print("Incorrect")

def main():
    div()

if __name__ == "__main__":
    main()
