
def SmallestNumber(coordinates, value):
    end = value;
    start = 0;
    answer = '';
    if(value == 0):
        return coordinates;
    elif(value >= len(coordinates)):
        return '0';
    else:
        while(end < len(coordinates)):
            temp = start;
            minValue = coordinates[start];
            minIndex = start;
            while(temp<=end):
                if(coordinates[temp] <= coordinates[minIndex]):
                    minIndex = temp;
                    minValue = coordinates[minIndex];
                temp += 1;
            answer = answer + str(coordinates[minIndex]);
            start = minIndex + 1;
            end += 1;
        print (answer);

def main():
    SmallestNumber("1099950905",5);

if __name__ == "__main__":
    main();
                    
