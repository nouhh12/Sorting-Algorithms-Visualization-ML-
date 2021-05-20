
                            Sorting Algorithms Visualization
Description
	
   Six sorting algorithms are compared in their running times used to sort randomly generated arrays. The sorting algorithms used here are: Bubble Sort, Insertion Sort, Selection Sort, Merge Sort, Heap Sort and Quick Sort. These arrays are of sizes 10, 100, 1000, 10000 and 100000. After each algorithm sorts all the randomly generated arrays, the running time it used for each array size will be stored to be finally plotted on a graph that show the difference in runtime between sorting algorithms of different time complexities. Here 3 sorting algorithms of time complexity O(n^2) are used, those being: Bubble Sort, Insertion Sort and Selection Sort. While the other 3 sorting algorithms are of time complexity O (n log n), those being: Merge Sort, Heap Sort and Quick Sort.
	
   Machine learning technique of polynomial regression was used to predict the runtime of Insertion Sort/ Selection Sort/ Bubble Sort when it comes to array sizes of 10000 and 10000. These would take an extremely long time to be sorted due to the huge array size combined with time complexity of O(n^2) of those 3 sorting algorithms. The library "scikit-learn" is used for this part of machine learning.

   Algorithms are visualized in action to get an idea of how each algorithms sorts out a random array. It is visualized with the use of multiple libraries such as "Tkinter" for the GUI as well as "Numpy" and "Pandas" working on the back.

 
