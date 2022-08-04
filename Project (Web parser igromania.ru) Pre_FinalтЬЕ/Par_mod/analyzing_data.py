import pandas as pd


# Reading csv file with pandas
# path - path to file
# returns DataFrame
def read_file(path):
    return pd.read_csv(path, delimiter=';')


# Analyzing series: section (finding number of each section, min and max values)
# path - path to csv file
# Returns DataFrame(Series) of sections to plotting
def analyze_by_section(path):
    df = read_file(path)
    df_section = df['Section'].value_counts()

    df_section_max = df_section[:1]
    df_section_min = df_section[-1:]

    return df_section


# Analyzing series: author (finding number of articles written by each author, min and max values)
# path - path to csv file
# Returns DataFrame(Series) of authors to plotting
def analyze_by_author(path):
    df = read_file(path)
    df_author = df['Author'].value_counts()

    df_author_max = df_author[:1]
    df_author_min = df_author[-1:]

    return df_author
