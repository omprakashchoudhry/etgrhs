N=int(input(""))
if N<100000:
    S=list(input().split())
    S.sort()
    print(''.join(reversed(S)))
