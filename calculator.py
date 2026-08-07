def calculate_cgpa(sgpas):
    """
    Calculates overall CGPA.
    """
    return round(sum(sgpas) / len(sgpas), 2)


def calculate_percentage(cgpa):
    """
    Converts CGPA to Percentage.
    """
    percentage = cgpa*9.5
    return round(percentage, 2)


def highest_sgpa(sgpas):
    """
    Returns highest SGPA.
    """
    return max(sgpas)


def lowest_sgpa(sgpas):
    """
    Returns lowest SGPA.
    """
    return min(sgpas)


def average_sgpa(sgpas):
    """
    Returns average SGPA.
    """
    return round(sum(sgpas) / len(sgpas), 2)