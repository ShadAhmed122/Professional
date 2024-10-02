from datetime import datetime

# Get the current date and time
current_date = datetime.now()

# Convert the date to a string in the "date/month/year" format (e.g., "01/10/2024")
date_string = current_date.strftime("%d/%m/%Y")

# Print the string representation of the current date
print("Current Date as String (dd/mm/yyyy):", date_string)
