# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 19:32:30 2022

@author: ed5ch
"""
import time
import pandas as pd
import numpy as np

def main():
    arr20 = readInputSet('arr20.txt')
    performQuickSort(arr20, 'arrQS_0_20.txt')
    
    arr100 = readInputSet('arr100.txt')
    performQuickSort(arr100, 'arrQS_0_100.txt')
    
    arr1000 = readInputSet('arr1000.txt')
    performQuickSort(arr1000, 'arrQS_0_1000.txt')
    
    arr4000 = readInputSet('arr4000.txt')
    performQuickSort(arr4000, 'arrQS_0_4000.txt')

def readInputSet(filename):
    sortingArray = np.loadtxt(filename, dtype = 'int')
    df = pd.DataFrame({ 'X':[row[0] for row in sortingArray],
                        'Y':[row[1] for row in sortingArray],
                        'Z':[row[2] for row in sortingArray]})
    df = df.eval('Sum = X + Y + Z')
    print(df)
    arr = df.values.tolist()
    print("to list", arr)
    return arr

def performQuickSort(inputArray, outputFile):
    start = time.perf_counter()
    result = quickSort(inputArray, 0, len(inputArray) - 1)
    elapsed = (time.perf_counter() - start)
    print("result", result)
    df = pd.DataFrame(result)
    print(df.to_string(index = False, header = False))
    print(elapsed)
    writeOutputSets(df, outputFile, elapsed)

def quickSort(inputArray, low, high, key=lambda x: x):
    if low < high:
  
        split = partition(inputArray, low, high)
        quickSort(inputArray, low, split - 1, key=lambda x: x[3])
        quickSort(inputArray, split + 1, high, key=lambda x: x[3])
    return inputArray

def partition(inputArray, low, high, key=lambda x: x[3]):
    pivot = key(inputArray[high])
    
    i = low - 1
    for j in range(low, high):
        if key(inputArray[j]) <= pivot:
            i = i + 1
            (inputArray[i], inputArray[j]) = (inputArray[j], inputArray[i])
    (inputArray[i + 1], inputArray[high]) = (inputArray[high], inputArray[i + 1])
    return i + 1

def writeOutputSets(arr, fileName, sortTime):
    with open(fileName, 'a') as f:
        dfAsString = arr.to_string(header = False, index = False)
        f.write(dfAsString)
        f.write(f"\n{sortTime}")

main()