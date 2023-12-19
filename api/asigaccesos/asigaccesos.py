
from flask import Blueprint, jsonify, request 

from api.asigaccesos.utils import format_asigaccesos
from api.asigaccesos.utils import update_asigaccesos
from api.asigaccesos.utils import create_asigaccesos
from api.asigaccesos.utils import get_asigaccesos, validate_asigaccesos

from api.asigaccesos.validate_asigaccesos import asigaccesosCreate ,  asigaccesosUpdate

api_asigaccesos = Blueprint("Api asigaccesos", __name__, url_prefix="/api/asigaccesos")

@api_asigaccesos.route("/", methods=["GET"])
def getAllasigaccesos():
    """
    Get all asigaccesos
    """
    asigaccesos = get_asigaccesos()
    return {
		"message": " asigaccesos consulta exitosamente",
        "status": 1,
        "data": asigaccesos,
    }

@api_asigaccesos.route("/", methods=["POST"])
def createasigaccesos():
    """
    Create asigaccesos
    """
    try:
        asigaccesos_validate = asigaccesosCreate(**request.json)
    except Exception as e:
        return jsonify({"errors": e.errors()}), 400
    data_asigaccesos = validate_asigaccesos(asigaccesos_validate.id_asigaccesos)
    if data_asigaccesos:
        return jsonify({"errors": "Ya existe un registro con este id"}), 400
    data_asigaccesos = create_asigaccesos(asigaccesos_validate.dict(exclude_unset=True))
    return {
				"message": "asigaccesos creada exitosamente",
				"status": 1,
				"data": {
                    "id_asigaccesos": int(data_asigaccesos.id_asigaccesos),
                }
				
			}

@api_asigaccesos.route("/", methods=["PUT"])
def updateasigaccesos():
    """
    Update asigaccesos
    """
    try:
        asigaccesos_validate = asigaccesosUpdate(**request.json)
    except Exception as e:
        return jsonify({"errors": e.errors()}), 400
    data_asigaccesos = validate_asigaccesos(int(asigaccesos_validate.id_asigaccesos))
    if not data_asigaccesos:
        return jsonify({"errors": "Ya existe un registro con este id"}), 400
    asigaccesos_update = asigaccesos_validate.dict(exclude_unset=True)
    if not asigaccesos_update:
        return jsonify({"errors": "No hay datos para actualizar"}), 400
    data_asigaccesos = update_asigaccesos(int(asigaccesos_validate.id_asigaccesos), asigaccesos_update)
    return {
       
        "message": "asigaccesos actualizado exitosamente",
        "status": 1,
        "data": data_asigaccesos,
    }



@api_asigaccesos.route("/<int:id_asigaccesos>", methods=["GET"]) 
def get_only_asigaccesos(id_asigaccesos: str):
    """
    Create asigaccesos
    """
    data_asigaccesos = validate_asigaccesos(id_asigaccesos)
    if not data_asigaccesos:
        return jsonify({"errors": "No existe un registro con este id"}), 400
    
    data_asigaccesos= format_asigaccesos(data_asigaccesos)
    return {
            "message": "asigaccesos consulta exitosamente",
            "status": 1,
            "data": data_asigaccesos,
        }
