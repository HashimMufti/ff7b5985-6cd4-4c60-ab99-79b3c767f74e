from kmartRunner import findLongestLength, runFromFile
import pytest


def fileLineCount(file1, file2):
<<<<<<< HEAD
    """Counts number of lines in each file (making sure they're the same).

    Args:
        file1 (String): Name of first file to count lines.
        file2 (String): Name of second file to count lines.
=======
    """Counts number of lines in each file (making sure they're the same)

    Args:
        file1 (String): Name of first file to count lines
        file2 (String): Name of second file to count lines
>>>>>>> cc2257cb36b982a4127e9926b1693ffc4126dee1
    """
    with open(file1, "r") as iFile, open(file2, "r") as oFile:
        assert int(sum(1 for _ in iFile)) == int(sum(1 for _ in oFile))


def fileCompare(file1, file2):
    """Runs findLongestLength on each line in file1
<<<<<<< HEAD
    comparing to each line in file2.

    Args:
        file1 (String): Name of file used as input to
            findLongestLength (each line in file is an array input).
        file2 (String): Name of file used to compare to output
            of findLongestLength on file1.
=======
    comparing to each line in file2

    Args:
        file1 (String): Name of file used as input to
            findLongestLength (each line in file is an array input)
        file2 (String): Name of file used to compare to output
            of findLongestLength on file1
>>>>>>> cc2257cb36b982a4127e9926b1693ffc4126dee1
    """
    with open(file1, "r") as iFile, open(file2, "r") as oFile:
        testCaseNumber = 1
        for iLine, oLine in zip(iFile, oFile):
            print("For testcase ", testCaseNumber)
            numberArray = iLine.rstrip().split(' ')
            assert findLongestLength(numberArray) == oLine.rstrip().split(' ')
            testCaseNumber += 1


def test_empty():
<<<<<<< HEAD
    """Tests findLongestLength with an empty array.
=======
    """Tests findLongestLength with an empty array
>>>>>>> cc2257cb36b982a4127e9926b1693ffc4126dee1
    """
    emptyArray = []
    expectedEmptyArray = []
    assert expectedEmptyArray == findLongestLength(emptyArray)


def test_all_zeroes():
<<<<<<< HEAD
    """Tests findLongestLength with all zero array.
=======
    """Tests findLongestLength with all zero array
>>>>>>> cc2257cb36b982a4127e9926b1693ffc4126dee1
    """
    zeroArray = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert [0] == findLongestLength(zeroArray)


def test_decreasing_sequence():
<<<<<<< HEAD
    """Tests findLongestLength with a continuous decreasing sequence.
=======
    """Tests findLongestLength with a continuous decreasing sequence
>>>>>>> cc2257cb36b982a4127e9926b1693ffc4126dee1
    """
    decreasingArray = [5, 4, 3, 2, 1]
    assert [decreasingArray[0]] == findLongestLength(decreasingArray)


def test_increasing_sequence():
<<<<<<< HEAD
    """Tests findLongestLength with a continuous increasing sequence.
=======
    """Tests findLongestLength with a continuous increasing sequence
>>>>>>> cc2257cb36b982a4127e9926b1693ffc4126dee1
    """
    increasingArray = [1, 2, 3, 4, 5, 6, 7]
    assert increasingArray == findLongestLength(increasingArray)


def test_negative_sequence():
<<<<<<< HEAD
    """Tests findLongestLength with a negative increasing sequence.
=======
    """Tests findLongestLength with a negative increasing sequence
>>>>>>> cc2257cb36b982a4127e9926b1693ffc4126dee1
    """
    negativeArray = [-11, -10, -9, -8, -7, -6]
    assert negativeArray == findLongestLength(negativeArray)


def test_negative_positive_sequence():
<<<<<<< HEAD
    """Tests findLongestLength with a mixed positive/negative sequence.
=======
    """Tests findLongestLength with a mixed positive/negative sequence
>>>>>>> cc2257cb36b982a4127e9926b1693ffc4126dee1
    """
    mixedArray = [-12, 11, 200, -5, 15, 300, 20]
    assert [-12, 11, 200] == findLongestLength(mixedArray)


def test_string():
<<<<<<< HEAD
    """Tests findLongestLength with a string input decreasing sequence.
=======
    """Tests findLongestLength with a string input decreasing sequence
>>>>>>> cc2257cb36b982a4127e9926b1693ffc4126dee1
    """
    with pytest.raises(ValueError):
        findLongestLength('abcdefghijk')


def test_github_files():
<<<<<<< HEAD
    """Tests findLongestLength against the provided Github tests.
=======
    """Tests findLongestLength against the provided Github tests
>>>>>>> cc2257cb36b982a4127e9926b1693ffc4126dee1
    """
    inputFile = "testFiles/realTestCasesInput.txt"
    inputFile2 = "testFiles/realTestCasesOutput.txt"
    fileLineCount(inputFile, inputFile2)
    fileCompare(inputFile, inputFile2)


def test_local_files():
<<<<<<< HEAD
    """Tests findLongestLength against the local simple tests.
=======
    """Tests findLongestLength against the local simple tests
>>>>>>> cc2257cb36b982a4127e9926b1693ffc4126dee1
    """
    inputFile = "testFiles/testCasesSimpleInput.txt"
    inputFile2 = "testFiles/testCasesSimpleOutput.txt"
    fileLineCount(inputFile, inputFile2)
    fileCompare(inputFile, inputFile2)


def test_different_file_sizes():
<<<<<<< HEAD
    """Tests findLongestLength against the local complex tests.
=======
    """Tests findLongestLength against the local complex tests
>>>>>>> cc2257cb36b982a4127e9926b1693ffc4126dee1
    """
    inputFile = "testFiles/testCasesInput.txt"
    inputFile2 = "testFiles/testCasesOutput.txt"
    with pytest.raises(AssertionError):
        fileLineCount(inputFile, inputFile2)


def test_run_from_file():
<<<<<<< HEAD
    """Tests runFromFile against the some simple tests.
=======
    """Tests runFromFile against the some simple tests
>>>>>>> cc2257cb36b982a4127e9926b1693ffc4126dee1
    """
    inputFile = "testFiles/runFromFileTest.txt"
    inputArray = [['12', '22', '99'], ['-3', '5', '7', '8']]
    assert inputArray == runFromFile(inputFile)
