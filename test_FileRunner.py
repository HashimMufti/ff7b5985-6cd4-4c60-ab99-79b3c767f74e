from kmartRunner import findLongestLength, runFromFile
import pytest


def fileLineCount(file1, file2):
    """Counts number of lines in each file (making sure they're the same).

    Args:
        file1 (String): Name of first file to count lines.
        file2 (String): Name of second file to count lines.
    """
    with open(file1, "r") as iFile, open(file2, "r") as oFile:
        assert int(sum(1 for _ in iFile)) == int(sum(1 for _ in oFile))


def fileCompare(file1, file2):
    """Runs findLongestLength on each line in file1
    comparing to each line in file2.

    Args:
        file1 (String): Name of file used as input to
            findLongestLength (each line in file is an array input).
        file2 (String): Name of file used to compare to output
            of findLongestLength on file1.
    """
    with open(file1, "r") as iFile, open(file2, "r") as oFile:
        testCaseNumber = 1
        for iLine, oLine in zip(iFile, oFile):
            print("For testcase ", testCaseNumber)
            numberArray = iLine.rstrip().split(' ')
            assert findLongestLength(numberArray) == oLine.rstrip().split(' ')
            testCaseNumber += 1


def test_empty():
    """Tests findLongestLength with an empty array.
    """
    emptyArray = []
    expectedEmptyArray = []
    assert expectedEmptyArray == findLongestLength(emptyArray)


def test_all_zeroes():
    """Tests findLongestLength with all zero array.
    """
    zeroArray = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert [0] == findLongestLength(zeroArray)


def test_decreasing_sequence():
    """Tests findLongestLength with a continuous decreasing sequence.
    """
    decreasingArray = [5, 4, 3, 2, 1]
    assert [decreasingArray[0]] == findLongestLength(decreasingArray)


def test_increasing_sequence():
    """Tests findLongestLength with a continuous increasing sequence.
    """
    increasingArray = [1, 2, 3, 4, 5, 6, 7]
    assert increasingArray == findLongestLength(increasingArray)


def test_negative_sequence():
    """Tests findLongestLength with a negative increasing sequence.
    """
    negativeArray = [-11, -10, -9, -8, -7, -6]
    assert negativeArray == findLongestLength(negativeArray)


def test_negative_positive_sequence():
    """Tests findLongestLength with a mixed positive/negative sequence.
    """
    mixedArray = [-12, 11, 200, -5, 15, 300, 20]
    assert [-12, 11, 200] == findLongestLength(mixedArray)


def test_string():
    """Tests findLongestLength with a string input decreasing sequence.
    """
    with pytest.raises(ValueError):
        findLongestLength('abcdefghijk')


def test_github_files():
    """Tests findLongestLength against the provided Github tests.
    """
    inputFile = "testFiles/realTestCasesInput.txt"
    inputFile2 = "testFiles/realTestCasesOutput.txt"
    fileLineCount(inputFile, inputFile2)
    fileCompare(inputFile, inputFile2)


def test_local_files():
    """Tests findLongestLength against the local simple tests.
    """
    inputFile = "testFiles/testCasesSimpleInput.txt"
    inputFile2 = "testFiles/testCasesSimpleOutput.txt"
    fileLineCount(inputFile, inputFile2)
    fileCompare(inputFile, inputFile2)


def test_different_file_sizes():
    """Tests findLongestLength against the local complex tests.
    """
    inputFile = "testFiles/testCasesInput.txt"
    inputFile2 = "testFiles/testCasesOutput.txt"
    with pytest.raises(AssertionError):
        fileLineCount(inputFile, inputFile2)


def test_run_from_file():
    """Tests runFromFile against the some simple tests.
    """
    inputFile = "testFiles/runFromFileTest.txt"
    inputArray = [['12', '22', '99'], ['-3', '5', '7', '8']]
    assert inputArray == runFromFile(inputFile)
