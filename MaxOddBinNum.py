class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count = 0
        new = ""
        for x in s:
            if "1" == x:
                count+=1
        print(len(s))
        for x in range(count-1):
            new+="1"
        for x in range(len(s)-count):
            new+="0"
        new+="1"
        return new
        '''
        cnt1 = s.count('1')
        cnt0 = s.count('0')
        ans = '1' * (cnt1 - 1) + '0' * cnt0 + '1'
        return ans
        '''