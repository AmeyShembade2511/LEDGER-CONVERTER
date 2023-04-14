import re
s="102003 SYSTEMS IN MECH. ENGG. 030/030 060/070 090/100 --- --- --- 90 03 O 10 30 --- ---"
s1="102003 SYSTEMS IN MECH. ENGG. --- --- --- --- 023/025 --- 92 01 O 10 10 --- ---"
s2="210244 COMPUTER GRAPHICS 020/030 060/070 080/100 --- --- --- 80 03 A 09 27 --- ---"

patt4=re.compile(r'(\s(\d+)\s)')
patt=re.compile(r'\s{0}(\d+)\b')
comp=patt.search(s2)
comp2 = patt4.search(s2)
print(re.search(r'(\s(\d+)\s)',s1))

print(comp2)
if(comp2):
    print(comp2.group(0))
    #print(comp2[0][0])
print(comp)    
print(comp.group(0))