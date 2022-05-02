
with open("input.txt", "r") as f:
    with open("output.txt", "w") as g:
        for id in f:
            id = id.strip()	
            email = f"{id.lower()}@student.ucll.be" if id[0].lower() == 's' or id[0].lower() == 'r' else f"{id.lower()}@ucll.be"
            g.write(f"{email}\n")