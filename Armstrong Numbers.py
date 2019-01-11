
def armstrong(sayı):

    sayı = str(sayı)
    a = 0
    for i in sayı:

        a += int(i)**3
    if (int(sayı)==a):
        return True
    else:
        return False

while True:
    sayı =int(input("Please write a number:"))
    if(armstrong (sayı)):
        print(sayı,"is an Armstrong Number")
    else:
        print(sayı,"is not an Armstrong Number")


