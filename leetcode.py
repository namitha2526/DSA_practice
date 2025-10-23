1###3461-check-if-digits-are-equal-in-string-after-operations
class Solution(object):
    def hasSameDigits(self, s):
        """
        :type s: str
        :rtype: bool
        """
        digits = [int(ch)for ch in s]
        while len(digits) > 2:
            digits=[(digits[i] + digits[i+1])% 10 for i in range(len(digits)-1)]
        return digits[0] == digits[1]

###
2###
nums =[1,2,3,1,2,3]
k=2
def containsNearbyDuplicate(nums, k):
    hash={}
    for i in nums:
        hash[i]=hash.get(i,0)+1
    for i,n in enumerate(nums):
        if n in hash and i - hash[n] <= k:
            return True
        hash[n]=i
    return False
containsNearbyDuplicate(nums,k)
###
