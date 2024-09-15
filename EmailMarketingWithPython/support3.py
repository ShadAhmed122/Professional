import pandas as pd
df = pd.read_excel('converted.xlsx')
column_data = df['tasnia203@gmail.com'].tolist()
# column_data.remove()
a=['','asdsad']
try:
    column_data.remove('')
except:
    pass
# Print the array (list) of values
print(column_data[1])
print(type(column_data[0]))
n=len(column_data)
for i in column_data:
    print(i)

print(type(a))
print(n)
# print(column_data)


