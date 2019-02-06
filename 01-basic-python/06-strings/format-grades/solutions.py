def format_grades(grades):
    return "\n".join( f"{student}: {grade}" for student, grade in grades )