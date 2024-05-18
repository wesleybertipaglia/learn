import csv

fmtparams = {
    'delimiter': ',',
    'quotechar': '"',
    'escapechar': None
}

# Open a CSV file for reading
with open('data.csv', 'r') as file_object:
    reader = csv.reader(file_object, dialect='excel', **fmtparams)
    dict_reader = csv.DictReader(file_object, fieldnames=None, restkey=None, restval=None, dialect='excel', **fmtparams)

# Open a CSV file for writing
with open('output.csv', 'w', newline='') as file_object:
    writer = csv.writer(file_object, dialect='excel', **fmtparams)
    dict_writer = csv.DictWriter(file_object, fieldnames=['Field1', 'Field2'], restval='', extrasaction='raise', dialect='excel', **fmtparams)

# List of available dialects for CSV files
available_dialects = csv.list_dialects()

# Sniffer class to deduce the format of a CSV file
sample = "sample_data"
sniffer = csv.Sniffer().sniff(sample, delimiters=None)

# Register a new dialect with the csv module
name = "custom_dialect"
dialect = csv.excel()
csv.register_dialect(name, dialect)
