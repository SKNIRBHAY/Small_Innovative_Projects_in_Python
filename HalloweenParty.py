
def HalloweenParty():
    T = int(input());
    Ks = [None] * T;
    for k in range(0,T):
        Ks[k] = int(input());
    for k in Ks:
        c = k//2;
        r = k-c; 
        print(c*r);

def main():
    HalloweenParty();

if __name__ == "__main__":
    main();
