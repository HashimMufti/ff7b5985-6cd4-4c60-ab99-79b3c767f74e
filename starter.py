def fileLineCount(file1, file2):
    with open(file1, "r") as iFile, open(file2, "r") as oFile:
        if int(sum(1 for _ in iFile)) == int(sum(1 for _ in oFile)):
            return True 

def fileCompare(file1, file2):
    with open(file1, "r") as iFile, open(file2, "r") as oFile:
        for iLine, oLine in zip(iFile, oFile):
            if iLine != oLine:
                return False
    return True

def testRunner(inputFile, inputFile2):
    if fileLineCount(inputFile, inputFile2):
        print("HELLO)")
    print(fileCompare(inputFile, inputFile2))

inputFile = "testCasesInput.txt"
inputFile2 = "testCasesInputBlaBla.txt"
outputFile = "testCasesOutput.txt"
testRunner(inputFile, inputFile2)

        
    
