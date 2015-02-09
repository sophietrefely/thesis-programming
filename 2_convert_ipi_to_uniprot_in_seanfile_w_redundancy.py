### Sean's data = supp table S2 at 'http://www.ncbi.nlm.nih.gov/pmc/articles/PMC3690479/?report=classic'
### copied relevent feilds from Sean's data into a new spreadsheet and exported as tab sep txt file.  
##
##path_to_data = 'data/separated_sean.txt'
### Open the file of sean's data
### Use universal newlines ('rU') because there are '\r' in the file
##sean_file = open(path_to_data, 'rU') 
##
### split creates a list out of the line [<first>, <second>] field
### [0] is gene name, [1] is IPI
##sean_list = []
##for line in sean_file:
##    stripped_line = line.rstrip()   # remove the newline from the line, it has one by default
##    sean_split = stripped_line.split('\t') #fields are tab seperated
##    sean_list.append(sean_split)

#converted 'sean_ipis' to uniprot accession using DAVID:
#'http://david.abcc.ncifcrf.gov/conversion.jsp'
# saved the conversion list as 'sean_conversion_list.txt'

path_to_conversion_david = 'data/sean_conversion_list.txt'
conversion_david= open(path_to_conversion_david, 'r')

# turn list into a dictionary. key = IPI, value = uniprots
# there is redundancy in the uniprot accessions ie several per IPI
# therefore will need to make a list within each value: dictionary = {IPI:[uniprot1,unpirot2], IPI:[uniprotb, uniprotc]}

conversion_dict = {}
for line in conversion_david:
    stripped_line = line.rstrip()
    split_line = stripped_line.split('\t')
    ipi = split_line[0]
    uniprot = split_line[1]
    if ipi in conversion_dict:
        new_uniprot = uniprot
        old_uniprot = conversion_dict[ipi]
        uniprot_list = old_uniprot
        if new_uniprot in old_uniprot:
            conversion_dict[ipi] = old_uniprot
        else:
            uniprot_list.append(new_uniprot)
            conversion_dict[ipi] = uniprot_list
    else:
        conversion_dict[ipi] = [uniprot]
print(conversion_dict)

##
### Each entry in sean_list looks like
### [<gene_name>, <ipi>, <some_other_data>, ... <lots of numbers>]
### replace IPIs in Sean_list with matching uniprot list from conversion_dict so it will look like:
### [<gene_name>, <[uniprota, uniprotb]>, <some_other_data>, ... <lots of numbers>]
##path_to_sean_list_converted = 'data/sean_list_converted.txt'
##sean_list_converted = open(path_to_sean_list_converted, 'w') # w makes it ready to write the file
##
##for item in sean_list:
##    sean_ipi = item[1]
##    # If the IPI has a conversion to a uniprot, convert it
##    if sean_ipi in conversion_dict:
##        uniprot = conversion_dict[sean_ipi] #find value(uniprots) in dictionary
##        item[1] = uniprot #convert ipi to uniprots
##        item_to_write = '\t'.join(item) + '\n'    #unsplits the list so that the file output will look like: <gene_name>/t<uniprot>/t<some_other_data>/t ... <lots of numbers> instead of a list with [] as above.  
##        sean_list_converted.write(item_to_write)
##    else:
##        print(sean_ipi) #this gives the ipis that were not assigned to uniprot accession in first run through DAVID.
##sean_list_converted.close() #must close file after writing
##


