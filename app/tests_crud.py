import unittest
from unittest.mock import MagicMock 
from sqlalchemy.orm import Session
import models, schemas
from crud import get_products, create_cart_product, update_product, get_product, delete_product, get_cart, get_carts, create_cart, Response, status

class Case1(unittest.TestCase):

    db = MagicMock(spec=Session)


    def test_get_products(self):
        self.db.query.return_value.offset.return_value.limit.return_value.all.return_value = [1, 2, 3]

        res = get_products(self.db)

        self.assertEqual(res, [1, 2, 3], "F")


    def test_create_cart_product(self):
        product = schemas.ProductCreate(title="Prueba", price=10.0, description="ga", category="Prod", image="1001", rating="10")
        db_product = models.Product(**product.dict(), owner_id=1)
        
        res = create_cart_product(self.db, product, 1)

        self.assertEqual(res.title, db_product.title, "F")


    def test_update_product(self):
        product = schemas.UpdateProduct(title="Prueba", price=10.0, description="ga", category="Prod", image="1001", rating="10", id=1)

        self.db.query.return_value.filter.return_value.first.return_value = 100

        res = update_product(1, product, self.db)

        self.assertEqual(res, 100, "F")

    def test_get_product(self):
        self.db.query.return_value.filter.return_value.first.return_value = 10

        res = get_product(self.db, 1)

        self.assertEqual(res, 10, "F")

    def test_delete_product(self):
        self.db.query.return_value.filter.return_value.first.return_value = 100
        assertion = Response(status_code=status.HTTP_204_NO_CONTENT)

        res = delete_product(1, self.db)

        self.assertEqual(res.status_code, assertion.status_code, "F")

    def test_get_cart(self):
        self.db.query.return_value.filter.return_value.first.return_value = 15

        res = get_cart(self.db, 10)

        self.assertEqual(res, 15, "F")
    
    def test_get_carts(self):
        self.db.query.return_value.offset.return_value.limit.return_value.all.return_value = [1, 2, 3]

        res = get_carts(self.db)

        self.assertEqual(res, [1, 2, 3], "F")
        
    def test_create_cart(self):
        cart = schemas.CartCreate(id=1)

        res = create_cart(self.db, cart)

        self.assertEqual(res.id, cart.id, "F")


if __name__== "__main__":
    unittest.main()