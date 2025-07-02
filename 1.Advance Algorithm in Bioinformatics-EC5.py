import numpy as np
import random

#put the 4 nucleotides in the list so we can make the mRNA by random
nucleotides = list ('ATGC')

number = 0

#numbers of iteration for Monte_Carlo algorithm
Iteration = 1000

Stop_codon = {'TAA', 'TAG', 'TGA'}

for test in range(1000):

    mRNA = ''.join(np.random.choice(nucleotides, replace=True, size=100))   

    #print (mRNA)

    s = mRNA

    r = random.randrange(len(mRNA))

    #print (r)

    s = s[:r] + s[r+1:]

    i = 0

    while (i<len(s)):
        if s[i:i+3] in Stop_codon:
            number += (i*3)
            #print (number)
            break
        i+=3

   
print (number)
total = Iteration *len(s)
print (total)

protien_lenght = (number)/(total)

print (protien_lenght)
