from app import create_app
from app.extensions import db
from app.models import User, Address, Geo, Company 

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()
    print("✅ Dropped and recreated all tables.")
