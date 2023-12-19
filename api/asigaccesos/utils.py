

from db.db import session
from sqlalchemy import select
from db.models import asigaccesos
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


def get_asigaccesos():
    query = session.query(
		asigaccesos.id_asigaccesos,
		asigaccesos.id_usuario,
		asigaccesos.id_asigperfiles,
		asigaccesos.id_asigroles,
		asigaccesos.fecha_creacion,
		asigaccesos.estado,

    ).all()
    data_asigaccesos = []
    for i in query:
        data = dict(i)
        data["id_asigaccesos"] = int(data["id_asigaccesos"]) 
        data_asigaccesos.append(data)
    return data_asigaccesos

def update_asigaccesos(id_asigaccesos, data):
    try:
        data_asigaccesos = asigaccesos(**data)
        session.query(asigaccesos).filter(
            asigaccesos.id_asigaccesos== data_asigaccesos.id_asigaccesos
        ).update(data)
        session.commit()
    except Exception as e:
        session.rollback()
        raise Exception("Error al actualizar el registro")
    data_asigaccesos= validate_asigaccesos(int(data_asigaccesos.id_asigaccesos))
    return format_asigaccesos(data_asigaccesos)


def create_asigaccesos(data):
    asigaccesos_data = asigaccesos(**data)
    data_asigaccesos = generic_post(asigaccesos_data)
    return data_asigaccesos

def validate_asigaccesos(id_asigaccesos: int):
    data_asigaccesos = (
        session.query(asigaccesos).filter(asigaccesos.id_asigaccesos == id_asigaccesos).first()
    )
    return data_asigaccesos

def format_asigaccesos(asigaccesos):
    asigaccesos = asigaccesos.__dict__
    asigaccesos.pop("_sa_instance_state")
    asigaccesos["id_asigaccesos"] = int(asigaccesos["id_asigaccesos"]) 
    return asigaccesos

