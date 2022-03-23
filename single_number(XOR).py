def main():
    n=int(input("Enter numbers"))
    arr=list(map(int,input().split(" ")))
    res=0
    for x in arr:
        res=res^x
    print(res)
main()