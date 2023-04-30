from rich.table import Table
from rich.console import Console
from rich.box import Box
import numpy as np

console = Console()

# Create the first matrix
m1_r = int(input("Rows of Matrix 1:"))
m1_c = int(input("Columns of Matrix 1:"))

matrix1 = np.zeros((m1_r, m1_c))

for i in range(m1_r):
    for j in range(m1_c):
        matrix1[i][j] = float(input(f"Enter value for [{i}][{j}]: "))

# Define the result variable
result = None

# Create the second matrix if desired
SM = input("Create Second Matrix? (y/n):")

if SM == "y":
    m2_r = int(input("Rows of Matrix 2:"))
    m2_c = int(input("Columns of Matrix 2:"))

    matrix2 = np.zeros((m2_r, m2_c))

    for i in range(m2_r):
        for j in range(m2_c):
            matrix2[i][j] = float(input(f"Enter value for [{i}][{j}]: "))

    # Display the two matrices
    console.print("\nMatrix 1:")
    table1 = Table(show_header=False, show_lines=True)
    for i in range(len(matrix1)):
        table1.add_row(*[str(matrix1[i][j]) for j in range(len(matrix1[i]))])
    console.print(table1)

    console.print("\nMatrix 2:")
    table2 = Table(show_header=False, show_lines=True)
    for i in range(len(matrix2)):
        table2.add_row(*[str(matrix2[i][j]) for j in range(len(matrix2[i]))])
    console.print(table2)

    # Allow for matrix operations
    op = input("Enter operation (+,-,*,det,inv,trans,scalar_mult) to perform on matrices: ")

    if op == "+":
        result = matrix1 + matrix2
    elif op == "-":
        result = matrix1 - matrix2
    #elif op == "*":
        #result = np.dot(matrix1, matrix2)



    elif op == "*":
        if matrix1.shape[1] == matrix2.shape[0]:
            matrix3 = np.dot(matrix1, matrix2)
            result = matrix3
        else:
            console.print("[bold red]Error: [/bold red]Cannot perform matrix multiplication. Invalid dimensions.")

    if result is not None:
        console.print("\nResult:")
        table3 = Table(show_header=False, show_lines=True)
        if op == "det":
            table3.add_row(str(result))
        else:
            for i in range(len(result)):
                table3.add_row(*[str(result[i][j]) for j in range(len(result[i]))])
        console.print(table3)

else:
    # Display the first matrix if second matrix is not created
    console.print("\nMatrix 1:")
    table1 = Table(show_header=False, show_lines=True)
    for i in range(len(matrix1)):
        table1.add_row(*[str(matrix1[i][j]) for j in range(len(matrix1[i]))])
    console.print(table1)

# Allow for single matrix operations
op = input("Enter operation (inv,trans,det,scalar_mult) to perform on matrix 1: ")

if op == "inv":
    result = np.linalg.inv(matrix1)
elif op == "trans":
    result = np.transpose(matrix1)
elif op == "det":
    result = np.linalg.det(matrix1)
elif op == "scalar_mult":
    scalar = float(input("Enter scalar value: "))
    result = scalar * matrix1

if result is not None:
    console.print("\nResult:")
    table3 = Table(show_header=False, show_lines=True)
    if op == "det":
        table3.add_row(str(result))
    else:
        for i in range(len(result)):
            table3.add_row(*[str(result[i][j]) for j in range(len(result[i]))])
    console.print(table3)
