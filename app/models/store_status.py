from app import db


class StoreStatus(db.Model):
    """
    Define the store status model.
    """

    id = db.Column(db.Integer, primary_key=True)
    store_name = db.Column(db.String(100), unique=True)
    store_status = db.Column(db.String(100))
    business_hours = db.relationship("BusinessHours", backref="store", lazy=True)
    timezone_info = db.relationship("TimezoneInfo", backref="store", lazy=True)
