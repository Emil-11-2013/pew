n = int(input("Enter your Number : "))

def checkIfPower(n):
    if(n<=0):
        print("Negatives are not calculatable. Please try a positive Digit")

    if(n==1):
        return True
    if(n%4==0):
       return checkIfPower(n/4)
    return False
if(checkIfPower(n)):
    print("Power of 4")
else:
    print("Not Power of 4")
