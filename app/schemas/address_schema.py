from marshmallow import Schema, fields
from .geo_schema import GeoSchema

class AddressSchema(Schema):
    street = fields.String(required=True)
    suite = fields.String(required=True)
    city = fields.String(required=True)
    zipcode = fields.String(required=True)
    geo = fields.Nested(GeoSchema, required=True)
