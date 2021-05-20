from tkinter import *
from tkinter import ttk
from matplotlib import pyplot as plt
import sys
import time
from datetime import datetime
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures

#Increasing the recursion limit otherwise maximum depth would be reached when sorting larger arrays
sys.setrecursionlimit(10**8)

#Generating random numpy arrays to be sorted
arr10=np.random.randint(100,size=(10))
arr100=np.random.randint(100,size=(100))
arr1000=np.random.randint(100,size=(1000))
arr10k=np.random.randint(100,size=(10000))
arr100k=np.random.randint(100,size=(100000))

visualizationFlag=False
iterations=0
data = []

#Used to draw the bar chart used in visualizing the sorting algorithms in action
def drawData(data,colorArray):
    canvas.delete("all")
    canvas_width = 500
    canvas_height = 400
    x_width = canvas_width / (len(data) + 1)
    offset = 4
    spacing = 2
    normalizedData = [i / max(data) for i in data]

    for i, height in enumerate(normalizedData):
        x0 = i * x_width + offset + spacing
        y0 = canvas_height - height * 390
        x1 = (i + 1) * x_width + offset
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])

    window.update_idletasks()

#Next 3 functions are for the Merge Sort
def merge(start, mid, end,data, drawData):
    p = start
    q = mid + 1
    list1 = []

    for i in range(start, end+1):
        if p > mid:
            list1.append(data[q])
            q+=1
        elif q > end:
            list1.append(data[p])
            p+=1
        elif data[p] < data[q]:
            list1.append(data[p])
            p+=1
        else:
            list1.append(data[q])
            q+=1

    for p in range(len(list1)):
        data[start] = list1[p]
        start += 1  
 
def mergeSort(start,end,data,drawData):
    global visualizationFlag
    global iterations
    if start<end:
        middle = int((start+end)/2)
        mergeSort(start,middle,data,drawData)
        mergeSort(middle+1,end,data,drawData)
        merge(start,middle,end,data,drawData)
        if visualizationFlag==True:
            iterations+=1
            update_iterations()
            drawData(data, ["#9563ff" if  x>(middle*2-len(data)) and x < middle else "#f3f700" if x == middle 
                                    else "#0066ec" if x > middle and x<=len(data)else "#b2c9ff" for x in range(len(data))])
            time.sleep(0.05)
    if visualizationFlag==True:
        iterations+=1
        update_iterations()
        drawData(data, ["#0063ab" for x in range(len(data))])

def mergeSorttimer(list1,drawData):
  global visualizationFlag
  start=datetime.now()
  list1copy=np.copy(list1)
  list1copy=mergeSort(0,len(list1copy)-1,list1copy,drawData)
  timetaken=datetime.now()-start
  timetaken=timetaken.total_seconds()
  visualizationFlag=False
  return timetaken,list1copy

#Next 3 functions are for the Quick Sort
def partition(start,end,data,drawData):
  global visualizationFlag
  global iterations
  i=start-1
  pivot=data[end]
  for j in range(start,end):
    if data[j]<=pivot:
      i+=1
      (data[j],data[i])=(data[i],data[j])
      if visualizationFlag==True:
        iterations+=1
        update_iterations()
        drawData(data, ["#00d47a" if x == j or x == j+1 else "#0063ab" for x in range(len(data))] )
        time.sleep(0.005)
  finalPivotIndex=i+1
  (data[finalPivotIndex],data[end])=(data[end],data[finalPivotIndex])
  if visualizationFlag==True:
    iterations+=1
    update_iterations()
    drawData(data, ["#00d47a" if x == j or x == j+1 else "#0063ab" for x in range(len(data))] )
    time.sleep(0.005)
  return finalPivotIndex

def quickSort(start,end,data,drawData):
  if start<end:
    p=partition(start,end,data,drawData)
    quickSort(start,p-1,data,drawData)
    quickSort(p+1,end,data,drawData)
  return data,drawData

def quickSorttimer(list1,drawData):
  global visualizationFlag
  start=datetime.now()
  list1copy=np.copy(list1)
  list1copy=quickSort(0,len(list1copy)-1,list1copy,drawData)
  timetaken=datetime.now()-start
  timetaken=timetaken.total_seconds()
  visualizationFlag=False
  return timetaken,list1copy

#Next 2 functions are for the Heap Sort
def heapify(list1,end,i,drawData):
  global visualizationFlag
  global iterations
  largest=i
  l=2*i+1
  r=2*i+2
  if l<end and list1[largest]<list1[l]:
    largest=l
  if r<end and list1[largest]<list1[r]:
    largest=r
  if largest!=i:
    (list1[i],list1[largest])=(list1[largest],list1[i])
    if visualizationFlag==True:
        iterations+=1
        update_iterations()
        drawData(data, ["#00d47a" if x == i or x == largest else "#0063ab" for x in range(len(data))] )
        time.sleep(0.05)
    heapify(list1,end,largest,drawData)

