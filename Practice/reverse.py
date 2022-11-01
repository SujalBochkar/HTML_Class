#reverse number
# numb=int(input("enter the number to be reversed"))
# rev = 0
# while (numb > 0):
#     sum=0
#     remainder=numb % 10
#     rev=(rev * 10)+ remainder
#     numb = numb //10
# print(rev)

#prime number
num=int(input("Enter the number greater than 1"))
count=0
i=1
while i<= num:
    if num % i==0 :
        count= count +1
    i= i +1
print(count)
if count==2:
    print("its a prime number")
else:
    print("Its composite number")
