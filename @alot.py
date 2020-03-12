import numpy as np

def DoWork(b,a):
    row=0#the row of the matrix that I take
    column=0#the column of the matrix that I take
    ret= np.zeros((np.size(b,0)-2,np.size(b,1)-2))#the matrix that return
    while row<np.size(b,0)-2:
        c=b[row:row+3,column:column+3]#a matrix of 3 on 3 from the matrix b
        ret[row][column]=(np.matmul(a,c)).sum()
        column=column+1
        if column>=(np.size(b,1)-2):
            column=0
            row=row+1
    return ret

def main():
    b=np.random.rand(8,8)
    for i in range (np.size(b,0)):
        for j in range (np.size(b,1)):
            b[i][j]= b[i][j]*5
    while (np.size(b,0)>2):
        a=np.random.rand(3,3)
        for i in range (np.size(a,0)):
            for j in range (np.size(a,1)):
                a[i][j]= a[i][j]*5
        b=DoWork(b,a)
        print("and now")
        print(b)
    
if __name__== "__main__":
  main()