

from db.db import session
from sqlalchemy import select
from db.models import asigroles
from flask import Blueprint, jsonify, request 
from sqlalchemy.orm import Session

def generic_post(data):
    try:
        session.add(data)
        session.commit()
        session.refresh(data)
    except Exception as e:
       
        session.rollback()
        raise Exception("Error al crear el registro")
    return data


def get_asigroles():
    query = session.query(
		asigroles.id_asigroles,
		asigroles.id_rol,
		asigroles.id_permiso,
		asigroles.fecha_creacion,
		asigroles.estado,

    ).all()
    data_asigroles = []
    for i in query:
        data = dict(i)
        data["id_asigroles"] = int(data["id_asigroles"]) 
        data_asigroles.append(data)
    return data_asigroles

def update_asigroles(id_asigroles, data):
    try:
        data_asigroles = asigroles(**data)
        session.query(asigroles).filter(
            asigroles.id_asigroles== data_asigroles.id_asigroles
        ).update(data)
        session.commit()
    except Exception as e:
        session.rollback()
        raise Exception("Error al actualizar el registro")
    data_asigroles= validate_asigroles(int(data_asigroles.id_asigroles))
    return format_asigroles(data_asigroles)


def create_asigroles(data):
    asigroles_data = asigroles(**data)
    data_asigroles = generic_post(asigroles_data)
    return data_asigroles

def validate_asigroles(id_asigroles: int):
    data_asigroles = (
        session.query(asigroles).filter(asigroles.id_asigroles == id_asigroles).first()
    )
    return data_asigroles

def format_asigroles(asigroles):
    asigroles = asigroles.__dict__
    asigroles.pop("_sa_instance_state")
    asigroles["id_asigroles"] = int(asigroles["id_asigroles"]) 
    return asigroles

