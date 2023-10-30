

#Question1
user_input = input("Enter a number: ")
print(len(str(user_input)))


#Question2
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    print("*" * i)

#Question 3
list1 = [54, 76, 2, 4, 98, 100]
int1=int(input("Enter the first integer: "))
int2=int(input("Enter the second integer: "))
while int1<2 or int1>100 or int2<2 or int2>100:
    print("Invalid input. Please enter integers between 2 and 100.")

if int1 > int2:
    int1, int2 = int2, int1

for value in list1:
    if int1 <= value <= int2:
        print(value)


#Question 4
Names = ["Maria", "Hala", "Ghady", "Ehsan", "Joe", "Zoe"]
while True:
    letter = input("Enter a letter: ")
    for name in Names:
        if letter in name.lower():
            print(name)





