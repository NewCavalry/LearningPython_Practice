# def main(): #this creates a new file
#     testFile = open("testFile.txt", "w") #w=write, a=append/add to existing, r=read

#     testFile.write("2\n") # \n is for new line
#     testFile.write("4\n")
#     testFile.write("8\n")
#     testFile.write(str(16) + "\n") # other way to write numbers as strings, code won't accept integers

# main()    

# def main(): #this reads a  file
#     testFile = open("testFile.txt", "r")

#     line =  testFile.readline()
#     line = line.rstrip("\n")

#     while line !="":
#         print(line)
#         line = testFile.readline().rstrip("\n") #.rstrip("\n") gets rid of extra line at end

#     testFile.close() #always close after reading or writing to file to empty buffer
# main ()

def main(): #this reads a  file
    try:
        testFile = open("testFile.txt", "r")

        line =  testFile.readline()
        line = line.rstrip("\n")

        while line !="":
            print(line)
            # print(int(line)) use this or float? if you want it to be a numerical value

            line = testFile.readline().rstrip("\n") #.rstrip("\n") gets rid of extra line at end
    except Exception as potentialError:
        print(potentialError)
    else:
        print("All systems go")
    finally:
        testFile.close() #always close after reading or writing to file to empty buffer
        print("End of program")
main ()