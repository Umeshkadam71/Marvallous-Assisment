#def chknum():
 #   a = int()
  #  b = int()
   # return a, b

def evenodd():
    x = int(input("Enter a number: "))
    #a, b = chknum()
    if x % 2 !=0:
        print("Odd number")
    else:
        print("Even number")

def main():
    evenodd()

if __name__ == "__main__":
    main()