def lower_triangle(rows):
    for i in range(rows):
        for j in range(i+1):
            print("*",end ="")
        print()

lower_triangle_rows=int(input("Enter the number of rows in the lower triangle :"))
lower_triangle(lower_triangle_rows)

def upper_triangle(rows):
    for i in range(rows):
        for j in range (i+1):
            print(" ",end="")
        for k in range(i,rows):
            print("*",end="")
        print()

upper_triangle_rows = int(input("Enter the number of rows in the upper triangle :"))
upper_triangle(upper_triangle_rows)

def pyramid(rows):
    for i in range(rows):
        for j in range(rows-i-1):
            print(" ",end =" ")
        for k in range(2*i+1):
            print("*",end=" ")
        print()

pyramid_rows=int(input("Enter the number of rows in the pyramid :"))
pyramid(pyramid_rows)






