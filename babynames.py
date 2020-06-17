#!/usr/bin/env python
# -*- coding: utf-8 -*-

# BabyNames python coding exercise.

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

"""
Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration. Here's what the HTML looks like in the
baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 - Extract all the text from the file and print it
 - Find and extract the year and print it
 - Extract the names and rank numbers and print them
 - Get the names data into a dict and print it
 - Build the [year, 'name rank', ... ] list and print it
 - Fix main() to use the extracted_names list
"""

import sys
import re
import argparse


def extract_names(filename):
    """
    Given a single file name for babyXXXX.html, returns a
    single list starting with the year string followed by
    the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', 'Aaron 57', 'Abagail 895', ...]
    """
    names = []
    names_disct = {}
    # +++your code here+++
    with open(filename) as file:
        data = file.read()
        pattern = re.compile(r'Popularity in')
        matches = pattern.finditer(data)
        for match in matches:
            year = match.span()
            names.append(data[year[1]:][1:5])

    with open(filename) as file_name:
        for line in file_name:
            rank_name = re.findall(
                f'"right"><td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', line)
            for name in rank_name:
                if not name[1] in names_disct:
                    names_disct[name[1]] = name[0]
                if not name[2] in names_disct:
                    names_disct[name[2]] = name[0]
    for key in sorted(names_disct):
        names.append(key + " " + names_disct[key])

    return names


def create_parser():
    """Create a command line parser object with 2 argument definitions."""
    parser = argparse.ArgumentParser(
        description="Extracts and alphabetizes baby names from html.")
    parser.add_argument(
        '--summaryfile', help='creates a summary file', action='store_true')
    # The nargs option instructs the parser to expect 1 or more
    # filenames. It will also expand wildcards just like the shell.
    # e.g. 'baby*.html' will work.
    parser.add_argument('files', help='filename(s) to parse', nargs='+')
    return parser


def main(args):
    # Create a command line parser object with parsing rules
    parser = create_parser()
    # Run the parser to collect command line arguments into a
    # NAMESPACE called 'ns'
    ns = parser.parse_args(args)

    if not ns:
        parser.print_usage()
        sys.exit(1)
    file_list = ns.files

    # option flag
    create_summary = ns.summaryfile

    # For each filename, call `extract_names()` with that single file.
    # Format the resulting list as a vertical list (separated by newline \n).
    # Use the create_summary flag to decide whether to print the list
    # or to write the list to a summary file (e.g. `baby1990.html.summary`).

    # +++your code here+++
    for file in file_list:
        name_output = extract_names(file)
        # print("-"*40)
        # print(create_summary)
        # print("-"*40)
        name_output = "\n".join(name_output)
        if not create_summary:
            print(name_output)
        else:
            new_file = file + ".summary"
            file = open(new_file, "w")
            file.write(str(name_output))
    # print("-"*40)
    # print(create_summary)
    # print("-"*40)


if __name__ == '__main__':
    main(sys.argv[1:])
