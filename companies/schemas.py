
from ninja import Schema
from datetime import datetime

class CompanyIn(Schema):
    name: str
    description: str | None = None
    company_contact_number: str

class CompanyOut(Schema):
    id: int
    name: str
    description: str | None = None
    company_contact_number: str