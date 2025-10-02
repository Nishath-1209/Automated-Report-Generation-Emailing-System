from typing import Optional, List, Dict
from src.dao.customer_dao import customer_dao

class CustomerService:
    def __init__(self):
        self.dao = customer_dao

    def add_customer(self, name: str, email: str, phone: str) -> Optional[Dict]:
        return self.dao.add_customer(name, email, phone)

    def update_customer(self, cust_id: int, fields: Dict) -> Optional[Dict]:
        return self.dao.update_customer(cust_id, fields)

    def delete_customer(self, cust_id: int) -> Optional[Dict]:
        return self.dao.delete_customer(cust_id)

    def list_customers(self, limit: int = 100) -> List[Dict]:
        return self.dao.list_customers(limit)

    def get_customer_by_id(self, cust_id: int) -> Optional[Dict]:
        return self.dao.get_customer_by_id(cust_id)

# Singleton instance
customer_service = CustomerService()
