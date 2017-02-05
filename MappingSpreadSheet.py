
def returnStr(number1):
    temp = 26;
    number = number1;
    count1 = 1;

    if(number < 26):
        print(chr(number));
        return;
    
    while(1):
        number = number - temp;
        count1 += 1;
        if(number < (temp*26)):
            break;
        else:
            temp = temp * 26;
            continue;

    print("Temp = " + str(temp));
    print("Number = " + str(number));
    
    count2 = 0;
    while(temp>1):
        count2 = 0;
        while(1):
            number -= temp;
            count2 += 1;
            if(number < temp):
                print(chr(65 + count2), end="");
                break;
            else:
                continue;
        temp = temp/26;
    if(number > 0):
        number -= 1;
    print(chr(65 + int(number)), end="");

returnStr(52);
