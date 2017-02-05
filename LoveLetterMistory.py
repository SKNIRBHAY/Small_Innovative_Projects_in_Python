
def MakePalindrom(A):
    strlen = len(A);
    end = strlen - 1;
    start = 0;
    numberOfOperations = 0;
    while((end - start > 0)):
        temp = abs(ord(A[start]) - ord(A[end]));
        numberOfOperations = numberOfOperations + temp;
        start += 1;
        end -= 1;
    print(numberOfOperations);

def main():
    numberOfTests = int(input());
    A = [];
    for i in range(numberOfTests):
        A.append(input());
    for i in A:
        MakePalindrom(i);

if __name__ == "__main__":
    main();
