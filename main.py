def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def main():
    print("{} + {} = {}".format(1, 2, add(1, 2)))
    print("{} - {} = {}".format(2, 1, sub(2, 1)))
    print("{} * {} = {}".format(2, 2, mul(2, 2)))
    
if __name__ == '__main__':
    main()