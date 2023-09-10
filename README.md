# GPA_Calculator_and_Sorting_Grades_from_CSV
This project is a program that reads grades of different individuals from a CSV file and performs various calculations on the grades. The program implements the following tasks:

1. Calculate and store the average grade for each individual along with their names. The output is saved in the same order as the input file.

2. Calculate and store the average grades in ascending order along with the names of the individuals. It's important to note that the program handles the order of the grades correctly, even when using dictionaries.

3. Identify and store the top three average grades along with the names of the individuals.

4. Save the bottom three average grades without including the names of the individuals.

5. Calculate the average of all the average grades and store it.

The program successfully reads the CSV file, performs the necessary calculations, and saves the results in an output file. The code has been thoroughly tested and is ready for use.

Please refer to the code in the repository for detailed implementation and further information.
### Examples

#### Input Example
```
mandana,5,7,3,15
hamid,3,9,4,20,9,1,8,16,0,5,2,4,7,2,1
sina,19,10,19,6,8,14,3
sara,0,5,20,14
soheila,13,2,5,1,3,10,12,4,13,17,7,7
ali,1,9
sarvin,0,16,16,13,19,2,17,8
```
#### Output Example - Task 1
```
mandana,7.5
hamid,6.066666666666666
sina,11.285714285714286
sara,9.75
soheila,7.833333333333333
ali,5.0
sarvin,11.375
```
#### Output Example - Task 2
```
ali,5.0
hamid,6.066666666666666
mandana,7.5
soheila,7.833333333333333
sara,9.75
sina,11.285714285714286
sarvin,11.375
```
#### Output Example - Task 3
```
sarvin,11.375
sina,11.285714285714286
sara,9.75
```
#### Output Example - Task 4
```
5.0
6.066666666666666
7.5
```
#### Output Example - Task 5
```
8.401530612244898
```
Note: In each task, if multiple individuals have the same average, the output order should be alphabetical. For example:
```
hossein 16.5
mona 16.5
```
