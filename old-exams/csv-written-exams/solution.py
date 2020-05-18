import csv


with open('exam-schedule.csv') as file:
    with open('output.txt', 'w') as out:
        data = csv.DictReader(file)

        result = {}

        for row in data:
            if row['Ex. Soortx'] == 'S':
                ids = row['Lector'].split('/')

                for id in ids:
                    result[id] = result.get(id, 0) + 1

        result = sorted(result.items(), key=lambda pair: int(pair[0][1:]))

        print("\n".join(f'{id} {v}' for id, v in result), file=out)