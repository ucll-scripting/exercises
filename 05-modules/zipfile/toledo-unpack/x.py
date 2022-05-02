import sys
from zipfile import ZipFile
import os
from pathlib import Path
import re

filename = sys.argv[1]
root = os.path.abspath(filename)

def path_dir_name(name):
    return f"submissions\{name}"

with ZipFile(root, 'r') as zip:
    txt = [i for i in zip.namelist() if Path(i).suffix == ".txt"]
    otherfiles = [i for i in zip.namelist() if Path(i).suffix != ".txt"]
    student_files = []
    for t in txt:
        tx = [t]
        for o in otherfiles:
            if Path(t).stem == Path(o).stem:
                tx.append(o)
        student_files.append(tuple(tx))
                
    for i in student_files:
        txt , *otherfiles = i
        with zip.open(txt) as text:
            content = text.read().decode('utf-8')
            match = re.fullmatch(r'Naam: (.*) \(.*\)',content)
            m = match.groups()[0]
            m = m.lower()
            firstname , *lastname = m.split(' ')
            lastname = "-".join(lastname)
            m = ('-').join([lastname,firstname])
            path = os.path.join("submissions",m)
            for i in otherfiles:
                zip.extract(member=i,path=path)
        
           
                
          

            

