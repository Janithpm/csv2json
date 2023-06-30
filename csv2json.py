import csv
import json
import os
import sys


def csv2json(csvFile):
    with open(csvFile, 'r') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    
    with open(jsonFile, 'w') as f:
        json.dump(rows, f, indent=4)

    return rows

if __name__ == '__main__':

    if len(sys.argv) < 2:
        print('Usage: python csv2json.py <csv_file_name>')
        sys.exit(1)
    
    csvFileName = sys.argv[1]
    csvFile = os.path.join(os.getcwd(), csvFileName)
    jsonFile = os.path.join(os.getcwd(), csvFileName.split('.')[0] + '.json')

    rows = csv2json(csvFileName)
    print(f'\n 🪄\tConvert {csvFile} to {jsonFile} successfully! 🥳 🎉 🎈')
    print(f'\n 🪄\tTotal {len(rows)} rows.')