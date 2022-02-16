from zipfile import ZipFile
import random
import os

N = 100
FILES = [ 'file-a', 'file-b', 'file-c' ]

rnd = random.Random(4231)



def create_zipfile(filename):
    with ZipFile(filename, 'w') as file:
        for f in FILES:
            if rnd.randint(1, 6) != 1:
                file.writestr(f, "contents")

        if rnd.randint(1, 10) == 1:
            file.writestr(f"redundant{str(rnd.randint(1, 1000))}", "blah")


if not os.path.isdir('data'):
    os.mkdir('data')

for i in range(N):
    zipfilename = f'data/sub{str(i).rjust(3, "0")}.zip'
    create_zipfile(zipfilename)
