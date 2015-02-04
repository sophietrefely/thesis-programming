print("Hello Sophie")


### If you want the program to stop, type control-c (together)


path_to_data = 'data/separated_sean.txt'
# open the file of sean's data
sean_file = open(path_to_data)

add3_store = []
# visit each line of the file in turn, tab separated
for line in sean_file:
    # remove the newline from the line, it has one by default
    stripped_line = line.strip()
    
    # split creates a list out of the line [<first>, <second>] field
    # fields[0] is gene name, fields[1] is IPI
    fields = stripped_line.split('\t')

    # if the gene name is 'Add3', store the IPI
    # boring but useful if it were another column
if fields[0] == 'Add3':
        add3_store.append(fields[1])

# Just print add3 store, but it could be doing more processing
print(add3_store)

# Print results, one at a time, with a newline after each
for result_item in add3_store:
    print(result_item)
