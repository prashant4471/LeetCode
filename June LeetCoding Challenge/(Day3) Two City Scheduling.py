class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        l=[]
        for i in costs:
            l.append(i[0]-i[1])
        l2=l[0:]
        l2.sort()
        m=len(l)
        n=m/2
        sum1=0
        sum2=0
        d=1
        for i in l2:
            s=l.index(i)
            if d<=n:
                sum1+=costs[s][0]
                d+=1
            else:
                sum2+=costs[s][1]
                d+=1
        sum=sum1+sum2
        return sum
        
        
        
#only 21 out of 49 test cases passes :((
