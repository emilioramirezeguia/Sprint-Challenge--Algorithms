#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) This snippet runs on linear time O(n). As the size of n increases, we enter the while loop n times. Therefore, it's runtime increases proportionally to the number of inputs n. O(n^3) / O(n^2) = O(n)

b) This snippert runs on logarithmic time O(nlogn). As the size of n increases, the number of computations to break out of the while loop is reduced by halve. It gets to a point where the numbers of inputs doesn't have much effect on the runtime. But we still have to account for the for loop that will increase proportionally to the number of inputs n.

c) A typical recursion function runs on linear time O(n). For every increase in input n, the function has to recurse the same number of times to reach it's base case.

## Exercise II

The only thing we know is that building is n stories tall. We also know that eggs dropped off floor f or higher will get broken. Any eggs thrown below that, won't get broken.

First take the midpoint of the building by diving the number of stores by 2.

Anything below that number is safe to drop eggs from.

This algorithm runs on constant time. No matter how big the number of n is (stores in a building), we will compute exactly 2 operations: taking the midpoint and saving the number of floors safe to throw from in a variable.

It will use a Binary Search Tree.
