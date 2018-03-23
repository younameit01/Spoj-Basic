t = int(input())
for k in range(t):
    l,c = input().split(' ')
    l = int(l)
    c = int(c)
    for i in range(l * 3 + 1):
        for j in range(c * 3 + 1):
            if(i % 3 == 0 or j % 3 == 0):
                print("*", end = "")
            else:
                print(".", end = "")
        print("\n")
