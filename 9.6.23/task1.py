def findMissingNumbers(inputArray):
    startingNumber = inputArray[0]
    endingNumber = inputArray[len(inputArray)-1]
    perfectArray = []
    resultArray = []
    for i in range(endingNumber):
      perfectArray.append(i+startingNumber)
    for i in range(len(perfectArray)):
      if perfectArray[i] not in inputArray:
        resultArray.append(perfectArray[i])
    
    return resultArray


print(findMissingNumbers([1,3,6,7,8]))