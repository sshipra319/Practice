
import collections
def lexSmallest(a): 
    dic = {}
    for i in a:
        split_str = list(i)
        min_ord = ord(split_str[0])
        for j in range(1,len(split_str)):
            min_ord = min(min_ord,ord(split_str[j]))
            
        if(min_ord in dic):
            dic[min_ord].append(i)
        else:
            dic[min_ord] = [i]
    for i in dic:
        if(len(dic[i]) > 1):
            dic[i].sort()
    dic = collections.OrderedDict(sorted(dic.items()))
    res = ''
    for i in dic:
        for j in (dic[i]):
            res += j
            
    return res

#a = ['c', 'cc', 'cca', 'cccb']
a = ['abc', 'ab', 'bc']
print(lexSmallest(a))