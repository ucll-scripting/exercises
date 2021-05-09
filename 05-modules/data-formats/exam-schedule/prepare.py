from urllib.request import urlretrieve
from zipfile import ZipFile
from os import remove


url = 'http://scripting.leone.ucll.be/data/exam-schedule.zip'


def report(chunk_index, chunk_size, total_size):
    percentage = round(100 * chunk_index * chunk_size / total_size)
    print(f'{percentage}%')


print(f'Downloading {url}')
filename, _ = urlretrieve(url, reporthook=report)

print('Unzipping...')
with ZipFile(filename, 'r') as archive:
    archive_contents = archive.namelist()
    archive.extractall('.')


for archive_file in archive_contents:
    print(f'Converting {archive_file}')
    with open(archive_file, encoding='latin-1') as file:
        contents = file.read()
    with open(archive_file, 'w', encoding='utf-8') as file:
        file.write(contents)


print('Cleaning up...')
remove(filename)
