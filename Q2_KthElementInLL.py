from LinkedList import LinkList
count = 0;
def main():
    L1 = LinkList();
    L1.AddAtLast(76);
    L1.AddAtLast(56);
    L1.AddAtLast(67);
    L1.AddAtLast(23);
    L1.AddAtLast(90);
    L1.AddAtLast(89);
    L1.AddAtLast(76);
    L1.AddAtLast(23);
    L1.AddAtLast(45);
    L1.AddAtLast(13);
    L1.AddAtLast(98);
    L1.AddAtLast(67);
    L1.AddAtLast(77);

    L1.PrintList();
    k = input("Enter the value of K: ");
    root = L1.GetRoot();
    Ans = KthElementinLL(k,root,L1);
    print("The Kth element in the LL: ", str(Ans));

def KthElementinLL(k,root,L1):
    global count;
    if(int(k) == L1.GetSize()):
        return root.GetData();
    if(int(k) > L1.GetSize() or int(k) <= 0):
        return "Wrong Input";
    if(root == None):
        return 0;
    root = root.GetLink();
    Ans = KthElementinLL(k,root,L1);
    #print("Count = ", count);
    #print("K = ", k);
    if(int(count) == int(k)):
        #print("In If....");
        #print("The Kth element in the LL: ", str(root.GetData()));
        count += 1;
        return root.GetData();
    count += 1;
    return Ans;

    
if __name__ == "__main__":
    main();
