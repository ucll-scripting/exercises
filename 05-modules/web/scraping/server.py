from flask import Flask
import random

MIN_PAGES = 50
MAX_PAGES = 1000


def generate_random_text(min=5, max=10, spaces=True):
    size = random.randint(min, max)
    alphabet = 'abcdefghijklmnopqrstuvwxyz' + ('    ' if spaces else '')
    return ''.join( random.choice(alphabet) for _ in range(size) )


def generate_random_filename():
    return f"{generate_random_text(min=10, max=10, spaces=False)}.html"


def generate_random_graph():
    names = [ 'index.html' ]
    result = {}

    for _ in range(random.randint(MIN_PAGES, MAX_PAGES)):
        names.append(generate_random_filename())

    for name in names:
        n_links = random.randint(5, 20)
        result[name] = [ random.choice(names) for _ in range(n_links) ]

    return result


def generate_random_page(links):
    body = ''

    for link in links:
        body += f'<p>{generate_random_text(max=1000)}'
        body += f'<a id="{generate_random_text()}" class="{generate_random_text()}" href="{link}">{generate_random_text(min=5,max=20)}</a>'
        body += f'{generate_random_text(max=1000)}</p>'

    return f'''
    <html>
      <body>
        {body}
      </body>
    </html>
    '''

def generate_random_website():
    graph = generate_random_graph()

    for name, links in graph.items():
        graph[name] = generate_random_page(links)

    return graph


website = generate_random_website()

app = Flask(__name__)

@app.route('/')
def index():
    return website['index.html']

@app.route('/<name>')
def page(name):
    return website[name]
