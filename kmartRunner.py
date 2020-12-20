def runFromFile(inputFile):
    with open(inputFile, "r") as iFile:
        for iLine in iFile:
            numberArray = iLine.rstrip().split(' ')
            findLongestLength(numberArray)
    return True


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
