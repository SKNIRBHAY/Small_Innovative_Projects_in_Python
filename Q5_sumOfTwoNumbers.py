from math import pow
from LinkedList1 import linkedList

def addNumbers(List1, List2):
    zeroCount1 = List1.getSize()-1; zeroCount2 = List2.getSize()-1;
    list1Temp = List1.getRoot(); list2Temp = List2.getRoot();
    #print(list1Temp.getLink());
    #print(list2Temp.getLink());
    List3 = linkedList();
    result = 0;

    while ((list1Temp != None) and (list2Temp != None)):
        temp1 = list1Temp.getData(); temp2 = list2Temp.getData();
        temp1 = temp1 * pow(10,zeroCount1); temp2 = temp2 * pow(10,zeroCount2);
        result += temp1 + temp2;
        list1Temp = list1Temp.getLink(); list2Temp = list2Temp.getLink();
        #print("count1 = ", int(zeroCount1));
        #print("count2 = ", int(zeroCount2));
        zeroCount1 -= 1; zeroCount2 -= 1;
        #print("result = ", int(result));

    if(zeroCount1 > zeroCount2):
        listTemp = list1Temp;
        zeroCount = zeroCount1;
    else:
        listTemp = list2Temp;
        zeroCount = zeroCount2;

    while (listTemp != None):
        result += listTemp.getData() * pow(10,zeroCount);
        listTemp = listTemp.getLink();
        zeroCount -= 1;
        if(zeroCount < 0):
            break;
        #print("result = ", int(result));
    #print("Sum = ", int(result));
    n = int(result);
    while(n != 0):
        nodeData = int(n % 10);
        List3.addAtBeg(nodeData);
        n = n//10;
    return List3;

def main():
    List1 = linkedList();
    List1.addAtEnd(7);
    List1.addAtEnd(2);
    List1.addAtEnd(4);
    List1.addAtEnd(3);
    List1.printList();
    List2 = linkedList();
    List2.addAtEnd(5);
    List2.addAtEnd(6);
    List2.addAtEnd(4);
    List2.printList();
    List3 = addNumbers(List1, List2);
    #print("Result: ", end = "")
    List3.printList();
    #print("Size of the List: " + str(List1.getSize()));
    #List1.delAtMid1();
    #List1.printList();
    #List1.rReverseList();
    #List1.printList();

if __name__ == "__main__":
    main();
