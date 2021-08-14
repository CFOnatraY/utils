import io
import os
import re

current_path = "."
cleaned_files_directory = "cleaned_files"


def clean_file(file_name):
    f = io.open(file_name, 'r', encoding='utf8')
    text_buffer = f.readlines()

    regex = re.compile('^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}', re.I)

    cleaned_content_lines = []

    for line in text_buffer:
        if "NOTE Confidence: 0." not in line \
                and "WEBVTT" not in line \
                and not line.startswith("NOTE language:") \
                and not line.startswith("NOTE duration:") \
                and not line.startswith("-->", 13) \
                and not regex.match(line) \
                and not remove_empty_spaces(line) == "":
            cleaned_content_lines.append(line)

    new_filename = file_name.split(".")[0] + " - cleaned.txt"

    save_cleaned_file_to_directory(new_filename, convert_to_single_line(cleaned_content_lines))


def convert_to_single_line(lines):
    single_line = ""

    for line in lines:
        single_line += line.rstrip() + " "

    return [single_line]


def save_cleaned_file_to_directory(file_name, cleaned_content_lines):
    filepath = os.path.join("..", cleaned_files_directory, file_name)
    cleaned_file = io.open(filepath, "w", encoding="utf-8")
    cleaned_file.writelines(cleaned_content_lines)
    cleaned_file.close()

    print("Just created the following new file: {}".format(filepath))


def create_cleaned_files_path():
    path = os.path.join('..', cleaned_files_directory)
    print("I'm going to attempt to create a new folder outside this current directory and it will be named: {}".format(
        cleaned_files_directory))
    try:
        os.mkdir(path)
    except OSError as error:
        print(error)


def remove_empty_spaces(string):
    pattern = re.compile(r'\s+')
    return re.sub(pattern, '', string)


# Here is where the magic happens:
create_cleaned_files_path()

for _path, dirs, files in os.walk(current_path):
    for filename in files:
        if filename.endswith(".vtt"):
            print("Currently working on file: {}".format(filename))
            clean_file(filename)
