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