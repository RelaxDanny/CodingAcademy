n = int(input())
a1 = list(map(int,input().split()))
m = int(input())
a2 = list(map(int,input().split()))

def bin_tree(s,n,st,en):
    if st > en:
        return 0
    mid = (st + en)//2
    if s[mid] > n:
        return bin_tree(s,n,st,mid-1)
    elif s[mid] < n:
        return bin_tree(s,n,mid+1,en)
    else:
        return 1
    

a1.sort()
for i in a2:
    print(bin_tree(a1,i,0,n-1))

