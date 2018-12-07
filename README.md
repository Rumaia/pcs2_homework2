# pcs2_homework2
## QUICKSORT AND MERGESORT REPORT:

Here I am writing a report on quicksort and mergesort functions and about their speed in sorting a given random list. The goal of my code is to make a comparision between these two function and understand which one is better for the provided random lists.

## IN CASE OF QUICKSORT:
In the function quicksort I have one element fixed, called pivot, and I am sorting all the coming elements according to the pivot and these elements are then put in a new list.

## IN CASE OF MERGESORT:
In the function mergesort the list is divided into two halves. I am calling the left part of the list, left; and the right part of the list, right. Then the two halves are sorted and put back together. Thus it modifies the original list, and sorts it. If you try to call the original list that was provided, you can see that it returns the sorted list. So the original one is lost.

## TIMER:
After writing the functions, to compare them I have wrote a Timer function that is measuring the time needed for each iteration. In the Timer I have used a setup module which is a simple way to time small Python codes. Then I have imported my codes of quicksort and mergesort and then using different samples that have different ranges, I have measured the time. I have also printed these values of time, because it makes easy to plot the graph.

## GRAPH:
At the end there is a small piece of code explaining how the graph has been created. You can see from the graph I uploaded that, in the X-axis the variables of time have been plotted and in the Y-axis the measure of time it took to perform quicksort and mergesort on the random lists. In the graph the blue line is for the function quicksort and the red line is for mergesort. At the beginning major differences of time between the two functions is not visible. But further quicksort does it's job way faster than mergesort. 

## DECISION:
Mergesort is slower because it needs extra memory to perform sorting, while quicksort is an in-place sorting algorithm. This means that quicksort doesn't need extra space for performing sorting. But there are some cases for which mergesort is better than quicksort and one of those cases is big data processing. Mergesort is a stable sort, unlike quicksort. With mergesort it is easy to operate with linked lists and very large lists. 

So we can state that between the two functions quicksort is faster and better.


