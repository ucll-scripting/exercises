
import urllib.request
from zipfile import ZipFile


urllib.request.urlretrieve('http://scripting.leone.ucll.be/data/covid.zip', 'covid.zip')


with ZipFile('covid.zip') as file:
    file.extract('covid.json')
