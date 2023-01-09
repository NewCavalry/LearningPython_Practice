# This is a string
name = "Desiree Girotto"
firstName = "Desiree"
lastName = "Girotto"
age = 54 # This is an int
bankAccountBalance = 123456.78

# This is displayig the values of the variable above using the Print function
print (name, age, bankAccountBalance)

# Operators
# sep is for the separator (by default it is a space)
firstNumber = 5
secondNumber = 10
#sep stands for separator (by defualt it's a space, whatever value you give it like the dashes below)
print(firstNumber + secondNumber, 88, "Another String", sep=" -- ")
# print value by default ends in separate line using end below means lines go together
print(firstNumber + secondNumber, 88, "Another String", sep=" -- ", end=" ")
print("Line 2")
print("Another Line")

#Input and Output Functions
userName = input("Please enter your name: ")

print("You typed in", userName)