import time
# O(N^2) Time Complexity 
# O(1) Space Complexity 
def bubbleSort(data, drawData, timeTick):
    for i in range(0, len(data) - 1): 
        for j in range(0, len(data) - 1 - i): 
            if data[j] > data[j+1]: 
                data[j], data[j+1] = data[j+1], data[j]
                drawData(data, ['red' if x == j or x == j + 1 else 'blue' for x in range(len(data))])
                time.sleep(timeTick)