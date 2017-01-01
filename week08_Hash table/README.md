## The 2-sum problem

Given an unsorted array A of n integers and an integer x, find 
if there are two numbers a and b in A with a+b = x.

A hash table H is used to store all elements in A. 
For any element a in A, if (x-a) exists in H, then the two numbers 
are found. 

Default value of x is 0, you can specify x through command line argument.
