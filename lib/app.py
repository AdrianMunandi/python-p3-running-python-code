print("Hello World! Pass this test, please.")

def pilot(nums,target):
    new_nums={}
    for idx, item in enumerate(nums):
        y=target-item
        if y in new_nums:
            return [new_nums[y],idx]
        new_nums[item]=idx
    return
print(pilot([2,5,6,7,11],8))

def getConcatenation(nums):
    ans=[n for i in range(2) for n in nums]
    return ans

print(getConcatenation([2,3]))
