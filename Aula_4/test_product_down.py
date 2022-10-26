from Entities.Product import Product


def test_product_down():
    #Arrange
    product = Product(1, "Milk", 8.50, 25)

    #Act
    product.down_stock(5)

    #Assert
    assert product.stock == 20



