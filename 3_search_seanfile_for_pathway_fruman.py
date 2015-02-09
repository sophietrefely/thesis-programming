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

## fetch the uniprot IDs for fructose/mannose pathway in 'fruman_uniprots.txt'
# opened file to read
path_to_fruman_uniprots = 'data/fruman_uniprots.txt'
fruman_uniprots_file = open(path_to_fruman_uniprots, 'rU')
fruman_uniprots = set(fruman_uniprots_file.read().strip().split('\n'))  # this makes a set rather than a list so in the next step the search for each entry searches the whole set, where there could be multiple entries, rather than stopping when finding one as in a  list 
print(fruman_uniprots)

## Export all fruman gene data into a new txt file ('glyoclysis_data.txt'):
path_to_fruman_data = 'data/fruman_data.txt'
fruman_data = open(path_to_fruman_data, 'w')

# Each item looks like ['37165', 'Q9WTZ4', 'SGGTSSSPIKAIF', ..., <lots of numbers>]
for item in sean_converted_list:
    sean_uniprots = item[1]
    sean_uniprot_split = sean_uniprots.split(' ') #split the multiple space separated uniprots into seperate elements
    for element in sean_uniprot_split:
        uniprot = element
    #if uniprot is in the KEGG fructose mannose list print all data relating to that protein in sean_list to file
        if uniprot in fruman_uniprots: #this is a set not a list so can find multiple entries not th efirst only
            item_for_write = '\t'.join(item) + '\n' #join is the opposite of split. split by tab before therefore must join by tab and can then add newline as string because it is no longer a set/list
            fruman_data.write(item_for_write)
fruman_data.close()
print('finish')
