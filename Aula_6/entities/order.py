from datetime import date

from entities.book import Book
from entities.customer import Customer


class Order:
    def __init__(self, id: int, customer: Customer, date_order: date, book:Book) -> None:
        self.id = id
        self.customer = customer
        self.date_order = date_order
        self.purchased_book = book
        self.total_price: book.price
