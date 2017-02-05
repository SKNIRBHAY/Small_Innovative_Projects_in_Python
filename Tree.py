from Queue import LinkedQueue
from Queue import Node

class Node(object):
    def __init__(self,d=0):
        self.data = d;
        self.left = None;
        self.right = None;

    def GetData(self):
        return self.data;
    def SetData(self,d):
        self.data = d;
    def GetLeft(self):
        return self.left;
    def SetLeft(self,l):
        self.left = l;
    def GetRight(self):
        return self.right;
    def SetRight(self,r):
        self.right = r;

class Tree(object):
    def __init__(self):
        self.root = None;
        self.size = 0;
    def GetRoot(self):
        return self.root;
    def SetRoot(self,r):
        self.root = r;

    def Insert(self,root,d):
        if (root == None):
            NewNode = Node(d);
            root = NewNode;
            return root;
        elif(d <= root.GetData()):
            root.SetLeft(self.Insert(root.GetLeft(),d));
            return root;
        else:
            root.SetRight(self.Insert(root.GetRight(),d));
            return root;

    def Search(self,root,d):
        if (root == None):
            #print ("Hello 1 !!!");
            return 0;
        elif(root.GetData() == d):
            #print ("Hello 2 !!!");
            return 1;
        elif(d <= root.GetData()):
            #print ("Hello 3 !!!");
            return self.Search(root.GetLeft(),d);
        else:
            #print ("Hello 4 !!!");
            return self.Search(root.GetRight(),d);

    def Min(self):
        temp = self.root;
        while(temp.GetLeft() != None):
            temp = temp.GetLeft();
        return temp.GetData();

    def Max(self):
        temp = self.root;
        while(temp.GetRight() != None):
            temp = temp.GetRight();
        return temp.GetData();

    def FindHeight(self,root):
        if(root == None):
            return -1;
        leftheight = self.FindHeight(root.GetLeft()) ;
        rightheight = self.FindHeight(root.GetRight());
        return max(leftheight,rightheight) + 1;

    def LevelFirst(self,temp,Q1):
        if(temp != None):
            print(str(temp.GetData()));
        if(temp.GetLeft() != None):
           Q1.EnQueue(temp.GetLeft());
        if(temp.GetRight() != None):
           Q1.EnQueue(temp.GetRight());
        if (Q1.IsEmpty() != 1):
            self.LevelFirst(Q1.DeQueue(),Q1);
        else:
            return;

    def Preorder(self,root):
        if(root == None):
            return;
        print(str(root.GetData()));
        self.Preorder(root.GetLeft());
        self.Preorder(root.GetRight());

    def Inorder(self,root):
        if(root == None):
            return;
        self.Inorder(root.GetLeft());
        print(str(root.GetData()));
        self.Inorder(root.GetRight());

    def Postorder(self,root):
        if(root == None):
            return;
        self.Postorder(root.GetLeft());
        self.Postorder(root.GetRight());
        print(str(root.GetData()));

    def IsBST(self,root,p):
        pass;
            
def Main():
    T1 = Tree(); Q1 = LinkedQueue();
    #root = T1.GetRoot();
    T1.SetRoot(T1.Insert(T1.GetRoot(),77));
    T1.SetRoot(T1.Insert(T1.GetRoot(),33));
    T1.SetRoot(T1.Insert(T1.GetRoot(),88));
    T1.SetRoot(T1.Insert(T1.GetRoot(),44));
    T1.SetRoot(T1.Insert(T1.GetRoot(),66));
    T1.SetRoot(T1.Insert(T1.GetRoot(),55));
    T1.SetRoot(T1.Insert(T1.GetRoot(),11));
    T1.SetRoot(T1.Insert(T1.GetRoot(),22));
    
    #print("The Minimum in the tree: " + str(T1.Min()));
    #print("The Maximum in the tree: " + str(T1.Max()));
    #if (T1.Search(T1.GetRoot(),88)):
    #    print("Element found !!!");
    #else:
    #    print("Element not found !!!");
    #print("The height of the tree: " + str(T1.FindHeight(T1.GetRoot())));
    print("The Postorder tree is: ");
    #T1.LevelFirst(T1.GetRoot(),Q1);
    T1.Postorder(T1.GetRoot());
    return;


if __name__ == "__main__":
    Main();
