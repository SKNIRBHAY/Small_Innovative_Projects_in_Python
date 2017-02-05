
def returnValidString(inString):
    list1 = [];
    list2 = [];
    inList = list(inString);
    if(ord(inString[0])<65 or  ord(inString[0])>90):
        return -1;
    for i in range(1,len(inString),1):
        inString[i]


def main():
    string = "HelloWorld";
    returnValidString(string);

if __name__ == "__main__":
    main();





































