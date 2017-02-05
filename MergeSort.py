def sort(A):
    n = len(A);
    if(n<2):
        return;
    mid = n//2;
    left = [None] * mid;
    right = [None] * (n-mid);
    for i in range(0,mid):
        left[i] = A[i];
    for i in range(mid,n):
        right[i-mid] = A[i];
    sort(left);
    sort(right);
    merge(left,right,A);
        
def merge(L,R,A):
    nL = len(L);
    nR = len(R);
    i=j=k=0;
    while((i<nL) and (j<nR)):
        if(L[i]<R[j]):
            A[k] = L[i];
            i+=1;
        else:
            A[k] = R[j];
            j+=1;
        k+=1;
    while(i<nL):
        A[k] = L[i];
        i+=1;
        k+=1;
    while(j<nR):
        A[k] = R[j];
        j+=1;
        k+=1;

def sort1(A):
    n = len(A);
    if(n<2):
        return;
    mid = n//2;
    left = [None]*mid;
    right = [None]*(n-mid);
    for i in range(0,mid):
        left[i] = A[i];
    for i in range(mid,n):
        right[i-mid] = A[i];
    sort1(left);
    sort1(right);
    merge1(left,right,A);

def merge1(L,R,A):
    nL = len(L);
    nR = len(R);
    i=j=k=0
    while((i<nL) and (j<nR)):
        if(L[i]<R[j]):
            A[k] = L[i];
            i += 1;
        else:
            A[k] = R[j];
            j += 1;
        k += 1;
    while(i<nL):
        A[k] = L[i];
        k += 1;
        i += 1;
    while(j<nR):
        A[k] = R[j];
        k += 1;
        j += 1;

def Main():
    A = [10,6,8,2,5,1,9,3];
    n = 8;
    print('Unsorted List: ', A);
    sort1(A);
    print('Sorted List: ', A);

if __name__ == "__main__":
    Main();
