

from db.db import session
from sqlalchemy import select
from db.models import asigperfiles
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


def get_asigperfiles():
    query = session.query(
		asigperfiles.id_asigperfiles,
		asigperfiles.id_perfiles,
		asigperfiles.id_funcionalidad,
		asigperfiles.fecha_creacion,
		asigperfiles.estado,

    ).all()
    data_asigperfiles = []
    for i in query:
        data = dict(i)
        data["id_asigperfiles"] = int(data["id_asigperfiles"]) 
        data_asigperfiles.append(data)
    return data_asigperfiles

def update_asigperfiles(id_asigperfiles, data):
    try:
        data_asigperfiles = asigperfiles(**data)
        session.query(asigperfiles).filter(
            asigperfiles.id_asigperfiles== data_asigperfiles.id_asigperfiles
        ).update(data)
        session.commit()
    except Exception as e:
        session.rollback()
        raise Exception("Error al actualizar el registro")
    data_asigperfiles= validate_asigperfiles(int(data_asigperfiles.id_asigperfiles))
    return format_asigperfiles(data_asigperfiles)


def create_asigperfiles(data):
    asigperfiles_data = asigperfiles(**data)
    data_asigperfiles = generic_post(asigperfiles_data)
    return data_asigperfiles

def validate_asigperfiles(id_asigperfiles: int):
    data_asigperfiles = (
        session.query(asigperfiles).filter(asigperfiles.id_asigperfiles == id_asigperfiles).first()
    )
    return data_asigperfiles

def format_asigperfiles(asigperfiles):
    asigperfiles = asigperfiles.__dict__
    asigperfiles.pop("_sa_instance_state")
    asigperfiles["id_asigperfiles"] = int(asigperfiles["id_asigperfiles"]) 
    return asigperfiles

