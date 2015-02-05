## This solution worked for simple exx data:
##kegg_uniprot_raw = 'mmu:100666\tup:D2KHZ9\nmmu:100334\tup:P16858\n'
### entries will look like [['mmu:100666', 'D2KHZ9'], ['mmu:100334', 'P16858']]
##entries = []
##for pair in kegg_uniprot_pairs:
##    entry = pair.split('\tup:')
##    entries.append(entry)
##print(entries)
###solution looks like [['mmu:100666', 'D2KHZ9'], ['mmu:100334', 'P16858']]



#better example data/list:
kegg_uniprot_raw = [b'mmu:100042025\tup:D2KHZ9\nmmu:100042025\tup:P16858\n', b'mmu:103988\tup:P52792\nmmu:103988\tup:Q5SVI5\nmmu:103988\tup:Q5SVI6\n', b'mmu:106557\tup:Q8BVP2\n', b'mmu:110695\tup:Q9DBF1\n', b'mmu:11522\tup:P00329\nmmu:11522\tup:Q3UKA4\n', b'mmu:11529\tup:Q64437\nmmu:11529\tup:Q9D748\n', b'mmu:11532\tup:P28474\nmmu:11532\tup:Q6P5I3\n', b'mmu:11669\tup:P47738\nmmu:11669\tup:Q544B1\n', b'mmu:11670\tup:P47739\nmmu:11670\tup:Q3UNF5\n', b'mmu:11671\tup:B1AV77\nmmu:11671\tup:P47740\n', b'mmu:11674\tup:A6ZI44\nmmu:11674\tup:P05064\nmmu:11674\tup:Q5FWB7\n']

# b stands for 'bytestring'. this is here because i didn't use requests to import url data need to convert this to string
kegg_uniprot_str = []
for line in kegg_uniprot_raw:
    line_str = str(line, encoding='utf8') #see http://stackoverflow.com/questions/540342/python-3-0-urllib-parse-error-type-str-doesnt-support-the-buffer-api
    kegg_uniprot_str.append(line_str)   # output looks like above list but no b
print('kegg_uniprot_str:')
print(kegg_uniprot_str)

# must split
kegg_uniprot_pairs = []
for line in kegg_uniprot_str:
    line_split = line.strip().split('\n')   #strip to get rid of extra ' '
    kegg_uniprot_pairs.append(line_split)
print('kegg_uniprot_pairs:')
print(kegg_uniprot_pairs)

##output looks like this: [['mmu:100042025\tup:D2KHZ9', 'mmu:100042025\tup:P16858'], ['mmu:103988\tup:P52792', 'mmu:103988\tup:Q5SVI5', 'mmu:103988\tup:Q5SVI6'], ['mmu:106557\tup:Q8BVP2'], ['mmu:110695\tup:Q9DBF1'], ['mmu:11522\tup:P00329', 'mmu:11522\tup:Q3UKA4'], ['mmu:11529\tup:Q64437', 'mmu:11529\tup:Q9D748'], ['mmu:11532\tup:P28474', 'mmu:11532\tup:Q6P5I3'], ['mmu:11669\tup:P47738', 'mmu:11669\tup:Q544B1'], ['mmu:11670\tup:P47739', 'mmu:11670\tup:Q3UNF5'], ['mmu:11671\tup:B1AV77', 'mmu:11671\tup:P47740'], ['mmu:11674\tup:A6ZI44', 'mmu:11674\tup:P05064', 'mmu:11674\tup:Q5FWB7']]

# make a new list with the pairs

##go through fileds[] one by one - need to turn this into a loop
pairs_list_0 = []
for line in kegg_uniprot_pairs:
    entry = line[0]
    pairs_list_0.append(entry)
print('pairs_list_0:')
print(pairs_list_0)
# output was sucessful: ['mmu:100042025\tup:D2KHZ9', 'mmu:103988\tup:P52792', 'mmu:106557\tup:Q8BVP2', 'mmu:110695\tup:Q9DBF1', 'mmu:11522\tup:P00329', 'mmu:11529\tup:Q64437', 'mmu:11532\tup:P28474', 'mmu:11669\tup:P47738', 'mmu:11670\tup:P47739', 'mmu:11671\tup:B1AV77', 'mmu:11674\tup:A6ZI44']

pairs_list_1 = []
for line in kegg_uniprot_pairs:
    entry = line[1]
    pairs_list_1.append(entry)
print('pairs_list_1:')
print(pairs_list_1)

n = int(x)        
pairs_list_n = []
for line in kegg_uniprot_pairs:
    if n <= 3:
        entry = line[n]
        pairs_list_1.append(entry)
print('pairs_list_1:')
print(pairs_list_1)
