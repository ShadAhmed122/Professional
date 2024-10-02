import openpyxl
from datetime import datetime

# Create a new workbook
workbook = openpyxl.Workbook()

# Get the current date and format it as "dd-mm-yyyy" (since "/" is invalid in Excel sheet names)




# Select the active sheet
sheet = workbook.active

# Rename the sheet with the corrected date string (using "-" instead of "/")
sheet.title = "ConvertedOn_" +datetime.now().strftime("%d-%m-%Y")

# Sample data to write into Excel (2D list, each sublist represents a row)
data = [
    ['Invoice No.', 'Item Name','Sales Description','Selling Price','Discount', 
     'Shipping Charge', 'Final Invoice Price', 'Product Type', 'Sales Account', 'Order No.'],
]

# Write data into the sheet by iterating through rows and columns
for row_num, row_data in enumerate(data, start=1):  # start=1 to write from the first row
    for col_num, value in enumerate(row_data, start=1):  # start=1 to write from the first column (A)
        sheet.cell(row=row_num, column=col_num).value = value

# Save the workbook with the desired filename
workbook.save('new_excel_file.xlsx')

print("Excel file created successfully!")
