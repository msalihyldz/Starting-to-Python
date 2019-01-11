

def perfectnumber (number):
    total = 0
    for i in range(1,number):
        if(number%i == 0):
            total += i
    if(total==number):
        print(number,"is a perfect number.")
    else:
        print(number,"is not a Perfect Number.")
    return total

while True:
    number= input("Please write a number:")
    if (number == 'q'):
        print("Program Closing...")
        break
    else:
        number=int(number)
        perfectnumber (number)