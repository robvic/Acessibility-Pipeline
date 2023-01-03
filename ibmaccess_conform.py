import openpyxl as oxl

# Open sheet
filename = 'Accessibility_Report-G1 - O portal de notícias da Globo.xlsx'
wb = oxl.load_workbook(filename)
sheet = wb['Issues']

# Find columns
select_columns = ['Page URL', 'Issue Type', 'Checkpoint', 'Issue', 'Xpath']

# Get values from columns
selected_names = []
for row in sheet.iter_rows():
    row_values = []
    for col in select_columns:
        row_values.append(row[col].value)
    selected_names.append(row_values)
