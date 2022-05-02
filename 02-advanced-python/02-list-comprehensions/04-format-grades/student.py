# Write your code here
def format_grades(grades):
    result = ""
    lengte = len(grades) - 1
    index = 0
    
    for x,y in grades.items():
        if index < lengte:
            average = round(sum(y)/len(y))
            result += f'{x}: {average}\n'
            index += 1
        else:
            average = round(sum(y)/len(y))
            result += f'{x}: {average}'
    return result

          
    
