
def selectionSort(A,n):
    for i in range(0,n-1):
        imin = i;
        for j in range(i+1,n):
            if(A[j] < A[imin]):
                imin = j;
        temp = A[imin];
        A[imin] = A[i];
        A[i] = temp;

def Main():
    A = [10,6,8,2,5,1,9,3];
    n = 8;
    print('Unsorted List: ', A);
    selectionSort(A, n);
    print('Sorted List: ', A);

if __name__ == "__main__":
    Main();
