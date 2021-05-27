
def getFizzBuzzResult(val):
    if(val%3 == 0 and val%5 == 0):
        return "FizzBuzz"
    elif(val%5==0):
        return "Buzz"
    elif(val%3==0):
        return "Fizz"
    return str(val)

def printAll():
    for x in range(1,101):
        print(getFizzBuzzResult(x))

printAll()
