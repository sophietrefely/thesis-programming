kegg_glycolysis_list = ['mmu:100042025', 'mmu:103988', 'mmu:106557', 'mmu:110695']

thing = 'mmu:100666\tup:D2KHZ9\nmmu:100334\tup:P16858\n'
thing.split('\n')[0].split('\tup:')     #converts to ['mmu:100666', 'D2KHZ9']

entries = []
i = 0
while i in thing:
    entry = thing.split('\n')[i].split('\tup:')
        for entry in thing:
        entries.append(entry)
    i = i + 1


 






