def is_random(s:str):
    s = list(map(int, s))
    s0 = s.count(s[0])==1
    s1 = s.count(s[1])==1
    s2 = s.count(s[2])==1
    s3 = s.count(s[3])==1
    s4 = s.count(s[4])==1
    s5 = s.count(s[5])==1
    if s0 and s1 and s2 and s3 and s4 and s5 and \
        s[0]%2 == s[2]%2 and s[2]%2 == s[4]%2 and \
        s[1]%2 == s[3]%2 and s[3]%2 == s[5]%2 and \
        s[0]%2!=s[1]%2:
            return True
    return False

c=0
for i in range(100000, 999999, 5):
    s = str(i)
    if is_random(s):
        c+=1
print(c)