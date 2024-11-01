#Alannah Steck
#U3L3
#merge sort
#ʕ •ᴥ•ʔ the good luck bear

def mergeSort(numberList):
  if len(numberList) > 1: #if for base case
    middle = int(len(numberList)/2)
    left = numberList[:middle]
    right = numberList[middle:]

    #print("OG", numberList)
    #print("L", left)
    #print("R", right, "\n\n")

    sortedLeft = mergeSort(left) #recursive call
    sortedRight = mergeSort(right)

    #print(f"Ready to merge: {sortedLeft} and {sortedRight}\n")
    finalList = []
    while len(sortedLeft) > 0 and len(sortedRight) > 0:
      if sortedLeft[0] > sortedRight[0]:
        #print(f"{sortedLeft[0]} > {sortedRight[0]}")
        finalList.append(sortedRight[0])
        sortedRight.pop(0)
      elif sortedLeft[0] < sortedRight[0]:
        #print(f"{sortedLeft[0]} < {sortedRight[0]}")
        finalList.append(sortedLeft[0])
        sortedLeft.pop(0)
          
      else:
        #print(f"{sortedLeft[0]} == {sortedRight[0]}")
        finalList.append(sortedLeft[0])
        sortedLeft.pop(0)
        finalList.append(sortedRight[0])
        sortedRight.pop(0)
    if len(sortedLeft) > 0:
      for item in sortedLeft:
        finalList.append(item)
    else:
      for item in sortedRight:
        finalList.append(item)

    return finalList
  
  #print(f"Base case: {numberList}\n")
  return numberList

def main():
    nums1 = [6,2,5,8,3,4,8]
    nums2 = [1,2,3,4,5,6,7,8]
    nums3 = [8,2,6,0,1,3]
    for numList in [nums1, nums2, nums3]:
        print(f"\nOriginal: {numList}")
        new = mergeSort(numList)
        print(f"Sorted: {new}\n")

if __name__ == "__main__":
    main()