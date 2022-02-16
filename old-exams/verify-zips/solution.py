from zipfile import ZipFile

FILES = [ 'file-a', 'file-b', 'file-c' ]


for i in range(1, 100):
    filename = f'sub{str(i).rjust(3, "0")}.zip'
    with ZipFile(f'data/{filename}') as file:
        contents = file.namelist()
        if len(contents) != 3 or not all(f in contents for f in FILES):
            print(filename)