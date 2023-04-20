import csv
import argparse

def replace_items(input_file, mapping_file, output_file):
    with open(input_file, 'r') as input_f, \
         open(mapping_file, 'r') as mapping_f, \
         open(output_file, 'w', newline='') as output_f:
        
        # Read mapping file and create a dictionary of replacements
        mapping_reader = csv.reader(mapping_f)
        replacements = {row[0]: row[1] for row in mapping_reader}
        print(replacements)

        # Read input file and perform replacements
        input_reader = csv.reader(input_f)
        output_writer = csv.writer(output_f)
        for row in input_reader:
            updated_row = [replacements.get(item, item) for item in row]
            output_writer.writerow(updated_row)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Replace items in a CSV file based on a mapping file')
    parser.add_argument('input_file', help='CSV file on which replacements are to be done')
    parser.add_argument('mapping_file', help='CSV file containing mappings of items to be replaced and their replacements')
    parser.add_argument('output_file', help='Output CSV file with replacements performed')
    args = parser.parse_args()