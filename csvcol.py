#!/usr/bin/env python
import sys
import csv


def print_usage():
    print sys.argv[0]
    print """Usage: %s input_csv_filename output_column_names [rename_column_names]

Reorders the columns in a csv file whose first line is column headers.
Output is printed to stdout.

input_csv_filename: (Required) Name of the csv file to process.  The
    first line of the file must be the column headers.

output_column_names: (Required) Comma-separated list of columns to
    include, in order, in the csv output.  There should be no
    whitespace around the commas, and there will be a cryptic error
    message if one or more of the output_column_names isn't in the
    input csv file.

rename_column_names: (Optional) Comma-separated list of columns to use
    as the header for the output csv file, thereby letting you rename
    the columns from the original file.  The length of the
    comma-separated list must exactly match the length of the
    output_column_names list.
""" % sys.argv[0]
    

def main():
    if len(sys.argv) < 3:
        print_usage()
        sys.exit(1)
    input_csv_filename = sys.argv[1]
    comma_separated_out_column_names = sys.argv[2]

    if len(sys.argv) == 3:
        out_columns = comma_separated_out_column_names.split(',')
        comma_separated_rename_to_column_names = sys.argv[3]
    else:
        print_usage()
        sys.exit(1)

    with open(input_csv_filename, 'rb') as incsvfile:
        csvreader = csv.DictReader(incsvfile)
        csvwriter = csv.DictWriter(sys.stdout, fieldnames=out_columns)
        print comma_separated_rename_to_column_names
        for row in csvreader:
            subrow = {k:v for k,v in row.iteritems() if k in out_columns}
            csvwriter.writerow(subrow)
        

if __name__ == '__main__':
    main()
