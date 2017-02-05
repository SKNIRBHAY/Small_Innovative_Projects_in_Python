from LinkedList import LinkList

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
    L1.AddAtLast(77);
    print("Before: ");
    L1.PrintList();
    RemoveDuplicatesFromLL(L1);
    print("After: ");
    L1.PrintList();

def RemoveDuplicatesFromLL(L1):
    if(L1.GetRoot() == None or L1.GetRoot().GetLink() == None):
        return;
    temp1 = L1.GetRoot();
    #print("Sample1: ", str(temp1.GetData()));
    while temp1.GetLink() != None:
        print(temp1.GetData());
        temp3 = temp1;
        temp2 = temp1.GetLink()
        while temp2 != None:
            if(temp1.GetData() == temp2.GetData()):
                temp3.SetLink(temp2.GetLink());
            temp3 = temp3.GetLink();
            temp2 = temp2.GetLink();
        temp1 = temp1.GetLink();
        if(temp1 == None):
            break;

if __name__ == '__main__':
    main();
