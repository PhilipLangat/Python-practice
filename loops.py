#Loops are also known as iteration control structures

#Print numbers 0 - 5 without a loop
'''
print("0")
print("1")
print("2")
print("3")
print("4")
print("5")
'''
count = 0
while count<=5:
    print(count)
    count = count+1
    
    
count = 100
while count>0:
    print(count)
    count = count-1
    
    
#For loop - It iterates over a sequence
name = "Mary"
for char in name:
    print(char)
    
fruits = ["Banana","Grapes","Oranges","Matunda Damu","WaterMelon","etc."]
for fruit in fruits:
    print(fruit)