import json


class Book:
    def __init__(self, title, year, author, genre, cost, potential_price):
        self.title = title
        self.year = year
        self.author = author
        self.genre = genre
        self.cost = cost
        self.potential_price = potential_price

    def to_dict(self):
        return {
            'title': self.title,
            'year': self.year,
            'author': self.author,
            'genre': self.genre,
            'cost': self.cost,
            'potential_price': self.potential_price
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data['title'], data['year'], data['author'], data['genre'], data['cost'], data['potential_price'])

    def __str__(self):
        return f'Title - {self.title}, Year - {self.year}, Author - {self.author}, Genre - {self.genre}, Cost - {self.cost}, Potential price - {self.potential_price}'
    

class Employee:
    def __init__(self, name, position, phone, email):
        self.name = name
        self.position = position
        self.phone = phone
        self.email = email

    def to_dict(self):
        return {
            'name': self.name,
            'position': self.position,
            'phone': self.phone,
            'email': self.email
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data['name'], data['position'], data['phone'], data['email'])

    def __str__(self):
        return f'Name - {self.name}, Position - {self.position}, Phone - {self.phone}, Email - {self.email}'
    

class Sale:
    def __init__(self, employee, book, sale_date, actual_price):
        self.employee = employee
        self.book = book
        self.sale_date = sale_date
        self.actual_price = actual_price

    def to_dict(self):
        return {
            'employee': self.employee.to_dict(),
            'book': self.book.to_dict(),
            'sale_date': self.sale_date,
            'actual_price': self.actual_price
        }

    @classmethod
    def from_dict(cls, data):
        return cls(Employee.from_dict(data['employee']), Book.from_dict(data['book']), data['sale_date'], data['actual_price'])

    def __str__(self):
        return f'Employee - {self.employee}, Book - {self.book}, Sale date - {self.sale_date}, Actual price - {self.actual_price}'
    

class Store:
    def __init__(self):
        self.books = []
        self.employees = []
        self.sales = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, employee):
        self.employees = [e for e in self.employees if e.name != employee.name]

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books = [b for b in self.books if b.title != book.title]

    def add_sale(self, sale):
        self.sales.append(sale)

    def remove_sale(self, sale):
        self.sales = [s for s in self.sales if not (s.employee.name == sale.employee.name and s.book.title == sale.book.title and s.sale_date == sale.sale_date)]

    def get_employees(self):
        return '\n'.join(str(i) for i in self.employees)

    def get_books(self):
        return '\n'.join(str(i) for i in self.books)

    def get_sales(self):
        return '\n'.join(str(i) for i in self.sales)

    def to_dict(self):
        return {
            'employees': [employee.to_dict() for employee in self.employees],
            'books': [book.to_dict() for book in self.books],
            'sales': [sale.to_dict() for sale in self.sales]
        }

    @classmethod
    def from_dict(cls, data):
        store = cls()
        store.employees = [Employee.from_dict(emp) for emp in data['employees']]
        store.books = [Book.from_dict(book) for book in data['books']]
        store.sales = [Sale.from_dict(sale) for sale in data['sales']]
        return store

    def __str__(self):
        return f'Employees - {self.get_employees()}, Books - {self.get_books()}, Sales - {self.get_sales()}'

    def get_sales_by_date(self, date):
        return [str(sale) for sale in self.sales if sale.sale_date == date]
    
    def get_sales_by_period(self, start_date, end_date):
        return [sale for sale in self.sales if start_date <= sale.sale_date <= end_date]

    def get_sales_by_employee(self, employee_name):
        return [sale for sale in self.sales if sale.employee.name == employee_name]

    def get_bestsellers(self, start_date, end_date):
        sales_by_period = self.get_sales_by_period(start_date, end_date)
        bestsellers = {}
        for sale in sales_by_period:
            if sale.book.title in bestsellers:
                bestsellers[sale.book.title] += 1
            else:
                bestsellers[sale.book.title] = 1
        return bestsellers

    def get_top_employee(self, start_date, end_date):
        sales_by_period = self.get_sales_by_period(start_date, end_date)
        top_employees = {}
        for sale in sales_by_period:
            if sale.employee.name in top_employees:
                top_employees[sale.employee.name] += 1
            else:
                top_employees[sale.employee.name] = 1
        return max(top_employees.items(), key=lambda x: x[1])

    def get_total_profit(self, start_date, end_date):
        total_profit = 0
        for sale in self.get_sales_by_period(start_date, end_date):
            total_profit += sale.actual_price - sale.book.cost
        return total_profit

    def get_top_author(self, start_date, end_date):
        sales_by_period = self.get_sales_by_period(start_date, end_date)
        top_authors = {}
        for sale in sales_by_period:
            if sale.book.author in top_authors:
                top_authors[sale.book.author] += 1
            else:
                top_authors[sale.book.author] = 1
        return max(top_authors.items(), key=lambda x: x[1])

    def get_top_genre(self, start_date, end_date):
        sales_by_period = self.get_sales_by_period(start_date, end_date)
        top_genres = {}
        for sale in sales_by_period:
            if sale.book.genre in top_genres:
                top_genres[sale.book.genre] += 1
            else:
                top_genres[sale.book.genre] = 1
        return max(top_genres.items(), key=lambda x: x[1])
    

