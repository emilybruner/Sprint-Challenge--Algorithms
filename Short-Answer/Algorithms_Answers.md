#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a O(n) - this is because the while loop will only run once per each instance of n


b) O(nlogn) - There are nested for loops, the first one will run at O(n), but the second one will run half as many times so instead of being O(n**2) it is O(nlogn)


c) O(n) - the for loop runs one time per instance of n 

## Exercise II

I would use a binary search method by first dropping an egg off of the middle floor. This will allow me to eliminate half of the floors. If the egg does not break when dropped off the midpoint, I can eliminate searching the floors below it, and move on to the middle floor of the top half of the floors, repeating until f is found. If the egg does break when dropped off the initial middle floor, then I would focus only on the floors below f and repeat with creating a new midpoint and eliminating until f is found. 

The runtime complexity of this method would be O(log(n))
