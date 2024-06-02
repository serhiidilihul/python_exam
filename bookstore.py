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