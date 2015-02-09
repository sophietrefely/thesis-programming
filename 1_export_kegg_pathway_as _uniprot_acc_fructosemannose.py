#Made a txt file copied from gene list for fructose mannose metabolism pathway on KEGG:
#'http://www.genome.jp/dbget-bin/get_linkdb?-t+genes+path:mmu00051'
###Note - can make this better by accessing this page directly. Just substitute the mmu... according to which pathway you want
path_to_kegg_fruman = 'data/mmu00051_fructosemannose.txt'
kegg_fruman = open(path_to_kegg_fruman)

kegg_fruman_list = []
for line in kegg_fruman:
##needed to remove odd " signs
    clean_kegg_fruman = line.replace('"mmu', 'mmu')
##seperated into a list so can isolate the KEGG ids   
    kegg_list = clean_kegg_fruman.split('  ')   #split into fields where [0] = KEGG ID, [1] = gene name
    kegg_fruman_list.append(kegg_list[0])       #append KEGG ID to list

##Need to convert KEGG IDs to uniprot IDs using the KEGG API

import urllib.request #allows python to access url 

kegg_uniprot_raw = []
for gene in kegg_fruman_list:
    kegg_gene = str(gene)
    url = "http://rest.kegg.jp/conv/uniprot/" + kegg_gene
    url_read = urllib.request.urlopen(url).read()   #read url output
    kegg_uniprot_raw.append(url_read)      #append output to list

# b stands for 'bytestring'. this is here because i didn't use requests to import url data need to convert this to string
kegg_uniprot_str = []
for line in kegg_uniprot_raw:
    line_str = str(line, encoding='utf8') #see http://stackoverflow.com/questions/540342/python-3-0-urllib-parse-error-type-str-doesnt-support-the-buffer-api
    kegg_uniprot_str.append(line_str)   # output looks like above list but no b

# must split
kegg_uniprot_pairs = []
for line in kegg_uniprot_str:
    line_split = line.strip().split('\n')   #strip to get rid of extra ' '
    kegg_uniprot_pairs.append(line_split)

##output looks like this: [['mmu:100042025\tup:D2KHZ9', 'mmu:100042025\tup:P16858'], ['mmu:103988\tup:P52792', 'mmu:103988\tup:Q5SVI5', 'mmu:103988\tup:Q5SVI6'], ['mmu:106557\tup:Q8BVP2'], ['mmu:110695\tup:Q9DBF1'], ['mmu:11522\tup:P00329', 'mmu:11522\tup:Q3UKA4'], ['mmu:11529\tup:Q64437', 'mmu:11529\tup:Q9D748'], ['mmu:11532\tup:P28474', 'mmu:11532\tup:Q6P5I3'], ['mmu:11669\tup:P47738', 'mmu:11669\tup:Q544B1'], ['mmu:11670\tup:P47739', 'mmu:11670\tup:Q3UNF5'], ['mmu:11671\tup:B1AV77', 'mmu:11671\tup:P47740'], ['mmu:11674\tup:A6ZI44', 'mmu:11674\tup:P05064', 'mmu:11674\tup:Q5FWB7']]
# make a new list with the pairs

pairs_list = []
for line in kegg_uniprot_pairs:
    for pair in line:
        pairs_list.append(pair)

## output: ['mmu:100042025\tup:D2KHZ9', 'mmu:100042025\tup:P16858', 'mmu:103988\tup:P52792', 'mmu:103988\tup:Q5SVI5', 'mmu:103988\tup:Q5SVI6', 'mmu:106557\tup:Q8BVP2', 'mmu:110695\tup:Q9DBF1', 'mmu:11522\tup:P00329', 'mmu:11522\tup:Q3UKA4', 'mmu:11529\tup:Q64437', 'mmu:11529\tup:Q9D748', 'mmu:11532\tup:P28474', 'mmu:11532\tup:Q6P5I3', 'mmu:11669\tup:P47738', 'mmu:11669\tup:Q544B1', 'mmu:11670\tup:P47739', 'mmu:11670\tup:Q3UNF5', 'mmu:11671\tup:B1AV77', 'mmu:11671\tup:P47740', 'mmu:11674\tup:A6ZI44', 'mmu:11674\tup:P05064', 'mmu:11674\tup:Q5FWB7']

# split kegg ID and uniprot ID
unpair_list = []
for pair in pairs_list:
    unpair = pair.split('\tup:')
    unpair_list.append(unpair)
print(unpair_list)
print('done')

## output: [['mmu:100042025', 'D2KHZ9'], ['mmu:100042025', 'P16858'], ['mmu:103988', 'P52792'], ['mmu:103988', 'Q5SVI5'], ['mmu:103988', 'Q5SVI6'], ['mmu:106557', 'Q8BVP2'], ['mmu:110695', 'Q9DBF1'], ['mmu:11522', 'P00329'], ['mmu:11522', 'Q3UKA4'], ['mmu:11529', 'Q64437'], ['mmu:11529', 'Q9D748'], ['mmu:11532', 'P28474'], ['mmu:11532', 'Q6P5I3'], ['mmu:11669', 'P47738'], ['mmu:11669', 'Q544B1'], ['mmu:11670', 'P47739'], ['mmu:11670', 'Q3UNF5'], ['mmu:11671', 'B1AV77'], ['mmu:11671', 'P47740'], ['mmu:11674', 'A6ZI44'], ['mmu:11674', 'P05064'], ['mmu:11674', 'Q5FWB7']]

#Extract uniprot IDs and write to a new file:
path_to_fruman_uniprots = 'data/fruman_uniprots.txt'
fruman_uniprots = open(path_to_fruman_uniprots, 'w')
for item in unpair_list:
    uniprot = item[1]
    item_to_write = uniprot + '\n'    #unsplits the list
    fruman_uniprots.write(item_to_write)
fruman_uniprots.close()
