
def QuickSort(A,start, end):
    if (start < end):
        pIndex = Partition(A,start,end);
        QuickSort(A,start, pIndex-1);
        QuickSort(A,pIndex+1,end);
    else:
        return;

def Partition(A,start,end):
    pivot = A[end];
    pIndex = start;
    for i in range(start,end):
        if(A[i] <= pivot):
            temp = A[i];
            A[i] = A[pIndex];
            A[pIndex] = temp;
            pIndex += 1;
    temp = A[end];
    A[end] = A[pIndex];
    A[pIndex] = temp;
    return pIndex;

def Main():
    A = [10,6,8,2,5,1,9,3];
    n = 8;
    print('Unsorted List: ', A);
    QuickSort(A,0,7);
    print('Sorted List: ', A); 

if __name__ == "__main__":
    Main();
