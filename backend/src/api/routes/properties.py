from ..schemas.property import PropertyCreate, PropertyUpdate

def create_property(db, data: PropertyCreate):
    return db.create_property(data.dict())

def update_property(db, property_id: str, data: PropertyUpdate):
    return db.update_property(property_id, data.dict(exclude_none=True))
