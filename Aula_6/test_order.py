from User_interface import UserInterface
from datetime import date 
from entities.book import Book
from entities.customer import Customer
from entities.order import Order
from repositories.book_repository import BookRepository
from repositories.customer_repository import CustomerRepository
from repositories.order_repository import OrderRepository

def test_order():
    #Arrange
    customer_1 = Customer(0,"Ian")
    order_1 = Order(0,customer_1,date.today())
    order_repository = OrderRepository()
    order_repository.add_order(order_1)
    #Act
    #Assert