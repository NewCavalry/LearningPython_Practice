# Loops
userAge = 1

for currentNumber in range (5): # 0, 1, 2, 3, 4 -- always starts with 0 for first number  
    print(currentNumber)
# for currentNumber in range (1, 5): will display 1, 2, 3, 4 
# for currentNumber in range (1, 11, 2): will display 1, 3, 5, 7, 9 (displays every second number) 

# Continue Function    
for currentNumber in range (10):
    if currentNumber ==5:
        continue
    else:
        print(currentNumber)

# Break Function    
for currentNumber in range (1, 10):
    if currentNumber ==4: # displays only 1, 2, 3 breaks at 4
        break

    print(currentNumber)
