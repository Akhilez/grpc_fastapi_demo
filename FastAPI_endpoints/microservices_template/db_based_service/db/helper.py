from db.connection import Session
from db.models import BasicModel

def add_to_basicmodel(column_1_value, column_2_value, column_3_value):
    try:
        new_basicmodel_object = BasicModel(column_1=column_1_value, column_2=column_2_value, column_3=column_3_value)
        Session.add(new_basicmodel_object)
        Session.commit()
        return "Sucessfully added"
    except:
        Session.rollback()
        return "Something unexpected happened, rolledback operation"

def update_basicmodel(old_column_1_value, new_column_1_value):
    try:
        ol_baicmodel_object = Session.query(BasicModel).filter_by(column_1=old_column_1_value).first()
        ol_baicmodel_object.column_1 = new_column_1_value
        Session.commit()
        return "Sucessfully updated"
    except:
        Session.rollback()
        return "Something unexpected happened, rolledback operation"

def get_all_basicmodel_entries():
    return Session.query(BasicModel).all()

def delete_from_basicmodel(column_2_value):
    try:
        to_be_deleted_object = Session.query(BasicModel).filter_by(column_2=column_2_value).first()
        Session.delete(to_be_deleted_object)
        return "Succesfully deleted!!"
    except:
        Session.rollback()
        return "Something unexpected happened, rolledback operation"
