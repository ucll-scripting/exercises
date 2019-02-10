def format_grades(results):
    def avg(ns):
        return round(sum(ns) / len(ns))

    return "\n".join( f'{name}: {avg(grades)}' for name, grades in results.items() )