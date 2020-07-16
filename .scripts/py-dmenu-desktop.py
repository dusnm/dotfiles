#!/usr/bin/env python3
#
# Copyright (C) 2020 Dusan Mitrovic <dusan@dusanmitrovic.xyz>
# Licensed under the terms of the GNU GPL, version 3 only
#
# A python script to launch .desktop applications with dmenu
import os
import sys
import re
import subprocess

def read_file(filename):
    with open(filename) as file:
        file_contents = file.read().splitlines()

    names = []
    exec_flags = []

    for item in file_contents:
        if re.match('^Name=', item):
            item = item.replace('Name=', '')
            names.append(item)

        if re.match('^Exec=', item):
            item = item.replace('Exec=', '') \
                       .replace('%u', '') \
                       .replace('%U', '') \
                       .replace('%f', '') \
                       .replace('%F', '') \
                       .strip()
            exec_flags.append(item)

    if not names or not exec_flags:
        return None

    return {
        'names': names,
        'exec_flags': exec_flags
    }

def load_files(application_dir, filenames):
    names = []
    exec_flags = []

    for filename in filenames:
        file_contents = read_file(application_dir + filename)

        if file_contents != None:
            for item in file_contents['names']:
                if item != '':
                    names.append(item)

            for item in file_contents['exec_flags']:
                if item != '':
                    exec_flags.append(item)

    return {
        'names': names,
        'exec_flags': exec_flags
    }

application_dir = '/usr/share/applications/'

file_contents = load_files(application_dir, os.listdir(application_dir))

list_of_choices = '\n'.join(file_contents['names'])

sys.argv.pop(0)
dmenu_arguments = ' '.join(sys.argv)
dmenu_selections = ('printf "{}" | dmenu ' + dmenu_arguments).format(list_of_choices)

choice_buffer = subprocess.check_output(dmenu_selections, shell=True)
choice = str(choice_buffer, 'utf-8').strip()

try:
    choice_index = file_contents['names'].index(choice)

    process_to_execute = file_contents['exec_flags'][choice_index]

    subprocess.call(process_to_execute, shell=True)

    sys.exit(0)
except ValueError:
    sys.exit(1)
