
class Node(object):
    
    def __init__(self,d):
        self.data = d;
        self.link = None;

    def SetData(self,d):
        self.data = d;
        
    def GetData(self):
        return self.data;
    
    def SetLink(self,l=None):
        self.link = l;      
        
    def GetLink(self):
        return self.link;

class LinkList(Node):

    def __init__(self):
        self.root = None;
        self.size = 0;

    def GetSize(self):
        return self.size;

    def SetRoot(self, r):
        self.root = r;

    def GetRoot(self):
        return self.root;

    def AddAtBeg(self,d):
        NewNode = Node(d);
        if(self.root == None):
            self.root = NewNode;
            self.size+=1;
            return;
        NewNode.SetLink(self.root);
        self.root = NewNode;
        self.size+=1;

    def AddAtLast(self,d):
        NewNode = Node(d);
        if(self.root == None):
            self.root = NewNode;
            NewNode.SetLink(None);
            self.size+=1;
            return;
        TempNode = self.root;
        while (TempNode.GetLink() != None):
            TempNode = TempNode.GetLink();
        TempNode.SetLink(NewNode);
        self.size+=1;
        
    def AddAtMid(self,d,p):
        if (p == 0):
            AddAtBeg(d);
        elif (p == 1):
            NewNode = Node(d);
            NewNode.SetLink(self.root.GetLink());
            self.root.SetLink(NewNode);
            self.size += 1;
        elif (p == self.size):
            AddAtLast(d);
        elif (p<0 or p>self.size):
            print("Invalid position to enter the new node !!!");
        else:
            TempNode1 = self.root;
            TempNode2 = TempNode1.GetLink()
            for i in range(1,p):
                TempNode1 = TempNode1.GetLink();
                TempNode2 = TempNode1.GetLink();
            NewNode = Node(d);
            NewNode.SetLink(TempNode2);
            TempNode1.SetLink(NewNode);
            self.size += 1;

    def DelAtBeg(self):
        if(self.root == None):
            print("The Link List is empty !!! \n");
            return;
        self.root = self.root.GetLink();
        self.size -= 1;

    def DelAtMid(self,p):
        if(self.root == None):
            print("The Link List is empty !!! \n");
        elif(p == 1):
            self.root = self.root.GetLink();
            self.size -= 1;
        elif(p == self.size):
            TempNode = self.root;
            while(TempNode.GetLink(TempNode.GetLink()) != None):
                TempNode = TempNode.GetLink();
            TempNode.SetLink(None);
            self.size -= 1;
        elif( p<=0 or p>self.size):
            print("Invalid position number !!! \n");
        else:
            TempNode1 = self.root;
            TempNode2 = TempNode1.GetLink();
            for i in range(1,p-1):
                TempNode1 = TempNode1.GetLink();
                TempNode2 = TempNode2.GetLink();
            TempNode1.SetLink(TempNode2.GetLink());
            self.size -= 1;

    def DelAtLast(self):
        if(self.size == 0):
            print("\n The list is empty !!! \n");
        elif(self.size == 1):
            self.root = None;
            self.size -= 1;
        else:
            TempNode = self.root;
            while (TempNode.GetLink().GetLink() != None):
                TempNode = TempNode.GetLink();
            TempNode.SetLink(None);
            self.size -= 1;

    def DisplayList(self):
        if (self.size == 0 and self.root == None):
            print("\n" + "The List is empty !!!" + "\n");
            return;
        TempNode = self.root;
        while (TempNode != None):
            print(str(TempNode.GetData()) + '\n');
            TempNode = TempNode.GetLink();

    def PrintList(self):
        if(self.root == None):
            print("The list is empty !!!\n");
        else:
            temp = self.root;
            #print("The List is as follows: ");
            while(temp != None):
                if(temp.GetLink() != None):
                    print(str(temp.GetData()) + " -> ", end="");
                else:
                    print(str(temp.GetData()));
                temp = temp.GetLink();

    def NReverseList(self):
        if (self.root == None or self.size == 1):
            print("The List is empty or has only one element. So, It can be reversed !!! ");
            return;
        if (self.size == 2):
            temp = self.root;
            self.root = self.root.GetLink();
            self.root.SetLink(temp);
            temp.SetLink(None);
            return;
        TempNode1 = self.root;
        TempNode2 = TempNode1.GetLink();
        TempNode3 = TempNode2.GetLink();
        TempNode1.SetLink(None);
        while(TempNode3 != None ):
            TempNode2.SetLink(TempNode1);
            TempNode1 = TempNode2;
            TempNode2 = TempNode3;
            TempNode3 = TempNode3.GetLink();
        TempNode2.SetLink(TempNode1);
        self.root = TempNode2;

    def RReverseList(self,TempNode1,TempNode2,TempNode3):
        if ( self.size == 1 or self.size == 0):
            print("The List is empty or has only one element. So, It can be reversed !!! ");
            return;
        if (self.size == 2):
            temp = self.root;
            self.root = self.root.GetLink();
            self.root.SetLink(temp);
            temp.SetLink(None);
            return;
        if (self.root != None):
            TempNode1 = self.root;
            TempNode2 = TempNode1.GetLink();
            TempNode3 = TempNode2.GetLink();
            TempNode1.SetLink(None);
            self.root = None;
            self.RReverseList(TempNode1,TempNode2,TempNode3);
            return;
        if (TempNode3 != None):
            TempNode2.SetLink(TempNode1);
            TempNode1 = TempNode2;
            TempNode2 = TempNode3;
            TempNode3 = TempNode3.GetLink();
            self.RReverseList(TempNode1,TempNode2,TempNode3);
            return;
        if (TempNode3 == None):
            TempNode2.SetLink(TempNode1);
            self.root = TempNode2;
            return;
    
def Main():
    List1 = LinkList();
    List1.AddAtBeg(33);
    List1.AddAtBeg(22);
    List1.AddAtBeg(11);
    List1.AddAtLast(44);
    List1.AddAtLast(66);
    List1.AddAtMid(55,4);
    print("The size of the List is:  " + str(List1.GetSize()));
    print("The List before Reverse is:" + '\n'); List1.PrintList();
    a = None; b = None; c = None;
    List1.RReverseList(a,b,c);
    print("The size of the List is:  " + str(List1.GetSize()) + '\n');
    print("The List after Reverse is:" + '\n'); List1.PrintList();

if __name__ == "__main__":
    Main();


