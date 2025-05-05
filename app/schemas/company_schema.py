from marshmallow import Schema, fields

class CompanySchema(Schema):
    name = fields.String(required=True)
    catchPhrase = fields.String(required=True)
    bs = fields.String(required=True)
