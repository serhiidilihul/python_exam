from bookstore import Book, Employee, Sale, Store, Menu

if __name__ == '__main__':
    bookstore = Store()
    menu = Menu(bookstore)
    employees = [
        Employee('John Doe', 'Manager', '555-0001', 'john.doe@example.com'),
        Employee('Jane Smith', 'Assistant Manager', '555-0002', 'jane.smith@example.com'),
        Employee('Emily Johnson', 'Cashier', '555-0003', 'emily.johnson@example.com'),
        Employee('Michael Brown', 'Stock Clerk', '555-0004', 'michael.brown@example.com'),
        Employee('Sarah Davis', 'Sales Associate', '555-0005', 'sarah.davis@example.com'),
        Employee('David Wilson', 'Customer Service', '555-0006', 'david.wilson@example.com'),
        Employee('Linda Martinez', 'Marketing Specialist', '555-0007', 'linda.martinez@example.com'),
        Employee('James Anderson', 'IT Support', '555-0008', 'james.anderson@example.com'),
        Employee('Patricia Taylor', 'HR Specialist', '555-0009', 'patricia.taylor@example.com'),
        Employee('Robert Thomas', 'Security', '555-0010', 'robert.thomas@example.com'),
        Employee('Jessica Jackson', 'Cashier', '555-0011', 'jessica.jackson@example.com'),
        Employee('Daniel White', 'Sales Associate', '555-0012', 'daniel.white@example.com'),
        Employee('Nancy Harris', 'Stock Clerk', '555-0013', 'nancy.harris@example.com'),
        Employee('Christopher Martin', 'Assistant Manager', '555-0014', 'christopher.martin@example.com'),
        Employee('Barbara Thompson', 'Customer Service', '555-0015', 'barbara.thompson@example.com'),
        Employee('Matthew Garcia', 'Marketing Specialist', '555-0016', 'matthew.garcia@example.com'),
        Employee('Elizabeth Rodriguez', 'IT Support', '555-0017', 'elizabeth.rodriguez@example.com'),
        Employee('Steven Lewis', 'HR Specialist', '555-0018', 'steven.lewis@example.com'),
        Employee('Jennifer Walker', 'Security', '555-0019', 'jennifer.walker@example.com'),
        Employee('Joseph Lee', 'Cashier', '555-0020', 'joseph.lee@example.com')
    ]
    for employee in employees:
        bookstore.add_employee(employee)

    books = [
        Book('To Kill a Mockingbird', 1960, 'Harper Lee', 'Fiction', 10.00, 18.99),
        Book('1984', 1949, 'George Orwell', 'Dystopian', 8.00, 14.99),
        Book('The Great Gatsby', 1925, 'F. Scott Fitzgerald', 'Classic', 12.00, 20.99),
        Book('The Catcher in the Rye', 1951, 'J.D. Salinger', 'Fiction', 9.00, 16.99),
        Book('Pride and Prejudice', 1813, 'Jane Austen', 'Romance', 7.00, 13.99),
        Book('The Hobbit', 1937, 'J.R.R. Tolkien', 'Fantasy', 11.00, 19.99),
        Book('Moby Dick', 1851, 'Herman Melville', 'Adventure', 6.00, 12.99),
        Book('War and Peace', 1869, 'Leo Tolstoy', 'Historical', 14.00, 22.99),
        Book('Crime and Punishment', 1866, 'Fyodor Dostoevsky', 'Psychological', 10.00, 18.99),
        Book('Anna Karenina', 1877, 'Leo Tolstoy', 'Romance', 12.00, 21.99),
        Book('The Brothers Karamazov', 1880, 'Fyodor Dostoevsky', 'Philosophical', 15.00, 24.99),
        Book('Brave New World', 1932, 'Aldous Huxley', 'Dystopian', 8.00, 15.99),
        Book('Jane Eyre', 1847, 'Charlotte Brontë', 'Gothic', 7.00, 14.99),
        Book('Wuthering Heights', 1847, 'Emily Brontë', 'Gothic', 6.00, 13.99),
        Book('The Odyssey', '8th Century BC', 'Homer', 'Epic', 10.00, 19.99),
        Book('The Iliad', '8th Century BC', 'Homer', 'Epic', 9.00, 18.99),
        Book('Great Expectations', 1861, 'Charles Dickens', 'Bildungsroman', 8.00, 16.99),
        Book('Little Women', 1868, 'Louisa May Alcott', 'Bildungsroman', 7.00, 14.99),
        Book('Fahrenheit 451', 1953, 'Ray Bradbury', 'Dystopian', 8.00, 16.99),
        Book('The Book Thief', 2005, 'Markus Zusak', 'Historical', 12.00, 21.99)
    ]

    for book in books:
        bookstore.add_book(book)

    sales = [
        Sale(employees[0], books[0], '2023-01-05', 19.99),
        Sale(employees[0], books[3], '2023-02-20', 16.99),
        Sale(employees[1], books[1], '2023-01-10', 14.99),
        Sale(employees[1], books[7], '2023-04-10', 22.99),
        Sale(employees[2], books[2], '2023-02-15', 20.99),
        Sale(employees[3], books[4], '2023-03-25', 13.99),
        Sale(employees[3], books[5], '2023-03-30', 19.99),
        Sale(employees[4], books[6], '2023-04-05', 12.99),
        Sale(employees[5], books[8], '2023-05-15', 18.99),
        Sale(employees[5], books[9], '2023-05-20', 21.99),
        Sale(employees[6], books[10], '2023-06-25', 24.99),
        Sale(employees[6], books[11], '2023-06-30', 15.99),
        Sale(employees[7], books[12], '2023-07-05', 14.99),
        Sale(employees[7], books[13], '2023-07-10', 13.99),
        Sale(employees[8], books[14], '2023-08-15', 19.99),
        Sale(employees[9], books[15], '2023-08-20', 18.99),
        Sale(employees[10], books[16], '2023-09-25', 16.99),
        Sale(employees[11], books[17], '2023-09-30', 14.99),
        Sale(employees[12], books[18], '2023-10-05', 16.99),
        Sale(employees[13], books[19], '2023-10-10', 20.99)
    ]

    for sale in sales:
        bookstore.add_sale(sale)
    while True:
        Menu.display_menu()
        menu.execute_choice()