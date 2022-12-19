import numpy as np
import pandas as pd
import time

def main():
    # function to generate set of numbers
    generateNumberSets()

    # reads the input from the generated arr20.txt file and performs insertion sort  
    # and save the sorted results along with the sorting time.
    arr20= readInputSet('arr20.txt')
    performInsertionSort(arr20,'arrIS_O_20.txt')

    # reads the input from the generated arr100.txt file and performs insertion sort  
    # and save the sorted results along with the sorting time.
    arr100= readInputSet('arr100.txt')
    performInsertionSort(arr100,'arrIS_O_100.txt')

    # reads the input from the generated arr1000.txt file and performs insertion sort  
    # and save the sorted results along with the sorting time.
    arr1000= readInputSet('arr1000.txt')
    performInsertionSort(arr1000,'arrIS_O_1000.txt')

    # reads the input from the generated arr4000.txt file and performs insertion sort  
    # and save the sorted results along with the sorting time.
    arr4000= readInputSet('arr4000.txt')
    performInsertionSort(arr4000,'arrIS_O_4000.txt')

#function to read the set of numbers from the generated input files and computes the sum of each row  
def readInputSet(filename):
    sortingArray = np.loadtxt(filename,dtype ='int')
    df = pd.DataFrame({ 'X':[row[0] for row in sortingArray],
                        'Y':[row[1] for row in sortingArray],
                        'Z':[row[2] for row in sortingArray]})
    df = df.eval('Sum = X + Y + Z')
    print(df)
    arr = df.values.tolist()
    print("to list", arr)
    return arr

#function initiates the insertion sorting algorithm, monitors the computation time of the algorithm and saves the sorted output to a file
def performInsertionSort(inputArray,outputFile):
    start = time.perf_counter()
    result = insertionSort(inputArray, key=lambda x: x[3])
    elapsed = (time.perf_counter() - start)
    print("result", result)
    df = pd.DataFrame(result)
    print(df.to_string(index=False, header=False))
    print (elapsed)
    #writeOutputSets( np.matrix(df),'arrIS_O_20.txt',elapsed)
    writeOutputSets( df,outputFile,elapsed)

#fuction executes the logic of insertion sort algorithm 
def insertionSort(inputArray, key=lambda x: x):
    for index in range(1, len(inputArray)):
        currentVal = inputArray[index]
        position = index
        while position > 0 and key(inputArray[position - 1]) > key(currentVal):
            inputArray[position] = inputArray[position - 1]
            position = position - 1
        inputArray[position] = currentVal
    return inputArray

#the below function generates the set of 3 numbers using random numbers from 0 to 99 .
def generateNumberSets():

    # generates set of 3 numbers in a list of 20,100,1000,4000 from random integers between 0 and 99 and saves them in a file 
    array20 = np.random.randint(0,99, size=(20, 3), dtype=int)
    saveNumberSets(array20,'arr20.txt')
  
    array100 = np.random.randint(0,99, size=(100, 3), dtype=int)
    saveNumberSets(array100,'arr100.txt')

    array1000 = np.random.randint(0,99, size=(1000, 3), dtype=int)
    saveNumberSets(array1000,'arr1000.txt')

    array4000 = np.random.randint(0,99, size=(4000, 3), dtype=int)
    saveNumberSets(array4000,'arr4000.txt')

#this function saves the random number sets generated in arr20txt, arr100.txt, arr1000.txt and arr4000.txt respectively
def saveNumberSets(arr,fileName):
    matrix = np.matrix(arr)
    with open(fileName,'wb') as f:
        for line in matrix:
            np.savetxt(f, line, fmt='%d')

# function to save the sorted output and computation time to text files.
def writeOutputSets(arr,fileName,sortTime):
    with open(fileName, 'a') as f:
        dfAsString = arr.to_string(header=False, index=False)
        f.write(dfAsString)
        f.write(f"\n{sortTime}")


main()