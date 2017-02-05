
class PythonListQueue(object):

    def __init__(self):
        self.A = [];
        self.front = -1;
        self.rear = -1;

    def EnQueue(self,d):
        if(self.front == -1 and self.rear == -1):
            self.front = self.rear = 0
            self.A.append(d);
        else:
            self.rear += 1;
            self.A.append(d);

    def DeQueue(self):
        if(self.front == -1 and self.rear == -1):
            print("The Queue is empty !!!");
        elif(self.front == self.rear):
            temp = self.A[self.front];
            self.front = self.rear = -1;
            return temp;
        else:
            temp = self.A[self.front];
            del self.A[self.front];
            self.rear -= 1;
            return temp;

    def IsEmpty(self):
        if (self.front == -1 and self.rear == -1):
            print("The Queue is empty !!!");
            return 1;
        else:
            print("The Queue is not empty !!!");
            return 0;

    def PrintQueue(self):
        if (self.front == -1 and self.rear == -1):
            print("The Queue is empty !!!");
        else:
            print("Front = " + str(self.front) + "  Rear = " + str(self.rear));
            print (self.A);


class ArrayQueue(object):

    def __init__(self):
        self.A = [0] * 10;
        self.MAX = 10;
        self.front = -1;
        self.rear = -1;

    def EnQueue(self,d):
        if(self.front == -1 and self.rear == -1):
            self.front = self.rear = 0;
            self.A[0]=d;
        elif(self.rear >= (self.MAX-1)):
            print("The Queue is full, cant add an element !!!");            
        else:
            self.rear += 1;
            self.A[self.rear]=d;

    def DeQueue(self):
        if(self.front == -1 and self.rear == -1):
            #print("The Queue is empty !!!");
            return;
        elif(self.front == self.rear):
            temp = self.A[self.front];
            self.front = self.rear = -1;
            return temp;
        else:
            temp = self.A[self.front];
            self.front += 1;
            return temp;

    def IsEmpty(self):
        if (self.front == -1 and self.rear == -1):
            print("The Queue is empty !!!");
            return 1;
        else:
            print("The Queue is not empty !!!");
            return 0;

    def PrintQueue(self):
        if (self.front == -1 and self.rear == -1):
            print("The Queue is empty !!!");
        else:
            print("The Queue is: ");
            print("Front = " + str(self.front) + "  Rear = " + str(self.rear));
            for i in range (self.front,self.rear + 1):
                print(self.A[i]);
        

class CirculerQueue(object):

    def __init__(self):
        self.A = [0] * 10;
        self.MAX = 10;
        self.front = -1;
        self.rear = -1;

    def EnQueue(self,d):
        if(self.front == -1 and self.rear == -1):
            self.front = self.rear = 0;
            self.A[0]=d;
        elif (((self.rear + 1)% self.MAX) == self.front):
            print("The Queue is full, cant add an element !!!");            
        else:
            self.rear = (self.rear + 1)% self.MAX;
            self.A[self.rear]=d;

    def DeQueue(self):
        if(self.front == -1 and self.rear == -1):
            print("The Queue is empty !!!");
        elif(self.front == self.rear):
            temp = self.A[self.front];
            self.front = self.rear = -1;
            return temp;
        else:
            temp = self.A[self.front];
            self.front = (self.front + 1) % self.MAX;
            return temp;

    def IsEmpty(self):
        if (self.front == -1 and self.rear == -1):
            print("The Queue is empty !!!");
            return 1;
        else:
            print("The Queue is not empty !!!");
            return 0;

    def PrintQueue(self):
        if (self.front == -1 and self.rear == -1):
            print("The Queue is empty !!!");
        else:
            print("The Queue is: ");
            print("Front = " + str(self.front) + "  Rear = " + str(self.rear));
            temp = self.front; temp1 = 0;
            while(1):
                print(self.A[temp]); 
                if(temp1 == 1):
                    break;
                if((temp + 1) % self.MAX == self.rear):
                    temp1 += 1;
                temp = (temp + 1) % self.MAX;

class Node(object):
    def __init__(self):
        self.data = 0;
        self.link = None;

    def GetData(self):
        return self.data;
    def SetData(self,d):
        self.data = d;
    def GetLink(self):
        return self.link;
    def SetLink(self,l):
        self.link = l;

class LinkedQueue(object):
    def __init__(self):
        self.front = None;
        self.rear = None;
        self.size = 0;

    def EnQueue(self,d):
        NewNode = Node();
        NewNode.SetData(d);
        if((self.rear == None) and (self.front == None)):
            self.rear = NewNode;
            self.front = NewNode;
            self.size += 1;
        else:
            self.rear.SetLink(NewNode);
            self.rear = NewNode;
            self.size += 1;

    def DeQueue(self):
        if((self.rear == None) and (self.front == None)):
            print("The Queue is empty !!!");
            return;
        elif(self.rear == self.front):
            temp = self.front.GetData();
            self.front = self.rear = None;
            self.size -= 1;
            return temp;
        else:
            temp = self.front.GetData();
            self.front = self.front.GetLink();
            self.size -= 1;
            return temp;

    def PrintQueue(self):
        if ((self.rear == None) and (self.front == None)):
            print ("The Queue is empty !!!");
            return;
        print("The list is: ");
        temp = self.front;
        while(temp != None):
            print(temp.GetData());
            temp = temp.GetLink();

    def IsEmpty(self):
        if((self.rear == None) and (self.front == None)):
            #print("The Queue is Empty !!!");
            return 1;
        else:
            #print("The Queue is not Empty !!!");
            return 0;
           
           
        
                                            
def Main():
    Q1 = LinkedQueue();
    Q1.EnQueue(11);
    Q1.EnQueue(22);
    Q1.EnQueue(33);
    Q1.EnQueue(44);
    Q1.EnQueue(55);
    Q1.EnQueue(66);
    Q1.EnQueue(77);
    Q1.EnQueue(88);
    Q1.EnQueue(99);
    Q1.EnQueue(100);
    Q1.PrintQueue();
    Q1.DeQueue();
    Q1.DeQueue();
    Q1.PrintQueue();
    Q1.EnQueue(111);
    Q1.EnQueue(222);
    Q1.PrintQueue();
    return;

if __name__ == "__main__":
    Main();
            
