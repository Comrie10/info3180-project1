from app import db

class Property(db.Model):
    __tablename__ = 'property_details'

    id = db.Column(db.Integer, primary_key=True)
    property_title = db.Column(db.String(256))
    property_description = db.Column(db.String(256))
    bedrooms = db.Column(db.Integer)
    bathrooms = db.Column(db.Integer)
    property_location = db.Column(db.String(256))
    property_price = db.Column(db.Numeric(10,2))
    type_property = db.Column(db.String(128))

    def __init__(self,property_title, property_description, bedrooms, bathrooms,property_location, property_price, type_property):
        super().__init__()
        self.property_title = property_title
        self.property_description = property_description
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.property_location = property_location
        self.property_price = property_price
        self.type_property = type_property