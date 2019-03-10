from zipfile import ZipFile
import sys
import re
import os


def make_slug(string):
    parts = string.lower().split(' ')
    fname = parts[0]
    lname = parts[1:]

    return "-".join([ *lname, fname ])


filename = sys.argv[1]

with ZipFile(filename) as zip:
    filenames = zip.namelist()

    table = {}
    submissions = []

    for filename in filenames:
        match = re.search(r'_(q\d{7})_.*\.txt$', filename)

        if match:
            q_id = match.group(1)

            with zip.open(filename) as contents:
                data = contents.read().decode('utf-8')

            student_name = re.search(r'Naam: (.*) \(q\d{7}\)', data).group(1)
            table[q_id] = make_slug(student_name)
        else:
            submissions.append(filename)

    for submission in submissions:
        match = re.search(r'_(q\d{7})_', submission)
        q_id = match.group(1)
        slug = table[q_id]
        os.makedirs(slug)
        zip.extract(submission, slug)
