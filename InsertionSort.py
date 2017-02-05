
def InsertionSort(A, n):
    for i in range(1,n):
        value = A[i];
        hole = i;
        while((A[hole-1] >= value) and (hole > 0)):
            print(str(A) + "; i = " + str(i) + "; hole = " + str(hole) + "; value = " + str(value));
            A[hole] = A[hole-1];
            hole = hole - 1;
        A[hole] = value;
    print(str(A) + "; i = " + str(i) + "; hole = " + str(hole) + "; value = " + str(value));

def Main():
    A = [10,6,8,2,5,1,9,3];
    n = 8;
    print('Unsorted List: ', A);
    InsertionSort(A, n);
    print('Sorted List: ', A);

if __name__ == "__main__":
    Main();
