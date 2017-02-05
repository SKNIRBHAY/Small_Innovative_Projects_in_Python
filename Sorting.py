
def SelectionSort(A, n):
    for i in range(0,n-1):
        imin = i;
        for j in range(i,n):
            if (A[j] < A[imin]):
                imin = j;
        temp = A[i];
        A[i] = A[imin];
        A[imin] = temp;
        print('Sorted List ', i , '  ', A);
    print('Sorted List: ', A);

def BubbleSort(A,n):
    for i in range(0,n):
        for j in range(0,n-i-1):
            if A[j] > A[j+1]:
                temp = A[j];
                A[j] = A[j+1];
                A[j+1] = temp;
    print('Sorted List: ', A);

def InsertionSort(A,n):
    for i in range(0,n):
        value = A[i];
        hole = i;
        while(hole > 0 and (A[hole-1] > value)):
            A[hole] = A[hole-1];
            hole -=1;
        A[hole] = value;
    print('Sorted List: ', A); 

def Main():
    A = [10,6,8,2,5,1,9,3];
    n = 8;
    print('Unsorted List: ', A);
    InsertionSort(A, n);

if __name__ == "__main__":
    Main();
