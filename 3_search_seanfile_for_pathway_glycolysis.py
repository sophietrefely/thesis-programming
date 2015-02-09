## Need to extract all the data from 'sean_list_converted.txt' for the proteins in the KEGG glycolysis/gluconeogenesis pathway. 
# opened file to read:
path_to_sean_list_converted = 'data/sean_list_converted.txt'
sean_list_converted = open(path_to_sean_list_converted, 'rU') #'rU' avoids confusion with read and formatting /r
#turn txt file into a list:
sean_converted_list = []
for line in sean_list_converted:
    stripped_line = line.rstrip()   # remove the newline from the line, it has one by default
    sean_split = stripped_line.split('\t') #fields are tab seperated
    sean_converted_list.append(sean_split)
print("loaded sean's data")
#print(sean_converted_list)

## fetch the uniprot IDs for glycolysis in 'glycolysis_uniprots.txt'
# opened file to read
path_to_glycolysis_uniprots = 'data/glycolysis_uniprots.txt'
glycolysis_uniprots_file = open(path_to_glycolysis_uniprots, 'rU')
glycolysis_uniprots = set(glycolysis_uniprots_file.read().strip().split('\n'))
print(glycolysis_uniprots)
## Export all glycolysis gene data into a new txt file ('glyoclysis_data.txt'):
path_to_glycolysis_data = 'data/glycolysis_data.txt'
glycolysis_data = open(path_to_glycolysis_data, 'w')

# Each item looks like ['37165', 'Q9WTZ4', 'SGGTSSSPIKAIF', ..., <lots of numbers>]
for item in sean_converted_list:
    sean_uniprot = item[1]
    #if uniprot is in the KEGG glycolysis list print all data relating to that protein in sean_list to file
    if sean_uniprot in glycolysis_uniprots:
        item_for_write = '\t'.join(item) + '\n' #join is the opposite of split. split by tab before therefore must join by tab and can then add newline as string because it is no linger a list
        glycolysis_data.write(item_for_write)
glycolysis_data.close()
print('finish')
