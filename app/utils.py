
def compute_age_group(age):
    if age is None:
        return "unknown"
    try:
        age = int(age)
    except Exception:
        return "unknown"

    if age < 18:
        return "child"
    if age < 65:
        return "adult"
    return "senior"
