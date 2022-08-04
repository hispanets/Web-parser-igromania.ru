import csv


# Saving list to csv file
# data - list to save
# file_name - path to save
# format_access - 'a' - append or 'w' - write
def save_file(data, file_name, format_access='w'):
    with open(file_name, format_access, newline='') as f:
        wrt = csv.writer(f, delimiter=';')
        if format_access == 'w':
            wrt.writerow(['Title', 'Subtitle', 'Date', 'Author', 'Section'])
        for item in data:
            wrt.writerow([item['title'], item['subtitle'], item['date'], item['author'], item['section']])