def heapSort(data,drawData):
  start=datetime.now()
  list1copy=np.copy(data)
  global iterations
  global visualizationFlag
  for i in range(len(list1copy//2) - 1,-1,-1):
    heapify(list1copy,len(list1copy),i,drawData)
  for j in range(len(list1copy)-1,0,-1):
    (list1copy[j],list1copy[0])=(list1copy[0],list1copy[j])
    if visualizationFlag==True:
        iterations+=1
        update_iterations()
        drawData(list1copy, ["#00d47a" if x == j or x == j+1 else "#0063ab" for x in range(len(list1copy))] )
        time.sleep(0.05)
    heapify(list1copy,j,0,drawData)
  if visualizationFlag==True:
    iterations+=1
    update_iterations()
    drawData(list1copy, ["#0063ab" for x in range(len(list1copy))])
  timetaken=datetime.now()-start
  timetaken=timetaken.total_seconds()
  visualizationFlag=False
  return timetaken,list1copy


def insertionSort(data,drawData):
    start=datetime.now()
    list1copy=np.copy(data)
    global visualizationFlag
    global iterations
    for i in range(1,len(list1copy)):
        x=i
        j=i-1
        while list1copy[x]<list1copy[j] and j>=0:
            (list1copy[x],list1copy[j])=(list1copy[j],list1copy[x])
            x-=1
            j-=1
            if visualizationFlag==True:
                iterations+=1
                update_iterations()
                drawData(list1copy, ["#00d47a" if z == j or z == j+1 else "#0063ab" for z in range(len(list1copy))] )
                time.sleep(0.005)
    if visualizationFlag==True:
        drawData(list1copy, ["#0063ab" for z in range(len(list1copy))])
    timetaken=datetime.now()-start
    timetaken=timetaken.total_seconds()
    visualizationFlag=False
    return timetaken,list1copy

def selectionSort(data,drawData):
    start=datetime.now()
    list1copy=np.copy(data)
    global visualizationFlag
    global iterations
    for i in range(len(list1copy)):
        minIndex=i
        for j in range(i+1,len(list1copy)):
            if list1copy[j]<list1copy[minIndex]:
                minIndex=j
        (list1copy[i],list1copy[minIndex])=(list1copy[minIndex],list1copy[i])
        if visualizationFlag==True:
            iterations+=1
            update_iterations()
            drawData(list1copy, ["#00d47a" if x == j or x == j+1 else "#0063ab" for x in range(len(list1copy))] )
            time.sleep(0.005)
    if visualizationFlag==True:
        drawData(list1copy, ["#0063ab" for x in range(len(list1copy))])
    timetaken=datetime.now()-start
    timetaken=timetaken.total_seconds()
    visualizationFlag=False
    return timetaken,list1copy

def bubbleSort(data,drawData):
    start=datetime.now()
    list1copy=np.copy(data)
    global visualizationFlag
    global iterations
    for i in range(len(list1copy)-1):
        for j in range(len(list1copy)-1):
            if(list1copy[j]>list1copy[j+1]):
                (list1copy[j],list1copy[j+1])=(list1copy[j+1],list1copy[j])
                if visualizationFlag==True:
                    iterations+=1
                    update_iterations()
                    drawData(list1copy, ["#00d47a" if x == j or x == j+1 else "#0063ab" for x in range(len(list1copy))] )
                    time.sleep(0.005)
    if visualizationFlag==True:
        drawData(list1copy, ["#0063ab" for x in range(len(list1copy))])
    timetaken=datetime.now()-start
    timetaken=timetaken.total_seconds()
    visualizationFlag=False
    return timetaken,list1copy


###PLOTTING TIME COMPLEXITY STARTS FROM HERE###

#Arrays to store the time taken by each sorting algorithm 
bubbleSorttimes=[bubbleSort(arr10,drawData)[0],bubbleSort(arr100,drawData)[0],bubbleSort(arr1000,drawData)[0]]
insertionSorttimes=[insertionSort(arr10,drawData)[0],insertionSort(arr100,drawData)[0],insertionSort(arr1000,drawData)[0]]
selectionSorttimes=[selectionSort(arr10,drawData)[0],selectionSort(arr100,drawData)[0],selectionSort(arr1000,drawData)[0]]
mergeSorttimes=[mergeSorttimer(arr10,drawData)[0],mergeSorttimer(arr100,drawData)[0],mergeSorttimer(arr1000,drawData)[0],mergeSorttimer(arr10k,drawData)[0],mergeSorttimer(arr100k,drawData)[0]]
heapSorttimes=[heapSort(arr10,drawData)[0],heapSort(arr100,drawData)[0],heapSort(arr1000,drawData)[0],heapSort(arr10k,drawData)[0],heapSort(arr100k,drawData)[0]]
quickSorttimes=[quickSorttimer(arr10,drawData)[0],quickSorttimer(arr100,drawData)[0],quickSorttimer(arr1000,drawData)[0],quickSorttimer(arr10k,drawData)[0],quickSorttimer(arr100k,drawData)[0]]

arraySizes=[10,100,1000]

#Bubble Sort Polynomial Regression for 10k and 100k arrays
df1=pd.DataFrame(bubbleSorttimes,columns=['bs times'])
df1_1=pd.DataFrame(arraySizes,columns=['Array sizes'])
reg1=make_pipeline(PolynomialFeatures(2),LinearRegression())
reg1.fit(df1_1,df1)
bubbleSorttimes.extend([reg1.predict([[10000]]),reg1.predict([[100000]])])

#Selection Sort Polynomial Regression for 10k and 100k arrays
df2=pd.DataFrame(selectionSorttimes,columns=['ss times'])
df2_1=pd.DataFrame(arraySizes,columns=['Array sizes'])
reg2=make_pipeline(PolynomialFeatures(2),LinearRegression())
reg2.fit(df2_1,df2)
selectionSorttimes.extend([reg2.predict([[10000]]),reg2.predict([[100000]])])

#Insertion Sort Polynomial Regression for 10k and 100k arrays
df3=pd.DataFrame(insertionSorttimes,columns=['is times'])
df3_1=pd.DataFrame(arraySizes,columns=['Array sizes'])
reg3=make_pipeline(PolynomialFeatures(2),LinearRegression())
reg3.fit(df3_1,df3)
insertionSorttimes.extend([reg3.predict([[10000]]),reg3.predict([[100000]])])

arraySizes.extend([10000,100000])

plt.plot(arraySizes,selectionSorttimes)
plt.plot(arraySizes,insertionSorttimes)
plt.plot(arraySizes,mergeSorttimes)
plt.plot(arraySizes,bubbleSorttimes)
plt.plot(arraySizes,heapSorttimes)
plt.plot(arraySizes,quickSorttimes)
plt.legend(["Selection Sort","Insertion Sort","Merge Sort","Bubble Sort","Heap Sort","Quick Sort"])
plt.xlabel("Number of Array Terms")
plt.ylabel("Time/sec")
plt.title("Sorting Algorithms Time Complexity")


###GUI STARTS FROM HERE###

window = Tk()
window.title("Sorting Algorithms Visualization")
window.maxsize(1000, 700)
window.config(bg = "#FFFFFF")

UI_frame = Frame(window, width= 900, height=300, bg="#FFFFFF")
UI_frame.grid(row=0, column=0, padx=10, pady=5)

#Used to store the list of algorithms displayed in drop down menu 
algorithm_name = StringVar()
algo_list = ['Bubble Sort', 'Insertion Sort','Selection Sort','Merge Sort','Heap Sort','Quick Sort']


# Dropdown to select sorting algorithm 
l1 = Label(UI_frame, text="Algorithm: ", bg="#C4C5BF")
l1.grid(row=0, column=0, padx=10, pady=5, sticky=W)
algo_menu = ttk.Combobox(UI_frame, textvariable=algorithm_name, values=algo_list,state="readonly")
algo_menu.grid(row=0, column=1, padx=5, pady=5)
algo_menu.current(0)

#Called when selecting an algorithm to visualize
def sort():
    global data
    global iterations
    global visualizationFlag
    visualizationFlag=True
    iterations=0
    if algo_menu.get()=="Bubble Sort":
        bubbleSort(data,drawData)
    if algo_menu.get()=="Insertion Sort":
        insertionSort(data,drawData)
    if algo_menu.get()=="Selection Sort":
        selectionSort(data,drawData)
    if algo_menu.get()=="Merge Sort":
        mergeSort(0,len(data)-1,data,drawData)
    if algo_menu.get()=="Heap Sort":
        heapSort(data,drawData)
    if algo_menu.get()=="Quick Sort":
        quickSort(0,len(data)-1,data,drawData)

def generate():
    global data
    data=np.random.randint(100,size=(50))
    drawData(data, ["#000000" for x in range(len(data))])

# Sort button 
b1 = Button(UI_frame, text="Sort", command=sort, bg="#C4C5BF")
b1.grid(row=2, column=1, padx=5, pady=5,sticky="NSEW")

# Button for generating array 
b3 = Button(UI_frame, text="Generate Array", command=generate, bg="#C4C5BF")
b3.grid(row=2, column=0, padx=5, pady=5,sticky="NSEW")


iterationCount=Label(UI_frame)
iterationCount.grid(row=2,column=3,padx=0,pady=5,sticky=E)

# canvas to draw our array 
canvas = Canvas(window, width=500, height=400, bg="#FFFFFF")
canvas.grid(row=1, column=0, padx=10, pady=5,columnspan=2)

def update_iterations():
    iterationCount.config(text="Iterations: "+str(iterations),
                  font='Times 15')  # change the text of the iteration label according to the current count
    window.after(100, update_iterations) 
window.after(0,update_iterations)

plt.show()
window.mainloop()