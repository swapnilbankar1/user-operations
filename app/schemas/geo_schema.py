from marshmallow import Schema, fields

class GeoSchema(Schema):
    lat = fields.String(required=True)
    lng = fields.String(required=True)
