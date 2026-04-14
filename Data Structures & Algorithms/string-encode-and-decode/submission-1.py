class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for s in strs:
            x=str(len(s))+"#"+s      #we can use this also
            res+=x                   #res+=str(len(s))+"#"+s
        return res

    def decode(self, s: str) -> List[str]:
        res=[]
        i=0 #making pointer
        while i<len(s):
            j=i #temporary pointer
            while s[j] != "#":
                j+=1
            length=int(s[i:j])
            #taking pointer i to position after '#'
            i=j+1
            word=s[i:i+length]#extraction of word
            res.append(word) #updating list res
            
            #now move pointer i to next section after one word found
            i=i+length
        return res
