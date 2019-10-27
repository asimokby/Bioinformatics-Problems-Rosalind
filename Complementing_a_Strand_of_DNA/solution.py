with open("rosalind_revc.txt",'r') as f: 
	out = f.read() 
	s = out

res = ""
for i in range(-1, -len(s)-1, -1):
    if s[i] == 'T':
        res += 'A'
    elif s[i] == 'A':
        res += 'T'
    elif s[i] == 'C':
        res += 'G'
    elif s[i] == 'G':
        res += 'C'
print(res)
