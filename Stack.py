
class ArrayStack(object):
    
    def __init__(self):
        self.MAX_SIZE = 10
        self.A = [];
        self.top = -1;

    def push(self,d):
        self.top += 1;
        self.A.append(d);
        return;

    def pop(self):
        if(self.top <= -1):
            print("The stack is empty !!!");
            return;
        temp = self.A[self.top];
        self.top -= 1;
        return temp;

    def IsEmpty(self):
        if(self.top <=-1):
            return true;
        else:
            return false;

    def PrintStack(self):
        if(self.top <= -1):
            print("The Stack is empty !!!");
            return;
        print("The Stack is : ");
        for i in range(self.top,-1,-1):
            print(self.A[i]);

class Node(object):
    def __init__(self,d = 0):
        self.data = d;
        self.link = None;
    def GetData(self):
        return self.data;
    def SetData(self,d):
        self.data = d;
    def GetLink(self):
        return self.link;
    def SetLink(self,l):
        self.link = l;

class LinkedStack(object):
    def __init__(self):
        self.top = -1;
        self.root = None
        self.size = 0;

    def push(self,d):
        NewNode = Node(d);
        temp = self.root;
        self.root = NewNode;
        NewNode.SetLink(temp);
        return;

    def pop(self):
        if(self.root == None):
            print("The Stack is Empty now !!!");
            return;
        temp = self.root.GetData();
        self.root = self.root.GetLink();
        return temp;

    def IsEmpty(self):
        if self.root == None:
            print("The Stack is empty !!!");
            return true;
        else:
            print("The Statck is not empty !!!");
            return false;
        
    def PrintStack(self):
        if(self.root == None):
           print("The Stack is empty !!!");
           return;
        temp = self.root;
        print("The Stack is:  ");
        while temp != None:
            print(temp.GetData());
            temp = temp.GetLink();

def Main():
    S1 = LinkedStack();
    S1.push(44);    
    S1.push(33);
    S1.push(22);
    S1.push(11);
    S1.PrintStack();
    print("First Pop - " + str(S1.pop()));
    print("Second Pop - " + str(S1.pop()));
    print("Thierd Pop - " + str(S1.pop()));
    S1.PrintStack();
    print("Fourth Pop - " + str(S1.pop()));
    S1.PrintStack();

if __name__ == "__main__":
    Main();
    
