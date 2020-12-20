import argparse


def runFromFile(inputFile):
    """Runs findLongestLength on each line in input file,
    returning an array of arrays as solution.

    Args:
        inputFile (String): Name of inputfile to run on

    Returns:
        Array: An array containing n number of arrays (where
            n represents the number of lines in inputFile)
    """
    with open(inputFile, "r") as iFile:
        solutionArray = []
        for iLine in iFile:
            numberArray = iLine.rstrip().split(' ')
            solutionArray.append(findLongestLength(numberArray))
    return solutionArray


def findLongestLength(inputArray):
    """Finds and returns the longest positive sequence in an array

    Args:
        inputArray (Array): An array of integers where
            each value is split by a space

    Returns:
        Array: Returns an array of string integers.
    """
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


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--a",
                        nargs="*",
                        type=int,
                        help='input integer array seperated by whitespace',
                        dest='a',
                        default=False
                        )
    parser.add_argument('-t', action='store_true', default=False,
                        dest='t',
                        help='Show input/output text')
    args = parser.parse_args()
    if args.t:
        print("Input:", args.a)
        print("Output:", findLongestLength(args.a))
    else:
        print(findLongestLength(args.a))
