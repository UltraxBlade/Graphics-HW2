"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( M ):
    if len(M)>0:
        maxFound=0
        for r in range(len(M)):
            for c in range(len(M[r])):
                if M[r][c]==0:
                    numspaces=0
                elif M[r][c]<0:
                    numspaces=int(math.log10(abs(M[r][c])))+1
                else:
                    numspaces=int(math.log10(M[r][c]))
                if numspaces>maxFound:
                    maxFound=numspaces
        
        for c in range(len(M[0])):
            for r in range(len(M)):
                if M[r][c]==0:
                    numspaces=0
                elif M[r][c]<0:
                    numspaces=int(math.log10(abs(M[r][c])))+1
                else:
                    numspaces=int(math.log10(M[r][c]))
                if numspaces>maxFound:
                    maxFound=numspaces
                print(M[r][c],end=" "*(maxFound-numspaces+1))
            print()

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i==j:
                matrix[i][j]=1
            else:
                matrix[i][j]=0
    return matrix

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( M1, M2 ):
    M=new_matrix(len(M2[0]),len(M2))
    for c in range(len(M)):
        for r in range(len(M[c])):
            for i in range(len(M1)):
                M[c][r]+=M1[i][r]*M2[c][i]
    for c in range(len(M)):
        for r in range(len(M[c])):
            M2[c][r]=M[c][r]
    return M

def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
