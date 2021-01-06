# -*- coding: utf-8 -*-
"""
@author: Shipra
"""

def f(ids,m):
    dict={} 
  
    for i in range(len(ids)):
        if(ids[i] in dict.keys()):
            dict[ids[i]]=dict[ids[i]]+1
        else:
            dict[ids[i]]=1
      
    sorted_d = sorted(dict.items(), key=lambda x: x[1])
    ans=len(dict.keys()) 
      
    removed_till_now=0
      
    for i in range(len(sorted_d)):
        if(removed_till_now+sorted_d[i][1]<=m):
            ans=ans-1 
            removed_till_now=removed_till_now+sorted_d[i][1]
        else:
            break
    return ans

ids = [1,1,1,1]
m = 2
print(f(ids, m))
