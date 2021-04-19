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
    archive.extractall('.')

print('Cleaning up...')
remove(filename)
