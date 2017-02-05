
def bubbleSort(A,n):
    for i in range(0,n-1):
        flag = 0;
        for j in range(0,n-i-1):
            if(A[j] > A[j+1]):
                temp = A[j];
                A[j] = A[j+1];
                A[j+1] = temp;
                flag = 1;
        if(flag == 0):
            break;
    return;

def Main():
    A = [10,6,8,2,5,1,9,3];
    n = 8;
    print('Unsorted List: ', A);
    bubbleSort(A, n);
    print('Sorted List: ', A);

if __name__ == "__main__":
    Main();
