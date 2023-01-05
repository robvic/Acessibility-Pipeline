import openpyxl as oxl
from datetime import date

import bq_ingest as bq

# Open sheet
filename = 'Accessibility_Report-G1 - O portal de notícias da Globo.xlsx'
wb = oxl.load_workbook(filename)
sheet = wb['Issues']

# Find columns
select_columns = ['Page URL', 'Issue type', 'Checkpoint', 'Issue', 'Xpath']
all_column_names = [cell.value for cell in sheet[1]]

# Get values from columns
selected_names = []
for row in sheet.iter_rows():
    row_values = []
    for col in select_columns:
        col_index = all_column_names.index(col)
        row_values.append(row[col_index].value)
    selected_names.append(row_values)
    
day = date.today()
for row in selected_names:
    row.append(day)

bq.insert(selected_names[1:])
print('Done')