def save_data(store, filename):
    try:
        with open(filename, 'w') as f:
            json.dump(store.to_dict(), f)
        print(f'Data was successfully saved to {filename}')
    except Exception as e:
        print(str(e))


def load_data(filename):
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
        store = Store.from_dict(data)
        print(f'Data was successfully loaded from {filename}')
        return store
    except Exception as e:
        print(str(e))
        return None


class Menu:
    def __init__(self, store):
        self.store = store

    @staticmethod
    def display_menu():
        print('1. Add employee')
        print('2. Remove employee')
        print('3. Add book')
        print('4. Remove book')
        print('5. Add sale')
        print('6. Remove sale')
        print('7. View all employees')
        print('8. View all books')
        print('9. View all sales')
        print('10. View sales by date')
        print('11. View sales by period')
        print('12. View sales by employee')
        print('13. View bestsellers')
        print('14. View top employee')
        print('15. View total profit')
        print('16. View top author')
        print('17. View top genre')
        print('18. Save data')
        print('19. Load data')
        print('20. Exit')

    def __add_employee(self):
        name = input('Enter Employee\'s name: ')
        position = input('Enter Employee\'s position: ')
        phone = input('Enter Employee\'s phone: ')
        email = input('Enter Employee\'s email: ')
        employee = Employee(name, position, phone, email)
        self.store.add_employee(employee)
        print(f'Employee "{name}" was successfully added')

    def __remove_employee(self):
        name = input('Enter Employee\'s name you want to delete: ')
        employee = next((e for e in self.store.employees if e.name == name), None)
        if employee:
            self.store.remove_employee(employee)
            print(f'Employee "{name}" was successfully deleted')
        else:
            print(f'Employee "{name}" not found')

    def __add_book(self):
        title = input('Enter Book\'s title: ')
        year = input('Enter Book\'s year: ')
        author = input('Enter Book\'s author: ')
        genre = input('Enter Book\'s genre: ')
        cost = float(input('Enter Book\'s cost: '))
        potential_price = float(input('Enter Book\'s potential price: '))
        book = Book(title, year, author, genre, cost, potential_price)
        self.store.add_book(book)
        print(f'Book "{title}" was successfully added')

    def __remove_book(self):
        title = input('Enter Book\'s title you want to delete: ')
        book = next((b for b in self.store.books if b.title == title), None)
        if book:
            self.store.remove_book(book)
            print(f'Book "{title}" was successfully deleted')
        else:
            print(f'Book "{title}" not found')

    def __add_sale(self):
        employee_name = input('Enter Employee\'s name: ')
        book_title = input('Enter Book\'s title: ')
        sale_date = input('Enter Sale\'s date: ')
        actual_price = float(input('Enter Sale\'s actual price: '))
        employee = next((e for e in self.store.employees if e.name == employee_name), None)
        book = next((b for b in self.store.books if b.title == book_title), None)
        if employee and book:
            sale = Sale(employee, book, sale_date, actual_price)
            self.store.add_sale(sale)
            print('Sale was successfully added')
        else:
            print('Employee or Book not found')

    def __remove_sale(self):
        employee_name = input('Enter Employee\'s name: ')
        book_title = input('Enter Book\'s title: ')
        sale_date = input('Enter Sale\'s date: ')
        employee = next((e for e in self.store.employees if e.name == employee_name), None)
        book = next((b for b in self.store.books if b.title == book_title), None)
        if employee and book:
            sale = next((s for s in self.store.sales if s.employee == employee and s.book == book and s.sale_date == sale_date), None)
            if sale:
                self.store.remove_sale(sale)
                print('Sale was successfully deleted')
            else:
                print('Sale not found')
        else:
            print('Employee or Book not found')