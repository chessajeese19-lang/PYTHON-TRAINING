
d={}
for i in range(len(nums)):
    R=target-nums[i]
    if R in d:
        print[d[R],i]
    d[nums[i]]=i  