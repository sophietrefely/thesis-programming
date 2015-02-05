list1 = [b'mmu:100042025\tup:D2KHZ9\nmmu:100042025\tup:P16858\n', b'mmu:103988\tup:P52792\nmmu:103988\tup:Q5SVI5\nmmu:103988\tup:Q5SVI6\n', b'mmu:106557\tup:Q8BVP2\n', b'mmu:110695\tup:Q9DBF1\n', b'mmu:11522\tup:P00329\nmmu:11522\tup:Q3UKA4\n']

##entries = []
##i = 0
##for i in list1:
##    entry = list1[i].split('\n').split('\tup:')
##    print(entry)
##    for entry in list1:
##        entries.append(entry)
##    i = i + 1
##print(entries)




##another try
##i = 0
##entry = list1[i]
##split_entry = entry.split('\n')
##print(split_entry)

entry1 = str(list1[0])
entry1_split = entry1.split('\n')
print(entry1)
print(entry1_split)
print(entry1_split[0])
entry_split2 = entry1.split('\n').split('\tup:')
print(entry1_split2)
