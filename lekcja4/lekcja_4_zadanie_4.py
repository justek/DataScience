raw_column_name = " PATIENT_age_YEARS "

standardized_column_name = (
    raw_column_name.strip()
    .lower()
    .replace("_", " ")
    .replace("years", "year")
    .title()
)

print(standardized_column_name)