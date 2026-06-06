"""
File Read and Write Basics
"""

import csv
import json
import os
from pathlib import Path

# Create data folder if it doesn't exist
os.makedirs("data", exist_ok=True)

# Create sample file for reading
with open("data/sample.txt", "w") as file:
    file.write("Hello from sample file!\n")
    file.write("This is line 2\n")
    file.write("This is line 3\n")
print()

# Reading files
with open("data/sample.txt", "r") as file:
    content = file.read()
    print(content)
print()

# Reading line by line
with open("data/sample.txt", "r") as file:
    for line in file:
        print(line.strip())
print()

# Reading all lines into a list
with open("data/sample.txt", "r") as file:
    lines = file.readlines()
    print(lines)
print()

# Reading specific number of characters
with open("data/sample.txt", "r") as file:
    first_20 = file.read(20)
    print(first_20)
print()

# Writing to a file
with open("data/output.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a new file.\n")
    file.write("Line 3\n")
print()

# Appending to a file
with open("data/output.txt", "a") as file:
    file.write("Appended line\n")
    file.write("Another appended line\n")
print()

# Reading the modified file
with open("data/output.txt", "r") as file:
    print(file.read())
print()

# Writing multiple lines
lines_to_write = ["Line 1\n", "Line 2\n", "Line 3\n", "Line 4\n"]
with open("data/output.txt", "w") as file:
    file.writelines(lines_to_write)
print()

# Reading and modifying content
with open("data/output.txt", "r") as file:
    lines = file.readlines()

modified_lines = [line.upper() for line in lines]

with open("data/output_modified.txt", "w") as file:
    file.writelines(modified_lines)

with open("data/output_modified.txt", "r") as file:
    print(file.read())
print()

# File position
with open("data/sample.txt", "r") as file:
    print("Position at start:", file.tell())
    file.read(10)
    print("Position after reading 10 chars:", file.tell())
    file.seek(0)
    print("Position after seek(0):", file.tell())
print()

# Checking if file exists
if os.path.exists("data/sample.txt"):
    print("File exists")
else:
    print("File does not exist")
print()

# Getting file size
if os.path.exists("data/sample.txt"):
    size = os.path.getsize("data/sample.txt")
    print(f"File size: {size} bytes")
print()

# Listing files in directory
files = os.listdir("data")
print(f"Files in data folder: {files}")
print()

# Working with file paths
path = os.path.join("data", "file.txt")
print(f"Joined path: {path}")
print()

# Getting absolute path
abs_path = os.path.abspath("data/sample.txt")
print(f"Absolute path: {abs_path}")
print()

# Splitting path into directory and filename
directory, filename = os.path.split(abs_path)
print(f"Directory: {directory}")
print(f"Filename: {filename}")
print()

# Writing and reading CSV files
csv_data = [
    ["Name", "Age", "City"],
    ["Alice", "25", "New York"],
    ["Bob", "30", "Los Angeles"],
    ["Charlie", "35", "Chicago"],
]

with open("data/data.csv", "w", newline="") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(csv_data)
print()

# Reading CSV files
with open("data/data.csv", "r") as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)
print()

# Reading CSV with DictReader
with open("data/data.csv", "r") as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(row)
print()

# Writing CSV with DictWriter
csv_dict_data = [
    {"Name": "Alice", "Age": "25", "City": "New York"},
    {"Name": "Bob", "Age": "30", "City": "Los Angeles"},
    {"Name": "Diana", "Age": "28", "City": "Chicago"},
]

with open("data/output_data.csv", "w", newline="") as file:
    fieldnames = ["Name", "Age", "City"]
    csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
    csv_writer.writeheader()
    csv_writer.writerows(csv_dict_data)
print()

# Reading the CSV file back
with open("data/output_data.csv", "r") as file:
    print(file.read())
print()

# Writing and reading JSON files
json_data = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "hobbies": ["reading", "coding", "gaming"],
}

with open("data/data.json", "w") as file:
    json.dump(json_data, file, indent=4)
print()

# Reading JSON files
with open("data/data.json", "r") as file:
    data = json.load(file)
    print(data)
print()

# Reading and writing JSON strings
json_string = '{"name": "Bob", "age": 30, "city": "Los Angeles"}'
data = json.loads(json_string)
print(data)
print()

json_output_string = json.dumps(data, indent=2)
print(json_output_string)
print()

# Exception handling for file operations
try:
    with open("data/nonexistent.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found error caught")
except IOError as e:
    print(f"IO Error: {e}")
print()

# Using pathlib for modern path handling
p = Path("data/sample.txt")
if p.exists():
    print(f"File exists: {p.name}")
print()

# Reading file with pathlib
if p.exists():
    content = p.read_text()
    print(f"Content using pathlib:\n{content}")
print()

# Writing file with pathlib
p_out = Path("data/output_pathlib.txt")
p_out.write_text("Hello from pathlib!\nLine 2\nLine 3\n")
print()

# Reading file written with pathlib
print(p_out.read_text())
print()

# Listing files with pathlib
folder = Path("data")
txt_files = list(folder.glob("*.txt"))
print(f"Text files found: {[str(f) for f in txt_files]}")
