
def armstrong(number):

    number = str(number)
    a = 0
    for i in number:

        a += int(i)**3
    if (int(number)==a):
        return True
    else:
        return False

while True:
    number =int(input("Please write a number:"))
    if(armstrong (number)):
        print(number,"is an Armstrong Number")
    else:
        print(number,"is not an Armstrong Number")


