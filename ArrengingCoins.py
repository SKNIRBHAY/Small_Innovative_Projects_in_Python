from math import *

def countStairs( coins ):
    
    for i in coins:
        sol1 = 0.5 + (sqrt( 1 + 8*i ) / 2);
        sol2 = 0.5 - (sqrt( 1 + 8*i ) / 2);
        if(sol1 > 0 and sol2 > 0):
            if(sol1<sol2):
                print(str(floor(sol1)-1));
            else:
                print(str(floor(sol2)-1));
        else:
            if(sol1>sol2):
                print(str(floor(sol1)-1));
            else:
                print(str(floor(sol2)-1));
                

def main():
    coins = [8,16,21,976];
    countStairs( coins );

if __name__ == "__main__":
    main();
