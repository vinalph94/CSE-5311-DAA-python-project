import numpy as np
import pandas as pd
import time 

def main():
    arr20 = readInputSet('arr20.txt')
    performMergeSort(arr20, 'arrMS_0_20.txt')
    
    arr100 = readInputSet('arr100.txt')
    performMergeSort(arr100, 'arrMS_0_100.txt')
    
    arr1000 = readInputSet('arr1000.txt')
    performMergeSort(arr1000, 'arrMS_0_1000.txt')
    
    arr4000 = readInputSet('arr4000.txt')
    performMergeSort(arr4000, 'arrMS_0_4000.txt')

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

def performMergeSort(inputArray, outputFile):
    start = time.perf_counter()
    result = mergeSort(inputArray, key=lambda x: x[3])
    elapsed = (time.perf_counter() - start)
    print("result", result)
    df = pd.DataFrame(result)
    print(df.to_string(index = False, header = False))
    print(elapsed)
    writeOutputSets(df, outputFile, elapsed)

def mergeSort(inputArray, key=lambda x: x):
    if len(inputArray) > 1:
        middle = len(inputArray)//2
        left = inputArray[:middle]
        right = inputArray[middle:]
        
        mergeSort(left, key=lambda x: x[3])
        mergeSort(right, key=lambda x: x[3])
        merge(inputArray, left, right, key=lambda x: x[3])
    return inputArray
        
def merge(inputArray, left, right, key=lambda x: x[3]):
    i = j = k = 0
    while i < len(left) and j < len(right):
        if key(left[i]) <= key(right[j]):
            inputArray[k] = left[i]
            i += 1
        else:
            inputArray[k] = right[j]
            j += 1

        k += 1
    while i < len(left):
        inputArray[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        inputArray[k] = right[j]
        j += 1
        k += 1

    return inputArray

            
def writeOutputSets(arr, fileName, sortTime):
    with open(fileName, 'a') as f:
        dfAsString = arr.to_string(header = False, index = False)
        f.write(dfAsString)
        f.write(f"\n{sortTime}")

main()