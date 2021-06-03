# Matrix-Multiplication-
Matrix Multiplication with given restriction in Python and Matlab

## Functions
Implement a matrix-matrix-product function called matrixmultiply that takes as arguments
matrices A and B and returns the product C = A*B. Your implementation should directly
implement the triply-nested for-loop algorithm. The following notes
apply:

- It is not necessary for the matrices to be square
- Your function should identify and report erroneous problem instances
- You are free to add any function arguments required for your language of choice (e.g.,
matrix sizes)
- You can use derived types or classes to represent matrices but will have to clearly explain
what you’re using and where it comes from (if you’re using a third-party library)

## Main program
Reads the sizes of matrices A and B from the command line (or other user input),
allocates and fills A and B as random matrices, and evaluates the product C = A*B

- Evaluates the computational time of the matrix product (excluding other operations)
and clearly displays the elapsed time
- Verifies the matrix product against a built-in/library routine (think carefully about
how can you succintly show that the result is correct)
- Evaluates the computational time of the built-in/library routine and clearly displays
the elapsed time

## Result and discussion 
1. Plot time versus problem size for the two methods

<img width="472" alt="Screen Shot 2021-06-03 at 3 00 44 PM" src="https://user-images.githubusercontent.com/73355680/120704641-769e3280-c47c-11eb-9128-0a6e2e16a91a.png">


<img width="478" alt="Screen Shot 2021-06-03 at 2 55 17 PM" src="https://user-images.githubusercontent.com/73355680/120704027-aef14100-c47b-11eb-927d-6b7d4dab503f.png">

2. Derive	the	order-of-growth	of	your	matrix	multiplication	algorithm.	Justify	why	or why	not	the	results	you	measured	agree	with	your	assessment	of	the	order-ofgrowth.	You	can do	this	on	just	the	square	matrix-matrix	multiplication	for	simplicity	

- The	order	of	growth of	matrix	multiplication	algorithm is	O(nˆ3).	My	measurement	is	
agree	with	this	assessment.	Since	the	algorithms I	used has	3	outer	loop	=>	first	loop	
will	run	N	times	from	i	=	0	to	i =	N-1,	second and	third	loop	also	run	N	times	
independently	=> N * N * N =	Nˆ3 times	loop	will	be	executed =>	time complexity	to	be	
O(Nˆ3)
