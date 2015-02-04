print("Hello Sophie")


### If you want the program to stop, type control-c (together)


path_to_data = 'data/separated_sean.txt'
# open the file of sean's data
sean_file = open(path_to_data)

sean_list = []
for line in sean_file:
# remove the newline from the line, it has one by default
    stripped_line = line.rstrip()
    # split creates a list out of the line [<first>, <second>] field
    # [0] is gene name, [1] is IPI
    sean_split = stripped_line.split('\t')
    sean_list.append(sean_split)
    

print(sean_list[1])

##converted IPIs to uniprot accession using DAVID:
#('http://david.abcc.ncifcrf.gov/conversion.jsp')
#saved the output list as 'ipi_uniprot_list.txt'

path_to_uniprot = 'data/ipi_uniprot_list.txt'
uniprot_list = open(path_to_uniprot)

if line in uniprot_list == line in sean_ist[1]:
    line.replace(sean_list[1], uniprot_list)
    


    
