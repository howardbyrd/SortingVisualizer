import time
# O(Nlog(N)) Time Complexity
# O(N) Space Complexity 
def mergeSort(data, drawData, timeTick): 
    mergeSortAlg(data, 0, len(data)-1, drawData, timeTick)

def mergeSortAlg(data, left, right, drawData, timeTick): 
    if left < right: 
        midpoint = (left + right) // 2
        mergeSortAlg(data, left, midpoint, drawData, timeTick)
        mergeSortAlg(data, midpoint+1, right, drawData, timeTick)
        merge(data, left, midpoint, right, drawData, timeTick)

def merge(data, left, midpoint, right, drawData, timeTick): 
    drawData(data, getcolorArray(len(data), left, midpoint, right))
    time.sleep(timeTick)

    leftPart = data[left:midpoint+1]
    rightPart = data[midpoint+1:right+1]

    left_pointer = right_pointer = 0 

    for i in range(left, right+1): 
        if left_pointer < len(leftPart) and right_pointer < len(rightPart): 
            if leftPart[left_pointer] < rightPart[right_pointer]: 
                data[i] = leftPart[left_pointer]
                left_pointer += 1
            else: 
                data[i] = rightPart[right_pointer]
                right_pointer += 1 
        elif left_pointer < len(leftPart): 
            data[i] = leftPart[left_pointer]
            left_pointer += 1 
        else: 
            data[i] = rightPart[right_pointer]
            right_pointer += 1 
    drawData(data, ["red" if x >= left and x <= right else "blue" for x in range(len(data))])
    time.sleep(timeTick)
def getcolorArray(length, left, middle, right): 
    colorArray = [] 
    for i in range(length): 
        if i >= left and i <= right: 
            if i <= middle: 
                colorArray.append("red") # red
            else:
                colorArray.append("green") # green
        else: 
            colorArray.append("blue") # blue

    return colorArray
