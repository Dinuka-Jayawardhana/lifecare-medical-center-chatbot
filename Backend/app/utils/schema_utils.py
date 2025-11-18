from app.models import *

def get_schema_description():
    models = [Patient, Doctor, Appointment, Test]
    schema_desc = ""
    for model in models:
        table_name = model.__tablename__
        columns = ", ".join(c.name for c in model.__table__.columns)
        schema_desc += f"- {table_name}: {columns}\n"
    return schema_desc

schema_info = get_schema_description()