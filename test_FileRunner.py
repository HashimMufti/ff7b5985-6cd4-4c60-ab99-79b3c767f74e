from kmartRunner import findLongestLength, runFromFile
import pytest


def fileLineCount(file1, file2):
    with open(file1, "r") as iFile, open(file2, "r") as oFile:
        assert int(sum(1 for _ in iFile)) == int(sum(1 for _ in oFile))


def fileCompare(file1, file2):
    with open(file1, "r") as iFile, open(file2, "r") as oFile:
        testCaseNumber = 1
        for iLine, oLine in zip(iFile, oFile):
            print("For testcase ", testCaseNumber)
            numberArray = iLine.rstrip().split(' ')
            assert findLongestLength(numberArray) == oLine.rstrip().split(' ')
            testCaseNumber += 1


def test_empty():
    emptyArray = []
    expectedEmptyArray = []
    assert expectedEmptyArray == findLongestLength(emptyArray)


def test_all_zeroes():
    zeroArray = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert [0] == findLongestLength(zeroArray)


def test_decreasing_sequence():
    decreasingArray = [5, 4, 3, 2, 1]
    assert [decreasingArray[0]] == findLongestLength(decreasingArray)


def test_increasing_sequence():
    increasingArray = [1, 2, 3, 4, 5, 6, 7]
    assert increasingArray == findLongestLength(increasingArray)


def test_negative_sequence():
    negativeArray = [-11, -10, -9, -8, -7, -6]
    assert negativeArray == findLongestLength(negativeArray)


def test_negative_positive_sequence():
    mixedArray = [-12, 11, 200, -5, 15, 300, 20]
    assert [-12, 11, 200] == findLongestLength(mixedArray)


def test_string():
    with pytest.raises(ValueError):
        findLongestLength('abcdefghijk')


def test_github_files():
    inputFile = "testFiles/realTestCasesInput.txt"
    inputFile2 = "testFiles/realTestCasesOutput.txt"
    fileLineCount(inputFile, inputFile2)
    fileCompare(inputFile, inputFile2)


def test_local_files():
    inputFile = "testFiles/testCasesSimpleInput.txt"
    inputFile2 = "testFiles/testCasesSimpleOutput.txt"
    fileLineCount(inputFile, inputFile2)
    fileCompare(inputFile, inputFile2)


def test_different_file_sizes():
    inputFile = "testFiles/testCasesInput.txt"
    inputFile2 = "testFiles/testCasesOutput.txt"
    with pytest.raises(AssertionError):
        fileLineCount(inputFile, inputFile2)


def test_run_from_file():
    inputFile = "testFiles/runFromFileTest.txt"
    inputArray = [['12', '22', '99'], ['-3', '5', '7', '8']]
    assert inputArray == runFromFile(inputFile)