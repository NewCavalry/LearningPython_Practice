def main():
    daysOfTheWeek = ["Monday Blues", "Fat Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunny Sunday"]
    # print(daysOfTheWeek)
    # print(daysOfTheWeek[4])
    # len(daysOfTheWeek) #length function tells how many objects ??maybe only works in Terminal if Python is installed?
    # daysOfTheWeek[4] = "Yay, it's Friday" #another only works in Terminal if Python is installed?
    # look up list slicing
    
    print () #this just leaves a space
    print("The days of the week are", end=" ")
    for currentDayoftheWeekIndex in range ( len(daysOfTheWeek)):
        if currentDayoftheWeekIndex == len(daysOfTheWeek) -2:
            print(daysOfTheWeek[currentDayoftheWeekIndex], end=" ")
        elif currentDayoftheWeekIndex == len(daysOfTheWeek) -1:
            print("and", daysOfTheWeek[currentDayoftheWeekIndex], end=". ")
        else:
            print(daysOfTheWeek[currentDayoftheWeekIndex], end=", ")

    print()
    print()


main()