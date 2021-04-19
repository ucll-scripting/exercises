# Explanations

First, run `run-server.sh`:

```bash
$ source run-server.sh
```

This sets up a website locally, which you can visit in your browser at `http://127.0.0.1:5000/index.html`.
If the run-server.sh gives ModuleNotFoundError: No module named 'flask', make sure flask is installed.
`pip install flask` should do the trick.

The website consists of many different html pages that are randomly generated.
The goal of this exercise is to write a script that starts at `index.html`, collects all links to other pages (`<a href="url">`), downloads these other pages, looks for links there, etc. thus visiting the entire site.

It suffices to print the names of all html pages in alphabetic order.
Run `solution.py` as an example.
