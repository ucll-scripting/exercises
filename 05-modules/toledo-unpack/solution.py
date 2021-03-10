from zipfile import ZipFile
import sys
import re
import os


def make_slug(string):
    '''
    Turns name "Firstname Lastname" into "lastname-firstname"
    '''
    parts = string.lower().split(' ')
    fname = parts[0]
    lname = parts[1:]

    return "-".join([ *lname, fname ])


def extract_qid_from_filename(filename):
    match = re.search(r'(q\d{7})', filename)
    if not match:
        print(f'Something unexpected happened - could not find q-id in {filename}')
        sys.exit(-1)
    return match.group(1)


def read_file_from_zipfile(zipfile, filename):
    with zipfile.open(filename) as contents:
        return contents.read().decode('utf-8')


def extract_name_from_file(data):
    match = re.search(r'Naam: (.*) \(q\d{7}\)', data)
    if not match:
        print(f'Could not find student name!')
        sys.exit(-1)
    return match.group(1)


def build_qid_dictionary(zipfile):
    '''
    Creates a dictionary that maps qids to names
    '''
    table = {}
    files_in_zip = zipfile.namelist()
    txt_files_in_zip = [ filename for filename in files_in_zip if filename.endswith('.txt') ]

    for filename in txt_files_in_zip:
        qid = extract_qid_from_filename(filename)
        txt_file_contents = read_file_from_zipfile(zipfile, filename)
        name = extract_name_from_file(txt_file_contents)
        table[qid] = name

    return table



filename = sys.argv[1]

with ZipFile(filename) as zipfile:
    qid_to_name = build_qid_dictionary(zipfile)
    files_in_zip = zipfile.namelist()
    submission_files_in_zip = [ filename for filename in files_in_zip if not filename.endswith('.txt') ]

    for submission_file in submission_files_in_zip:
        qid = extract_qid_from_filename(submission_file)
        name = qid_to_name[qid]
        slug = make_slug(name)
        directory = f"submissions/{slug}"
        os.makedirs(directory, exist_ok=True)
        zipfile.extract(submission_file, directory)
