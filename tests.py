from bookstore import Store, Book, Employee, Sale


bookstore = Store()

employees = [
    Employee('John Doe', 'Manager', '555-0001', 'john.doe@example.com'),
    Employee('Jane Smith', 'Assistant Manager', '555-0002', 'jane.smith@example.com'),
    Employee('Emily Johnson', 'Cashier', '555-0003', 'emily.johnson@example.com')
]
for employee in employees:
    bookstore.add_employee(employee)

books = [
    Book('To Kill a Mockingbird', 1960, 'Harper Lee', 'Fiction', 10.00, 18.99),
    Book('1984', 1949, 'George Orwell', 'Dystopian', 8.00, 14.99),
    Book('The Great Gatsby', 1925, 'F. Scott Fitzgerald', 'Classic', 12.00, 20.99)
]
for book in books:
    bookstore.add_book(book)

# Add sales
sales = [
    Sale(employees[0], books[0], '2023-01-05', 19.99),
    Sale(employees[1], books[1], '2023-01-10', 14.99),
    Sale(employees[2], books[2], '2023-02-15', 20.99)
]
for sale in sales:
    bookstore.add_sale(sale)

all_sales = bookstore.get_sales()
assert len(all_sales) == 3

sales_by_date = bookstore.get_sales_by_date('2023-01-05', '2023-01-11')
assert len(sales_by_date) == 1

sales_by_period = bookstore.get_sales_by_period('2023-01-01', '2023-01-15')
assert len(sales_by_period) == 2

bestsellers = bookstore.get_bestsellers('2023-01-01', '2023-12-31')
assert len(bestsellers) == 3

total_profit = bookstore.get_total_profit('2023-01-01', '2023-12-31')
assert total_profit == 55.97

top_author = bookstore.get_top_author('2023-01-01', '2023-12-31')
assert top_author[0] == 'Harper Lee'

top_genre = bookstore.get_top_genre('2023-01-01', '2023-12-31')
assert top_genre[0] == 'Fiction'
