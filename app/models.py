from app import db

class Property(db.Model):
    __tablename__ = 'property_details'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256))
    description = db.Column(db.String(256))
    bedrooms = db.Column(db.Integer)
    bathrooms = db.Column(db.Integer)
    location = db.Column(db.String(256))
    price = db.Column(db.Numeric(10,2))
    property_type = db.Column(db.String(128))
    photo = db.Column(db.String(255), nullable=False)

    def __init__(self,title, description, bedrooms, bathrooms,location, price, property_type, photo):
        super().__init__()
        self.title = title
        self.description = description
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.location = location
        self.price = price
        self.type_property = property_type
        self.photo =photo