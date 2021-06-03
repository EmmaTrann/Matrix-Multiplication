
prompt = "Enter the number of rows for matrix A: ";
rowa = input(prompt); 
prompt = "Enter the number of columns for matrix A: ";
cola = input(prompt);
prompt = "Enter the number of columns for matrix B: ";
colb = input(prompt);

x = randi(10, rowa, cola);
y = randi(10, cola, colb);
[rowx, colx] = size(x);
[rowy, coly] = size(y);
matrixMultiplication = zeros(rowx, coly); 
tic;
for row=1:rowx
    for col=1:coly
        sum=0;
        for k=1:colx
            sum = sum + x(row,k) * y(k,col);
        end 
        matrixMultiplication(row,col) = sum;
    end
end 
toc;
t=toc;
tic;
matrixMultiplicationMatlab = x * y;
toc;
t = toc;
 
different = matrixMultiplicationMatlab - matrixMultiplication; 
if different == 0
    disp("The matrix calculated using for loop is same as the matrix calculate using matlab")
end 
