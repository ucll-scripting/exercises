import re

with open('input.txt', 'r') as f:
    with open('output.txt', 'w') as out:
        content = f.readlines()
        for line in content:
            match = re.fullmatch(r'04[56789]\d-\d{2}-\d{2}-\d{2}|\+32-4[56789]\d-\d{2}-\d{2}-\d{2}',line.strip())
            if match:
                out.write(f"{line}")
            
    


    
    
    