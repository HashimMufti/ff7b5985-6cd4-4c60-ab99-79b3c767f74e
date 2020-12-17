def fileLineCount(file1, file2):
    with open(file1, "r") as iFile, open(file2, "r") as oFile:
        if int(sum(1 for _ in iFile)) == int(sum(1 for _ in oFile)):
            return True 

def fileCompare(file1, file2):
    with open(file1, "r") as iFile, open(file2, "r") as oFile:
        testCaseNumber = 1
        for iLine, oLine in zip(iFile, oFile):
            print("For testcase ", testCaseNumber)
            numberArray = iLine.rstrip().split(' ')
            if findLongestLength(numberArray) != oLine.rstrip().split(' '):
                print("TEST CASE FAILED!")
                print(numberArray)
                print(findLongestLength(numberArray))
                print(oLine.rstrip().split(' '))
                return False
            print("Test case passed")
            testCaseNumber += 1
    return True

def fileWrite(inputFile):
    with open(inputFile, "r") as iFile:
        for iLine in iFile:
            numberArray = iLine.rstrip().split(' ')
            findLongestLength(numberArray)
    return True

def testRunner(inputFile, inputFile2):
    if fileLineCount(inputFile, inputFile2):
        print(fileCompare(inputFile, inputFile2))

def findLongestLength(inputArray):
    maxLengthArray = []
    tempArray = []
    for number in inputArray:
        # Base case (first run)
        if len(tempArray) < 1:
            tempArray.append(number)
        # Case where number is greater end of array
        elif int(number) > int(tempArray[-1]):
            tempArray.append(number)
        # Case where number is smaller than end of array
        else:
            if len(tempArray) > len(maxLengthArray):
                maxLengthArray = tempArray
            tempArray = []
            tempArray.append(number)
    # Compare last array in memory to current max array
    if len(tempArray) > len(maxLengthArray):
        maxLengthArray = tempArray
    return maxLengthArray
                    
        
testArray = [6,1,5,9,2]
#print(findLongestLength(testArray))
#fileWrite("realTestCasesInput.txt")
inputFile = "testCasesInput.txt"
inputFile2 = "testCasesInputBlaBla.txt"
outputFile = "testCasesOutput.txt"
simpleInput = "testCasesSimpleInput.txt"
simpleOutput = "testCasesSimpleOutput.txt"
realInput = "realTestCasesInput.txt"
realOutput = "realTestCasesOutput.txt"
#testRunner(simpleInput, simpleOutput)
testRunner(realInput, realOutput)
        
    
