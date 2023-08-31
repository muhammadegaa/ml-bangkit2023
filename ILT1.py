# Define variables
numCopies = 25
bookPrice = 12.99
bookTitle = "The Great Gatsby"
inStock = True

# Perform calculations using arithmetic operators
totalCopies = numCopies * 2

# Compare values using comparison operators
if numCopies > 20:
    print("We have a good stock of this book.")

# Combine conditions using logical operators
if inStock and bookPrice < 15:
    print(f"The book '{bookTitle}' is in stock and affordable.")

# Define a function to calculate total price
def calculate_total_price(price, quantity):
    return price * quantity

# Use the function to calculate total cost
totalCost = calculate_total_price(bookPrice, numCopies)
print(f"The total cost for {numCopies} copies of '{bookTitle}' is ${totalCost:.2f}")

# Using lists to store book titles
book_titles = ["The Great Gatsby", "To Kill a Mockingbird"]
for title in book_titles:
    print(f"Book title: {title}")

# Using dictionaries to store book information
book_info = {
    "title": "The Great Gatsby",
    "price": 12.99,
    "in_stock": True
}
print("Book Information:")
print(f"Title: {book_info['title']}")
print(f"Price: ${book_info['price']:.2f}")
print(f"In Stock: {book_info['in_stock']}")

# Example of a loop with break and continue
while numCopies > 0:
    if numCopies == 10:
        print("Running low on copies. Need to reorder.")
        break
    elif not inStock:
        print("Book is out of stock. Skipping...")
        continue
    print(f"Processing {numCopies} copies...")
    numCopies -= 1
