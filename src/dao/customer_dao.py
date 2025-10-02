from typing import Optional, List, Dict
from src.config import get_supabase

sb = get_supabase()

class CustomerDAO:
    def __init__(self):
        self.sb = sb

    def add_customer(self, name: str, email: str, phone: str) -> Optional[Dict]:
        payload = {"name": name, "email": email, "phone": phone}
        self.sb.table("customers").insert(payload).execute()
        resp = self.sb.table("customers").select("*").eq("email", email).limit(1).execute()
        return resp.data[0] if resp.data else None

    def update_customer(self, cust_id: int, fields: Dict) -> Optional[Dict]:
        self.sb.table("customers").update(fields).eq("customerid", cust_id).execute()
        resp = self.sb.table("customers").select("*").eq("customerid", cust_id).limit(1).execute()
        return resp.data[0] if resp.data else None

    def delete_customer(self, cust_id: int) -> Optional[Dict]:
        resp_before = self.sb.table("customers").select("*").eq("customerid", cust_id).limit(1).execute()
        row = resp_before.data[0] if resp_before.data else None
        self.sb.table("customers").delete().eq("customerid", cust_id).execute()
        return row

    def list_customers(self, limit: int = 100) -> List[Dict]:
        resp = self.sb.table("customers").select("*").order("customerid", desc=False).limit(limit).execute()
        return resp.data or []

    def get_customer_by_id(self, cust_id: int) -> Optional[Dict]:
        resp = self.sb.table("customers").select("*").eq("customerid", cust_id).limit(1).execute()
        return resp.data[0] if resp.data else None

# Singleton instance
customer_dao = CustomerDAO()
