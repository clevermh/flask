
from flask import Blueprint, jsonify, request 

from api.asigroles.utils import format_asigroles
from api.asigroles.utils import update_asigroles
from api.asigroles.utils import create_asigroles
from api.asigroles.utils import get_asigroles, validate_asigroles

from api.asigroles.validate_asigroles import asigrolesCreate ,  asigrolesUpdate

api_asigroles = Blueprint("Api asigroles", __name__, url_prefix="/api/asigroles")

@api_asigroles.route("/", methods=["GET"])
def getAllasigroles():
    """
    Get all asigroles
    """
    asigroles = get_asigroles()
    return {
		"message": " asigroles consulta exitosamente",
        "status": 1,
        "data": asigroles,
    }

@api_asigroles.route("/", methods=["POST"])
def createasigroles():
    """
    Create asigroles
    """
    try:
        asigroles_validate = asigrolesCreate(**request.json)
    except Exception as e:
        return jsonify({"errors": e.errors()}), 400
    data_asigroles = validate_asigroles(asigroles_validate.id_asigroles)
    if data_asigroles:
        return jsonify({"errors": "Ya existe un registro con este id"}), 400
    data_asigroles = create_asigroles(asigroles_validate.dict(exclude_unset=True))
    return {
				"message": "asigroles creada exitosamente",
				"status": 1,
				"data": {
                    "id_asigroles": int(data_asigroles.id_asigroles),
                }
				
			}

@api_asigroles.route("/", methods=["PUT"])
def updateasigroles():
    """
    Update asigroles
    """
    try:
        asigroles_validate = asigrolesUpdate(**request.json)
    except Exception as e:
        return jsonify({"errors": e.errors()}), 400
    data_asigroles = validate_asigroles(int(asigroles_validate.id_asigroles))
    if not data_asigroles:
        return jsonify({"errors": "Ya existe un registro con este id"}), 400
    asigroles_update = asigroles_validate.dict(exclude_unset=True)
    if not asigroles_update:
        return jsonify({"errors": "No hay datos para actualizar"}), 400
    data_asigroles = update_asigroles(int(asigroles_validate.id_asigroles), asigroles_update)
    return {
       
        "message": "asigroles actualizado exitosamente",
        "status": 1,
        "data": data_asigroles,
    }



@api_asigroles.route("/<int:id_asigroles>", methods=["GET"]) 
def get_only_asigroles(id_asigroles: str):
    """
    Create asigroles
    """
    asigroles = validate_asigroles(id_asigroles)
    if not asigroles:
        return jsonify({"errors": "No existe un registro con este id"}), 400
    
    asigroles_db= format_asigroles(asigroles)
    return {
            "message": "asigroles consulta exitosamente",
            "status": 1,
            "data": asigroles_db,
        }
