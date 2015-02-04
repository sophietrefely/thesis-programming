print('Hello Sophie')

## I want to get url output from this address for all of the genes in the list
import urllib.request
kegg_gene = 'mmu:100042025'
url = "http://rest.kegg.jp/conv/uniprot/" + kegg_gene
url_read = urllib.request.urlopen(url).read()

print(url_read)

#the conversion comes out w tabs and newlines as: b'mmu:100042025\tup:D2KHZ9\nmmu:100042025\tup:P16858\n'
#I want to extract the uniprot IDs and store them.
#To do this I need to:
#1. Get rid of the 'up:'
#2. make it into a list
#3 Extract only the uinprot IDs from list


uniprot_conversion_list = []
for line in url_read:
#replace 'up:' with '':
    clean_url_read = line.replace('up:', '')
# split creates a list out of the line [<first>, <second>] field
    # fields[0] is KEGG ID, fields[1] is uniprot ID
    fields = url_read.split('\t')

print(clean_url_read)

##instead of list can try dictionary:
uniprot_conversion_dict = {}

line = url_read
while line:
    kegg, uniprot = line.split(\t)
    line = url_read

print(uniprot_conversion_dict)
