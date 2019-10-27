with open("rosalind_rna.txt",'r') as f: 
	out = f.read() 
	s = out

s = list(s)
for i in range(len(s)): 
    if s[i] == 'T':
        s[i] = 'U'
print("".join(s))
