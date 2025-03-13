# localy_bounded_codes

Code for project in Coding and algorithms for memories course (236379) at the Technion.

This is a python code for calculating the amount of vectors of size n, that are (l,delta) localy bounded. That is, that every window of size l has a weight of at most l/2-delta.
Using the code is done as follows:
1) you enter the n value
2) you enter the l value
3) you enter the delta value
after that, the code will print the desired number.

for example: if n=10, l=10, delta=0
the code will output 638.
If we will solve it mathematically, it is all the vectors of size 10 that have at most 5 ones. So
10nCr0+10nCr1+10nCr2+10nCr3+10nCr4+10nCr5=638 as expected
