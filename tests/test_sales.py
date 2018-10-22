import unittest
import json

from endpoints.sales import app


def test_admin_can_get_all_sale_records(self):
    feedback = self.admin.get(
        'StoreManager/api/v1/GetAllSales/'
    )
    self.assertEqual(200, feedback.status_code)


def test_route_get_all_sales_requires_login(self):
    feedback = self.admin.get(
        'StoreManager/api/v1/GetAllSales/', follow_redirects=True)
    self.assertIn(b'Please log in to access this page', feedback.data)


if __name__ == '__main__':
    unittest.main()
