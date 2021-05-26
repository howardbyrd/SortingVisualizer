from tkinter import *
from tkinter import ttk
import random
from bubbleSort import bubbleSort
from insertionSort import insertionSort
from mergeSort import mergeSort
from quickSort import quickSort

root = Tk()
root.title('Sorting Algorithm Visualization')
root.maxsize (900, 900)
root.config(bg='black')


#variabbles
selectedAlg = StringVar()
data = []

def drawData(data, colorArray):
    canvas.delete("all")
    canvasHeight = 380
    canvasWidth = 600
    xWidth = canvasWidth / (len(data) + 1)
    offset = 30
    spacing = 10
   
    normalizedData = [ i / max(data) for i in data]
    for i, height in enumerate(normalizedData): #Iterates through a list while simultaneously tracking its index
        #top left
        x0 = i * xWidth + offset + spacing
        y0 = canvasHeight - height * 340
        #bottom right
        x1 = (i + 1) * xWidth + offset
        y1 = canvasHeight
        
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        canvas.create_text(x0+2, y0, anchor=SW, text=str(data[i]))    
    root.update()
    
def Generate():
    global data
    minVal = int(minEntry.get())
    maxVal = int(maxEntry.get())
    size = int(sizeEntry.get())
    
    data = [] #Clears the array
    for _ in range(size):
        data.append(random.randrange(minVal, maxVal+1)) #Generates new data
    
    drawData(data, ['blue' for x in range(len(data))]) #Creates an array of blue rectangles

def StartAlgorithm():
    global data
    if algorithmSelection.get() == "Bubble Sort": 
        bubbleSort(data, drawData, speedSlider.get())
    elif algorithmSelection.get() == "Insertion Sort": 
        insertionSort(data, drawData, speedSlider.get())
    elif algorithmSelection.get() == "Quick Sort": 
        quickSort(data, 0, len(data)-1, drawData, speedSlider.get())
    elif algorithmSelection.get() == "Merge Sort": 
        mergeSort(data, drawData, speedSlider.get())

    drawData(data, ['red' for x in range(len(data))])
    
# General Layout of frame
frameUI = Frame(root, width=400, height = 400, bg='grey') #Creates UI frame
frameUI.grid(row=0, column=0, padx=5, pady=5) #Draws out the grid while also positioning and padding it.

canvas = Canvas(root, width=600, height=380,bg='white') # Creates canvas
canvas.grid(row=1, column=0, padx=5, pady=5) #Canvas positioning

#UI Layout
#Row[0]
Label(frameUI, text="Algorithm: ", bg='grey').grid(row=0, column=0, padx=5, pady=5, sticky=W) #Algorithm Label
algorithmSelection = ttk.Combobox(frameUI, textvariable=selectedAlg, values=['Bubble Sort', 'Merge Sort', 'Insertion Sort', 'Quick Sort']) # Dropdown  selection
algorithmSelection.grid(row=0, column=1, padx=5, pady=5) #Draws out the menu
algorithmSelection.current(0)

speedSlider = Scale(frameUI, from_=0.1, to=2.0, length=200, digits=2, resolution=0.2, orient=HORIZONTAL, label="Select Speed[s]") #Slider for sort speed
speedSlider.grid(row=0, column=2, padx=5, pady=5) #Draws the slider
Button(frameUI, text='Start', command=StartAlgorithm, bg='red').grid(row=0, column=3, padx=5, pady=5) #Start Button


#Row[1]

sizeEntry = Scale(frameUI, from_=3, to=25, length=150, resolution=1, orient=HORIZONTAL, label="Data Size") #Slider for data size
sizeEntry.grid(row=1, column=0, padx=5, pady=5)


minEntry =Scale(frameUI, from_=0, to=10,  length=150,resolution=1, orient=HORIZONTAL, label="Mininum Value") #Slider for the minimum value
minEntry.grid(row=1, column=1, padx=5, pady=5)


maxEntry = Scale(frameUI, from_=10, to=100, length=200, resolution=1, orient=HORIZONTAL, label="Maximum Value") #Slider for maximum value
maxEntry.grid(row=1, column=2, padx=5, pady=5)

Button(frameUI, text='Generate', command=Generate, bg='white').grid(row=1, column=3, padx=5, pady=5) #Generates the array of rectangles that will be sorted

root.mainloop()