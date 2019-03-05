def format_grades(grades):
    def avg(ns):
        return round(sum(ns) / len(ns))

    return "\n".join( f'{name}: {avg(grades)}' for name, grades in grades.items() )