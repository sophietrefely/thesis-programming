##Made a txt file copied from gene list for glycolysis pathway on KEGG
path_to_kegg_glycolysis_list = 'data/mmu00010_glycolysis.txt'
kegg_glycolysis = open(path_to_kegg_glycolysis_list)

kegg_glycolysis_list = []
for line in kegg_glycolysis:
##needed to remove odd " signs
    clean_kegg_glycolysis = line.replace('"mmu', 'mmu')
##seperated into a list so can isolate the KEGG ids   
    kegg_list = clean_kegg_glycolysis.split('  ')   #split into fields where [0] = KEGG ID, [1] = gene name
    kegg_glycolysis_list.append(kegg_list[0])       #append KEGG ID to list


##Need to convert KEGG IDs to uniprot IDs using the KEGG API
import urllib.request #allows python to access url 

uniprot_conversion_list = []
for gene in kegg_glycolysis_list:
    kegg_gene = str(gene)
    url = "http://rest.kegg.jp/conv/uniprot/" + kegg_gene
    url_read = urllib.request.urlopen(url).read()   #read url output
    uniprot_conversion_list.append(url_read)      #append output to list

print(uniprot_conversion_list)



