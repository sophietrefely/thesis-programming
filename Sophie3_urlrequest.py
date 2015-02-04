print('Hello Sophie')

##got gene list from KEGG for mouse glycolysis/gluconeogenesis pathway and made into txt file
path_to_kegg_glycolysis_list = 'data/mmu00010_glycolysis.txt'
kegg_glycolysis = open(path_to_kegg_glycolysis_list)

for line in kegg_glycolysis:
#needed to remove odd " signs
    clean_kegg_glycolysis = line.replace('"mmu', 'mmu')
#seperated into a list so can isolate the KEGG IDs
#fields[0] is gene name, fields[1] is KEGG ID
    kegg_list = clean_kegg_glycolysis.split('  ')

    kegg_glycolysis_list = kegg_list[0] #these are the KEGG IDs that need converting to uniprot ID

## Need to convert KEGG ID to Uniprot ID using the KEGG API converter:"http://rest.kegg.jp/conv/uniprot/"
#Need to store url output from converter for all of the genes in the list

import urllib.request #allows python to access url 

uniprot_conversion_list = []
for gene in kegg_glycolysis_list:
    kegg_gene = str(gene)
    url = "http://rest.kegg.jp/conv/uniprot/" + kegg_gene
    url_read = urllib.request.urlopen(url).read()
    uniprot_conversion_list.append(url_read)

print(uniprot_conversion_list)

