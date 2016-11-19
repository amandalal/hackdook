#!/usr/bin/python
chmod a+x gc.py
dna_seq = 'atgcatgacgatgcgatagcgatgtgatccatgtactgagtgtcgatcg'
no_c = dna_seq.count('c')
no_g = dna_seq.count('g')
dnalength = len(dna_seq)
gcpercent = (no_c + no_g) *100/dnalength
print(gcpercent)

