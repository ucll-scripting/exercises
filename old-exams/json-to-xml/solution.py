import json

with open('input.json') as f:
    students = json.load(f)

with open('output.txt', 'w') as out:
    print('<students>', file=out)
    for entry in students:
        id, grades = entry['id'], entry['grades']
        formatted_grades = "".join( f"<grade>{x}</grade>" for x in grades )

        print(f'<student id="{id}"><grades>{formatted_grades}</grades></student>', file=out)
    print('</students>', file=out)