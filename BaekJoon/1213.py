import collections

word = list(map(str,input()))
word.sort()
dic_cnt = dict(collections.Counter(word))
odd_cnt = 0
center = ""
sort = ""
reverse_sort = ""
for i in dic_cnt:
    if dic_cnt[i]%2 == 1:
        odd_cnt+=1
        center = i
        word.remove(i)
if(odd_cnt>1):
    print("I'm Sorry Hansoo")
else:
    for i in range(0,len(word),2):
        sort+=word[i]
    reverse_sort = sort[::-1]
    print(sort + center + reverse_sort)