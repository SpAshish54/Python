a=int(input(("Enter total numbers\n")))
nums=list(map(int,input().split(" ")))
'''fir=nums[0]
res=[]
count=0
for i in nums:
    if(i!=fir):
        fir=i
        res.append(i)
    else:
        count+=1
        if(count<=1):
            res.append(i)
print(res)
'''
v=set(nums)
print(list(v))