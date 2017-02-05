from LinkedList import LinkList

def partitionLL(L1, pivotal):
    root = L1.GetRoot();
    temp0 = root;
    temp1 = root;
    length = L1.GetSize();
    count = 1;
    if(root == None or root.GetLink() == None):
        print("The Linked List is empty or there is only one item in the list !!!");
        return;
    temp2 = temp1;
    while(count < length):
        print("Count = ",count);
        print("Temp0 is pointing to: ", temp0.GetData());
        print("Temp1 is pointing to: ", temp1.GetData());
        print("Temp2 is pointing to: ", temp2.GetData());
        L1.PrintList();
        if(temp0.GetData() < pivotal):
            print("In: temp1.GetData() < pivotal");
            temp2.SetLink(temp1.GetLink());
            temp0 = temp1.GetLink();
            if(temp1 != root):
                temp1.SetLink(root);
            root = temp1; # Setting the local root
            L1.SetRoot(temp1); # Setting the actual root of the linked list
        if(temp0.GetData() > pivotal):
            print("In: temp1.GetData() > pivotal");
            #temp2.SetLink(temp1.GetLink());
            temp = temp1;
            while(temp.GetLink() != None):
                temp = temp.GetLink();
            temp.SetLink(temp1);
            if(temp1 == temp2):
                L1.SetRoot(root.GetLink());
                root = root.GetLink();
            else:
                temp2.SetLink(temp1.GetLink());
            temp0 = temp1.GetLink();
            temp1.SetLink(None);
        if(temp0 == root):
            temp1=temp2=temp0;
        else:
            if((count != 1) and (temp1 == temp2 == root)):
                temp1 = temp0;
            else:
                temp1 = temp0;
                temp2 = temp1;
                temp1 = temp1.GetLink();
        count += 1;
        print("---------------------------------------------------------------");

def partitionLL1(L1, pivotal):
    root = L1.GetRoot();
    temp0 = temp1 = temp2 = root;
    length = L1.GetSize();
    count = 1;
    temp = root;
    if(root == None or root.GetLink() == None):
        print("The Linked List is empty or there is only one item in the list !!!");
        return;
    while(temp.GetLink()!= None):
        temp = temp.GetLink();
    #print("-------------------------------------------------------------");
    while(temp0 == temp1 == temp2 == root):
        #print("Count = ",count);
        #print("Temp0 is pointing to: ", temp0.GetData());
        #print("Temp1 is pointing to: ", temp1.GetData());
        #print("Temp2 is pointing to: ", temp2.GetData());
        #L1.PrintList();
        if(temp0.GetData() > pivotal):
            #print("In: temp1.GetData() > pivotal");
            temp.SetLink(temp1);
            temp0 = temp0.GetLink();
            temp1 = temp1.GetLink();
            temp2.SetLink(None);
            temp = temp2;
            temp2 = temp0;
            root = temp0;
            L1.SetRoot(temp0);
        else:
            #print("In: temp1.GetData() < or == pivotal");
            temp0 = temp0.GetLink();
            temp1 = temp1.GetLink();
        count += 1;
        #print("-------------------------------------------------------------");
        if(count > length-1):
            break;
        
    while(count <= length):
        #print("Count = ",count);
        #print("Temp0 is pointing to: ", temp0.GetData());
        #print("Temp1 is pointing to: ", temp1.GetData());
        #print("Temp2 is pointing to: ", temp2.GetData());
        #L1.PrintList();
        if(temp0.GetData() > pivotal):
            #print("In: temp1.GetData() > pivotal");
            temp2.SetLink(temp1.GetLink());
            temp.SetLink(temp1);
            temp0 = temp0.GetLink();
            temp1.SetLink(None);
            temp = temp1;
            temp1 = temp0;
        elif(temp0.GetData() < pivotal):
            #print("In: temp1.GetData() < pivotal");
            temp2.SetLink(temp1.GetLink());
            temp0 = temp0.GetLink();
            temp1.SetLink(root);
            root = temp1;
            L1.SetRoot(temp1);
            temp1 = temp0;
        else:
            #print("In: temp1.GetData() == pivotal");
            temp2 = temp2.GetLink();
            temp0 = temp0.GetLink();
            temp1 = temp1.GetLink();
        count += 1;
        #print("-------------------------------------------------------------");

def main():
    L1 = LinkList();
    L1.AddAtLast(76);
    L1.AddAtLast(56);
    L1.AddAtLast(67);
    L1.AddAtLast(23);
    L1.AddAtLast(90);
    L1.AddAtLast(89);
    L1.AddAtLast(76);
    L1.AddAtLast(24);
    L1.AddAtLast(45);
    L1.AddAtLast(13);
    L1.AddAtLast(98);
    L1.AddAtLast(67);
    L1.AddAtLast(77);
    L1.AddAtLast(26);
    pivotal = int(input("Enter the pivotal Number: "));
    print("Before:");
    L1.PrintList();
    partitionLL1(L1, pivotal);
    print("After:");
    L1.PrintList();

if __name__ == "__main__":
    main();
