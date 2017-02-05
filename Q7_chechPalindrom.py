from LinkedList import LinkList;
from Stack import LinkedStack;

def checkPalindrom(L1,S1):
    fast = slow = L1.GetRoot();
    while((fast != None) or (fast.GetLink()!=None)):
        S1.push(slow.GetData());
        slow = slow.GetLink();
        fast = fast.GetLink().GetLink();
        # Following if statment:
        # To adjust for the case where odd nmbr of elements are there in the list.
        # To push the last element of the list unto the stack
        if(fast != None): 
            if(fast.GetLink() == None):
                S1.push(slow.GetData());
        #print("fast = " + str(fast.GetData()) + "; slow = " + str(slow.GetData()));
        # Following if statment:
        # To avoide the condition where fast does not become None and then the while condition is checked
        if((fast == None) or (fast.GetLink() == None)):
            break;
    #S1.PrintStack();
    while(slow != None):
        if(S1.pop() != (slow.GetData())):
            return 0;
        slow = slow.GetLink();
    return 1;

def main():
    L1 = LinkList();
    S1 = LinkedStack();
    L1.AddAtLast(0);
    L1.AddAtLast(1);
    L1.AddAtLast(2);
    L1.AddAtLast(3);
    L1.AddAtLast(4);
    L1.AddAtLast(5);
    L1.AddAtLast(6);
    L1.AddAtLast(7);
    L1.AddAtLast(6);
    L1.AddAtLast(5);
    L1.AddAtLast(4);
    L1.AddAtLast(3);
    L1.AddAtLast(2);
    L1.AddAtLast(1);
    L1.AddAtLast(0);
    
    L1.PrintList();
    if (checkPalindrom(L1,S1)):
        print("The List is palindrom");
    else:
        print("The List is not palindrom");
        
if __name__ == "__main__":
    main();
