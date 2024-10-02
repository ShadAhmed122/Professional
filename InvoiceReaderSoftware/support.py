import re

# New provided strings
a = """NATURO
Help Line: 09639812525
Name: Khaleda Jannati Phone: 8801751998060
Address:  Barguna sador, Barguna
Product Qty Price Total
Chia Seeds 2 Kg 1 Tk 2,900.00 Tk 1,100.00
Garlic Honey 0.5 Kg 1 Tk 700.00 Tk 700.00
Invoice No: NA-088322 Date: 21-09-2024 00:10:59
Sub Total Tk 1,100.00
Shipping Cost Tk 100.00
Discount Tk 50.00
Total Amount Tk 1,200.00
126"""

b = """NATURO
Help Line: 09639812525
Invoice No: NA-088321 Date: 21-09-2024 00:10:49
Name: সােরায়ার έহােসন Phone: 8801911955832
Address:  বাদাঘাট বাজার, έপাѶ অিফস: বাদাঘাট বাজার, থানা/উপেজলা : তািহরপুর, έজলা: সুনামগП।
Product Qty Price Total
Garlic Honey 0.5 Kg 1 Tk 700.00 Tk 700.00
Sub Total Tk 700.00
Shipping Cost Tk 100.00
Discount Tk 150.00
Total Amount Tk 800.00
125"""

c = """NATURO
Help Line: 09639812525
Invoice No: NA-088326
Date: 21-09-2024 00:15:10
Name: শােহদ Phone: 8801625368593
Address:  শািоবাগ শҝামলী আ/এ ৪ নং έরাড মাϒাসা িবΝўং আςাবাদ চСςাম।
Product Qty Price Total
Sundarban Natural Honey 1 Kg 1 Tk 2,100.00 Tk 1,500.00
Garlic Honey 0.5 Kg 2 Tk 700.00 Tk 1,400.00
Sub Total Tk 700.00
Shipping Cost Tk 100.00
Total Amount Tk 800.00
128"""

d = """NATURO
Help Line: 09639812525
Invoice No: NA-088327 
Date: 21-09-2024 00:20:32
Name: G S M RIFAT MAHAMUD Phone: 8801778839288
Address:  Tongi College Gate, Bonmala Road, Digir par
Product Qty Price Total
Sundarban 5 Kg 1 Tk 2,100.00 Tk 1,500.00
Sub Total Tk 1,500.00
Shipping Cost Tk 100.00
Total Amount Tk 1,600.00
129"""

# Function to extract product information
def extract_product_info(text):
    # Updated regex pattern to match various product formats
    product_pattern = re.compile(r"([A-Za-z ]+ [\d.]+ [A-Za-z]+) (\d+) Tk ([\d,]+\.\d{2}) Tk ([\d,]+\.\d{2})")
    
    # Find all products in the string
    products = product_pattern.findall(text)
    
    # Initialize an empty list to store product details
    product_details = []
    
    for product in products:
        product_name = product[0].strip()
        qty = int(product[1].strip())
        price = float(product[2].replace(',', ''))
        total = float(product[3].replace(',', ''))
        
        # Store the details in a dictionary
        product_details.append({
            'Product Name': product_name,
            'Quantity': qty,
            'Price': price,
            'Total': total
        })
    
    # Return the product details and the total number of products
    return product_details, len(products)



# List of all strings
texts = [a, b, c, d]

# Loop through each string and extract product information
for i, text in enumerate(texts):
    product_info, total_products = extract_product_info(text)
    
    print(f"\nDetails for string {chr(97 + i)}:")
    print(f"Total number of products: {total_products}")
    
    # print(product_info)
    
    for a,product in enumerate(product_info):
        print(a)
        print(type(a))
        print(f"Product Name: {product['Product Name']}")
        print(f"Quantity: {product['Quantity']}")
        print(f"Price: {product['Price']}")
        print(f"Total: {product['Total']}\n")
        
