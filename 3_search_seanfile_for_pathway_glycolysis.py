## Need to extract all the data from 'sean_list_converted.txt' for the proteins in the KEGG glycolysis/gluconeogenesis pathway. 
# opened file to read:
path_to_sean_list_converted = 'data/sean_list_converted_redundant.txt'
sean_list_converted_redundant = open(path_to_sean_list_converted, 'rU') #'rU' avoids confusion with read and formatting /r
#turn txt file into a list:
# each entry in list will look like:
# ['37165', "['Q6Y681', 'Q63891', 'Q61994', 'Q9WTZ5', 'Q9WTZ6', 'Q7TSC9', 'Q7TSD0', 'Q8C4C1', 'Q99JF4', 'P25425', 'Q99JH0', 'Q8BT04', 'Q8K570', 'Q9WTZ4']", 'SGGTSSSPIKAIF', '-0.13', '-0.05', '0.14', '0.06', '-0.07', '0.1', '0.8', '-0.12', '0.81', 'NaN', 'NaN', 'NaN', '-0.13', '-0.05', 'NaN', 'NaN', 'NaN', 'NaN', '0.14', 'NaN', 'NaN', '0.06', 'NaN', 'NaN', '-0.07', 'NaN', 'NaN', '0.10', '0.51', 'NaN', '1.08', 'NaN', 'NaN', '-0.12', 'NaN', '1.05', '0.56', 'NaN', 'NaN', 'NaN']
sean_converted_list = []
for line in sean_list_converted_redundant:
    stripped_line = line.rstrip()   # remove the newline from the line, it has one by default
    sean_split = stripped_line.split('\t') #fields are tab seperated
    sean_converted_list.append(sean_split)
print("loaded sean's data")

## fetch the uniprot IDs for glycolysis in 'glycolysis_uniprots.txt'
# opened file to read
path_to_glycolysis_uniprots = 'data/glycolysis_uniprots.txt'
glycolysis_uniprots_file = open(path_to_glycolysis_uniprots, 'rU')
glycolysis_uniprots = set(glycolysis_uniprots_file.read().strip().split('\n'))
print(glycolysis_uniprots)

## Export all glycolysis gene data into a new txt file ('glyoclysis_data.txt'):
path_to_glycolysis_data = 'data/glycolysis_data.txt'
glycolysis_data = open(path_to_glycolysis_data, 'w')


# Each item looks like ['37165', "['Q6Y681', 'Q63891', 'Q61994', 'Q9WTZ5']" , 'SGGTSSSPIKAIF', ..., <lots of numbers>]
# ie ['number', "['uniprot a', 'uniprot b']", 'sequence', 'number', ....]
for item in sean_converted_list:
    sean_uniprots = eval(item[1])  #eval unpacks the values  in the "[]". 
    for sean_uniprot in sean_uniprots: #go through each uniprot in redundant list   
#if uniprot is in the KEGG fructose mannose list print all data relating to that protein in sean_list to file
        if sean_uniprot in glycolysis_uniprots: #this is list so only uses the first entry - stops repetition as sean_conversion_list is redundant for all possible uniprots
            item_for_write = '\t'.join(item) + '\n' #join is the opposite of split. split by tab before therefore must join by tab and can then add newline as string because it is no longer a set/list
            glycolysis_data.write(item_for_write)
glycolysis_data.close()
print('finish')

# elimante duplicates - by making a set
path_to_glycolysis_datanodupl = 'data/glycolysis_data_nodupl.txt'
path_to_glycolysis_data = 'data/glycolysis_data.txt'

lines_seen = set() # holds lines already seen
outfile = open(path_to_glycolysis_datanodupl, "w")
for line in open(path_to_glycolysis_data, "r"):
    if line not in lines_seen: # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
outfile.close()
