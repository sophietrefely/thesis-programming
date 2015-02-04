kegg_glycolysis_list = ['mmu:100042025', 'mmu:103988', 'mmu:106557', 'mmu:110695']

kegg_uniprot_raw = 'mmu:100666\tup:D2KHZ9\nmmu:100334\tup:P16858\n'

# one element looks like 'mmu:100666\tup:D2KHZ9'
kegg_uniprot_pairs = kegg_uniprot_raw.strip().split('\n')

# entries will look like [['mmu:100666', 'D2KHZ9'], ['mmu:100334', 'P16858']]
entries = []
for pair in kegg_uniprot_pairs:
    entry = pair.split('\tup:')
    entries.append(entry)
print(entries)
 






