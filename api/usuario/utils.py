

import json
from db.db import session
from sqlalchemy import select
from db.models import usuario,asigaccesos
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

def get_usuarioselect():
    result = session.execute("select * from tb_seg_asigaccesos inner join tb_seg_usuario on tb_seg_asigaccesos.id_usuario = tb_seg_usuario.id_usuario ")

    # If no rows were returned in the result, return an empty list
    if result.returns_rows == False:
        response = []

    # Convert the response to a plain list of dicts
    else:
        response = [dict(row) for row in result]

    # Output the query result as JSON
    # print(json.dumps(response))
    return response
    # # result = session.query(usuario).join(asigaccesos, usuario.id_usuario==asigaccesos.id_usuario)
    # query = (
    #     session.query(usuario).join(asigaccesos, usuario.id_usuario==asigaccesos.id_usuario).all()
    # )
    # data_usuario = []
    # data = dict()
    # for i in query:
       
    #     data["id_usuario"] = int(data["id_usuario"]) 
    #     data_usuario.append(data)
    # return data_usuario

    


 
    # print("My Join Query: ",str(json.dumps(result)))
    # for _a in result.all():
    #     print (_a.id_usuario, _a.nombre)
    # response = []
    # response = [dict(row.items()) for row in result]
    
    # print ("My Join Querysss: ",json.dumps(response))
    # # if result:
    # #     response = []

    # # # Convert the response to a plain list of dicts
    # # else:
    # #     response = [dict(row.items()) for row in result]

    # # Output the query result as JSON
    # return (json.dumps(response))


def get_usuario():
    query = session.query(
		usuario.id_usuario,
		usuario.nombre,
		usuario.usuario,
		usuario.contrasena,
		usuario.fecha_creacion,
		usuario.estado,

    ).all()
    data_usuario = []
    for i in query:
        data = dict(i)
        data["id_usuario"] = int(data["id_usuario"]) 
        data_usuario.append(data)
    return data_usuario

def update_usuario(id_usuario, data):
    try:
        data_usuario = usuario(**data)
        session.query(usuario).filter(
            usuario.id_usuario== data_usuario.id_usuario
        ).update(data)
        session.commit()
    except Exception as e:
        session.rollback()
        raise Exception("Error al actualizar el registro")
    data_usuario= validate_usuario(int(data_usuario.id_usuario))
    return format_usuario(data_usuario)


def create_usuario(data):
    usuario_data = usuario(**data)
    data_usuario = generic_post(usuario_data)
    return data_usuario

def validate_usuario(id_usuario: int):
    data_usuario = (
        session.query(usuario).filter(usuario.id_usuario == id_usuario).first()
    )
    return data_usuario

def format_usuario(usuario):
    usuario = usuario.__dict__
    usuario.pop("_sa_instance_state")
    usuario["id_usuario"] = int(usuario["id_usuario"]) 
    return usuario

