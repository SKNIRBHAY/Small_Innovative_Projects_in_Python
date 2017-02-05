from LinkedList import LinkList;

class hashMap(object):

    def __init__(self):
        self.size = 26;
        self.map = [None] * self.size;

    def getHash(self, key):
        if((ord(key) >= 65) and (ord(key) <= 90)):
            return (ord(key) - 65);
        elif((ord(key) >= 97) and (ord(key) <= 122)):
            return (ord(key) - 97);
        else:
            return -1;

    def add(self, key):
        keyHash = self.getHash(key);
        
        if(keyHash != -1):
            keyValue = key;
        else:
            print("wrong hash key value pair");
            return 0;

        if(self.map[keyHash] == None):
            self.map[keyHash] = LinkList();
            self.map[keyHash].AddAtBeg(keyValue);
        else:
            temp = self.map[keyHash].GetRoot();
            while(temp != None):
                if(temp.GetData() == keyValue):
                    return 0;
                temp = temp.GetLink();
            self.map[keyHash].AddAtLast(keyValue);
        return 1;

    def get(self, key):
        keyHash = self.getHash(key);
        
        if(keyHash == -1):
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

    def delete(self, key):
        keyHash = self.getHash(key);

        if(keyHash == -1):
            print("wrong hash key value pair");
            return;

        if(self.map[keyHash] != None):
            temp = self.map[keyHash].GetRoot();
            if(temp.GetData()==key):
                self.map[keyHash].SetRoot(temp.GetLink());
                return 1;
            elif((temp.GetData()!= key) and (temp.GetLink() == None)):
                print("The element not in hashMap");
                return 0;
            else:
                while(temp != None):
                    if(temp.GetLink().GetData() == key):
                        temp.SetLink(temp.GetLink().GetLink());
                        return 1;
                    temp = temp.GetLink();
            print("The element not in hashMap");
            return 0;
        else:
            print("The element not in hashMap");
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

def main():
    H1 = hashMap();
    H1.add('A');
    H1.add('a');
    H1.add('B');
    H1.add('b');
    H1.add('z');
    H1.add('e');
    H1.add('E');
    H1.add('Q');
    H1.add('q');
    H1.print();
    H1.delete('b');
    H1.delete('Q');
    H1.delete('P');
    H1.print();
    H1.delete('b');
    print(H1.get('A'));
    print(H1.get('Z'));

if(__name__ == "__main__"):
    main();
