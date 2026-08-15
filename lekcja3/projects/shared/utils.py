def print_project_info(project_name):
    print(f"Project: {project_name}")


def calculate_missing_percentage(df):
    return df.isnull().mean() * 100