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