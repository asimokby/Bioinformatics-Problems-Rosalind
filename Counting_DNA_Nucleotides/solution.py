
with open("rosalind_dna.txt",'r') as f: 
	out = f.read() 
	s = out

d = {}
for char in s:
	if char in d:
		d[char]+=1
	elif char not in d and char != '\n':
		d[char] = 1

print(d['A'], d['C'], d['G'], d['T'])
