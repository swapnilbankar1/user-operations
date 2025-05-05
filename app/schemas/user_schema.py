from marshmallow import Schema, fields
from .address_schema import AddressSchema
from .company_schema import CompanySchema


class UserSchema(Schema):
    id = fields.Integer()
    name = fields.String(required=True)
    username = fields.String(required=True)
    email = fields.Email(required=True)
    phone = fields.String(required=True)
    website = fields.String(required=True)
    address = fields.Nested(AddressSchema, required=True)
    company = fields.Nested(CompanySchema, required=True)
