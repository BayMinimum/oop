import csv

def table_to_dict(data_file):
    a_dict = {}
    reader = csv.reader(data_file)

    for row in reader:
        if row[0].isdigit():
            a_dict[row[1]] = row[:8]

    return a_dict


def parse_element(element_str):
    last_alpha = 0
    while last_alpha < len(element_str):
        if not element_str[last_alpha].isalpha():
            break
        last_alpha += 1
    symbol = element_str[:last_alpha]
    quantity = int(element_str[last_alpha:]) if last_alpha < len(element_str) else 1
    return symbol, quantity

# Open file
data_file = open('../Periodic-Table.csv', encoding='windows-1252')

# Create dictionary
periodic_dict = table_to_dict(data_file)

# Get input and parse
element_list = []
for element_quantity in input('Input a chemical compound, hyphenated, e.g. H2-O: ').split('-'): # Prompt user for compound
    element_list.append(parse_element(element_quantity))

mass = 0.0
print('The compound is composed of', end=' ')

for element, quantity in element_list:
    print(periodic_dict[element][5], end=', ') # Print this element name
    mass += quantity * float(periodic_dict[element][6]) # Add mass for this element

print('\nThe atomic mass of the compound is {:f}'.format(mass))
