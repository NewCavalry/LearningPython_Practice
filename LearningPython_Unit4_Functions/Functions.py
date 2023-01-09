def displayMath():
    print("The sum of 2 + 2 = 4")

# Function Argurment Example
def displayMathAdvanced(firstNumber, secondNumber): #firstNumber and secondNumber are the parameters
    answer = firstNumber + secondNumber
    print ("The sum of", firstNumber, "+", secondNumber, "is", answer)

# Return Values - Scope and Global Values
def displayMathSuperAdvanced(firstNumber, secondNumber, thirdNumber):
    difference = firstNumber - secondNumber - thirdNumber
    return difference

# Multiple Return Values
def applyBasicCalculations(firstNumber, secondNumber):
    sum = firstNumber + secondNumber
    difference = firstNumber - secondNumber
    product = firstNumber * secondNumber
    quotient = firstNumber / secondNumber

    return sum, difference, product, quotient

# Always need a main function, this is always called first in any program
def main():
    sumValue, differenceValue, productValue, quotientValue = applyBasicCalculations(10, 3)   
    print (sumValue, differenceValue, productValue, quotientValue)

    main()



# displayMath()    

# displayMathAdvanced(5, 8.6) #positional arguments

# SuperAdvancedDifference = displayMathSuperAdvanced(10, 12, 2)
# print(SuperAdvancedDifference)