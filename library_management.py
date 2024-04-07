'''
Title: Library Management System
Desc: Creating a library management system. Represents books,
customers and library. Able to add/remove books, lend and return
books to customers, track overdue books
'''

#Book data
class Book:
    def __init__(self, title, author, pub_date, isbn, num_copies):
        self.title = title
        self.author = author
        self.pub_date = pub_date
        self.isbn = isbn
        self.num_copies = num_copies

#Customer data
class Customer:
    def __init__(self, name, address, phone_num, email):
        self.name = name
        self.address = address
        self.phone_num = phone_num
        self.email = email
        self.books_borrowed = []

#Library details
