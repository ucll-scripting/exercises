# Write your code here
"""# Assignment

Write a function `generate_git_script(id)` that generates the following string:

```bash
if [ ! -d id ]; then
    git clone https://github.com/id/project id
else
    (cd id; git pull)
fi
```

where all four occurrence of `id` are replaced by the argument.

We don't provide a JavaScript version: this exercise relies on functionality
that is not readily available in JavaScript."""
from textwrap import dedent
def generate_git_script(id):
    string = f'''
    if [ ! -d {id} ]; then
        git clone https://github.com/{id}/project {id}
    else
        (cd {id}; git pull)
    fi'''
    return dedent(string).strip()



