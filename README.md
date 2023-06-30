# CSV to JSON Converter

This Python script converts a CSV file to JSON format.

## Prerequisites

- Python 3.x

## Usage

1. Download the `csv_to_json.py` script from the [releases](https://github.com/Janithpm/csv2json/releases) page.

2. Open a terminal or command prompt.

3. Navigate to the directory containing the downloaded `csv_to_json.py` file.

4. Run the script using the following command:

   ```bash
   python csv_to_json.py <csv_file>


## Example

Let's say you have a CSV file named `input.csv` with the following content:
```bash
Name,Department,Salary
John Doe,Engineering,50000
Jane Smith,Marketing,45000
```

To convert this CSV file to JSON, you would run the following command:

   ```bash
   python csv_to_json.py input.csv
   ```
The script will generate a JSON file named `input.json` with the following content:

```bash
[
    {
        "Name": "John Doe",
        "Department": "Engineering",
        "Salary": "50000"
    },
    {
        "Name": "Jane Smith",
        "Department": "Marketing",
        "Salary": "45000"
    }
]

```

Feel free to adjust the content and filenames as per your needs.


