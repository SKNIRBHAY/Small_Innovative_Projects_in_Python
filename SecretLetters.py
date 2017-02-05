def reverseStringButPreserveWhiteSpace(Sentance):
    listofWord = Sentance.split(' ');
    result = '';
    for word in listofWord:
        if(word != ''):
            temp = '';
            for j in range((len(word)-1),-1,-1):
                temp = temp + word[j];
            result = result + temp + ' ';
        else:
            result = result + ' ';
    return result;
            

def main():
    result = reverseStringButPreserveWhiteSpace("Let's meet     in the   owlery today");
    print(result);

if __name__ == "__main__":
    main();
