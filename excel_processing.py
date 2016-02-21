##to change pathways (ie glycolysis to fruman) change file names

path_to_excel_file = 'data/excel_fruman.txt'
excel_file = open(path_to_excel_file, 'r')
#turn into a list
excel_file_list = []
for line in excel_file:
    stripped_line = line.rstrip()   # remove the newline from the line, it has one by default
    split_line = stripped_line.split('\t') #fields are tab seperated
    excel_file_list.append(split_line)
#print(excel_file_list) #looks like [['Acss2', '1.080887921'], ['Acss2', '0.887119972'],....]

#count how many entries for each gene and print a new list ['gene', 'entries']
#call it number_gene_list

#NOTE: this bit not working

number_gene_list = []
for entry in excel_file_list:
    gene = entry[0]
    for item in number_gene_list:
        if item == gene:
            item = item + gene
    else:
        number_gene_list.append(gene)
print(number_gene_list)
    
#NOTE: this bit not working    


#make a new list where fold, mean ins/bas (entry[1]) is classified as positive (>=1.2) or negative (<=0.8)
#first remove entries without a mean value ie a list of length 1
new_excel_list = []
for entry in excel_file_list:
    if len(entry) > 1:
        new_excel_list.append(entry)

for entry in new_excel_list:
    if entry[1]:
        ins_bas_raw = entry[1]
        ins_bas = float(ins_bas_raw)    #must convert string to a floating number
        if ins_bas <= 0.8:
            entry[1] = 'negative'
        if ins_bas >= 1.2:
            entry[1] = 'postitive'
        else:
            entry[1] = 'no change'
#print(new_excel_list) #look like [['Acss2', 'no change'], ['Acss2', 'no change'],...]
path_to_python_file = 'data/python_fruman.txt'
python_file = open(path_to_python_file, 'w')

for item in new_excel_list:
    text_to_write = '\t'.join(item) + '\n'
    python_file.write(text_to_write)
python_file.close()


#separate into lists according to ins_bas :'postitive', 'negative' and 'no change'
#NOTE! this bit is not working
positive_list = []
for entry in new_excel_list:
    gene = entry[0]
    value = entry[1]
    if value == 'positive':
        positive_list.append(gene) 
print(positive_list)

negative_list = []
for entry in new_excel_list:
    gene = entry[0]
    value = entry[1]
    if value == 'negative':
        negative_list.append(gene)
print(negative_list)
#NOTE! this bit is not working
