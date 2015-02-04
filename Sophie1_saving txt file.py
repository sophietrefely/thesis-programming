print("Hello Sophie")


### If you want the program to stop, type control-c (together)


path_to_data = 'data/separated_sean.txt'
# open the file of sean's data
sean_file = open(path_to_data)

for line in sean_file:
# remove the newline from the line, it has one by default
    stripped_line = line.rstrip()
    
    # split creates a list out of the line [<first>, <second>] field
    # fields[0] is gene name, fields[1] is IPI
    fields = stripped_line.split('\t')


    

path_to_kegg_glycolysis_list = 'data/mmu00010_glycolysis.txt'
kegg_glycolysis = open(path_to_kegg_glycolysis_list)

for line in kegg_glycolysis:

    clean_kegg_glycolysis = line.replace('"mmu', 'mmu')
    
    kegg_list = clean_kegg_glycolysis.split('  ')

    clean_kegg_list = kegg_list[0]


##now want to export the cleaned list as a txt file

output_path = 'data/kegg_glycolysis_clean.txt' # this will get overwritten if it already exists
outfile = open(output_path, 'w') # open the file for writing, create it if it doesn't exist

for item in clean_kegg_list: 
    outfile.write(item)
   
    
outfile.close() # important! the file will be empty if you don't do this

     
        
