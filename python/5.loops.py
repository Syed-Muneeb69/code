#Loops
#for
#break
nums = [1 ,2 ,3,4,5]
for num in nums:
    if num ==3:
        print("found")
        break#condition met break out of the loop
        print(num)
#continue  
nums = [1 ,2 ,3,4,5]
for num in nums:
    if num ==3:
        print("found")
        continue#condition met continues with next iterations of the loop
    print(num)
 
for num in nums:
   for letter in "abc":
    print(num,letter)

#range
for i in range(10):
   print(i)
   for i in range(1,11):
      print(i)
#while
x=0
while x < 10:
   print(x)
   x=x+1
#infinite loop
while True:
   if x == 5:
    break
   print(x)
   x+=1
   
    



