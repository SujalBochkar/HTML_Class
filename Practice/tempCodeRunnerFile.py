numb=int(input("enter the number to be reversed"))
rev = 0
while (numb > 0):
    sum=0
    remainder=numb % 10
    rev=(rev * 10)+ remainder
    numb = numb //10
print(rev)