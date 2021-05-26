import time
# O(N^2) Time Complexity 
# O(1) Space Complexity 
def insertionSort(data, drawData, timeTick): 
    for i in range (len(data)): 
        j = i 
        while j > 0 and data[j-1] > data[j]: 
            data[j-1], data[j] = data[j], data[j-1]
            j -= 1
            drawData(data, ['red' if x == j or x == j + 1 else 'blue' for x in range(len(data))])
            time.sleep(timeTick)
