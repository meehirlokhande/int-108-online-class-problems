class Solution(object):
    def repeatedCharacter(self, s):
        res=[1]*len(s)
        for i in range(1,len(s)):
            if s[i] in list(s)[:i]:
                res[i]+=1
        return('' if sum(res)==len(s) else s[[i for i in range(len(res)) if res[i]>=2][0]])
