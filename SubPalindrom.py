from LinkedList import LinkList;

class hashMap(object):

    def __init__(self):
        self.size = 26;
        self.map = [None] * self.size;

    def getHash(self, key):
        totalAscii = 0;
        for i in key:
            totalAscii = totalAscii + ord(i);

        return (totalAscii % 26);

    def add(self, key):
        keyHash = self.getHash(key);

        if((keyHash < 0) or (keyHash > 25)):
            print("wrong hash key value pair");
            return 0;

        if(self.map[keyHash] == None):
            self.map[keyHash] = LinkList();
            self.map[keyHash].AddAtBeg(key);
        else:
            temp1 = self.map[keyHash].GetRoot();
            while(temp1 != None):
                if (temp1.GetData() == key):
                    return 0;
                temp1 = temp1.GetLink();
            self.map[keyHash].AddAtLast(key);
        return 1;

    def get(self, key):
        keyHash = self.getHash(key);
        
        if((keyHash < 0) or (keyHash > 25)):
            print("wrong hash key value pair");
            return 0;

        if(self.map[keyHash] != None):
            temp = self.map[keyHash].GetRoot();
            while temp != None:
                if(temp.GetData() == key):
                    return temp.GetData();
                temp = temp.GetLink();
        else:
            print("Element not found in the hash table !!!");
            return 0;

    def print(self):
        print("--------------The Hash Map--------------");
        index = 0;
        for item in self.map:
            if(item != None):
                print("At index " + str(index) + ": ",end ="");
                item.PrintList();
                #print("\n");
            index += 1;
        print("----------------------------------------");

def makeSubStrings(A):
    H1 = hashMap();
    strlen = len(A);
    answer = 0;
    for i in range(strlen):
        start = 0;
        end = i;
        while (end < strlen):
            pFlag = checkPalindrom(A,start,end);
            if(pFlag == 1):
                data = [];
                for k in range(start,end+1):
                    data.append(A[k]);
                cFlag = H1.add(data);
                if(cFlag == 1):
                    answer += 1;
            start += 1;
            end += 1;
    H1.print();
    print(answer);

def checkPalindrom(A,start,end):
    strlen = len(A);
    while ((start - end <= 1) and (end < strlen) and (start >= 0)):
        if (A[start] != A[end]):
            return 0;
        start += 1;
        end -= 1;
    return 1;

def main():
    A = "ccaabaacc";
    makeSubStrings(A);

if __name__ == "__main__":
    main();
