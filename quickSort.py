import time

# O(Nlog(N)) Time Complexity
# O(N) Space Complexity (Worst Case) and O(logN) Space Complexity average case
def partition(data, head, tail, drawData, timeTick):
    border = head
    pivot = data[tail]

    drawData(data, getcolorArray(len(data), head, tail, border, border))
    time.sleep(timeTick)

    for i in range(head, tail): 
        if data[i] < pivot: 
            drawData(data, getcolorArray(len(data), head, tail, border, i, True)) # calling visualization function
            time.sleep(timeTick)
            data[border], data[i] = data[i], data[border] 
            border += 1
        drawData(data, getcolorArray(len(data), head, tail, border, i))
        time.sleep(timeTick)
    # swap pivot with border
    drawData(data, getcolorArray(len(data), head, tail, border, tail, True)) # calling visualization function
    time.sleep(timeTick) 

    data[border], data[tail] = data[tail], data[border]
    return border 

def quickSort(data, head, tail, drawData, timeTick):
    if head < tail:
        partitionIndex = partition(data, head, tail, drawData, timeTick) 

        # LEFT PARTITION
        quickSort(data, head, partitionIndex-1, drawData, timeTick)

        # RIGHT PARTITION 
        quickSort(data, partitionIndex+1, tail, drawData, timeTick)

def getcolorArray(dataLength, head, tail, border, currentIndex, isSwapping=False):
    colorArray = [] 
    for i in range(dataLength):
        #base coloring 
        if i <= head and i <= tail: 
            colorArray.append('pink') # partially sorted pink
        else:
            colorArray.append('red') # red 
        if i == tail: 
            colorArray[i] = 'orange' # pivot, orange
        elif i == border: 
            colorArray[i] = 'blue'  # blue
        elif i == currentIndex:
            colorArray[i] = 'green' # green 
        
        if isSwapping: 
            if i == border or i == currentIndex: 
                colorArray[i] = 'red' # red for selected elements 
    return colorArray  
