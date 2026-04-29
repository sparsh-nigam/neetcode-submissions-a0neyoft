class Solution:
    def isValid(self, s: str) -> bool:
        lis=[]
        for ch in s:
            if ch == '(':
                lis.append(')')
            elif ch  == '{':
                lis.append('}')
            elif ch == '[':
                lis.append(']')
            else:
                if not lis or lis.pop() != ch:
                    return False
        return len(lis)==0