
from flask import Blueprint, jsonify, request 

from api.asigperfiles.utils import format_asigperfiles
from api.asigperfiles.utils import update_asigperfiles
from api.asigperfiles.utils import create_asigperfiles
from api.asigperfiles.utils import get_asigperfiles, validate_asigperfiles

from api.asigperfiles.validate_asigperfiles import asigperfilesCreate ,  asigperfilesUpdate

api_asigperfiles = Blueprint("Api asigperfiles", __name__, url_prefix="/api/asigperfiles")

@api_asigperfiles.route("/", methods=["GET"])
def getAllasigperfiles():
    """
    Get all asigperfiles
    """
    asigperfiles = get_asigperfiles()
    return {
		"message": " asigperfiles consulta exitosamente",
        "status": 1,
        "data": asigperfiles,
    }

@api_asigperfiles.route("/", methods=["POST"])
def createasigperfiles():
    """
    Create asigperfiles
    """
    try:
        asigperfiles_validate = asigperfilesCreate(**request.json)
    except Exception as e:
        return jsonify({"errors": e.errors()}), 400
    data_asigperfiles = validate_asigperfiles(asigperfiles_validate.id_asigperfiles)
    if data_asigperfiles:
        return jsonify({"errors": "Ya existe un registro con este id"}), 400
    data_asigperfiles = create_asigperfiles(asigperfiles_validate.dict(exclude_unset=True))
    return {
				"message": "asigperfiles creada exitosamente",
				"status": 1,
				"data": {
                    "id_asigperfiles": int(data_asigperfiles.id_asigperfiles),
                }
				
			}

@api_asigperfiles.route("/", methods=["PUT"])
def updateasigperfiles():
    """
    Update asigperfiles
    """
    try:
        asigperfiles_validate = asigperfilesUpdate(**request.json)
    except Exception as e:
        return jsonify({"errors": e.errors()}), 400
    data_asigperfiles = validate_asigperfiles(int(asigperfiles_validate.id_asigperfiles))
    if not data_asigperfiles:
        return jsonify({"errors": "Ya existe un registro con este id"}), 400
    asigperfiles_update = asigperfiles_validate.dict(exclude_unset=True)
    if not asigperfiles_update:
        return jsonify({"errors": "No hay datos para actualizar"}), 400
    data_asigperfiles = update_asigperfiles(int(asigperfiles_validate.id_asigperfiles), asigperfiles_update)
    return {
       
        "message": "asigperfiles actualizado exitosamente",
        "status": 1,
        "data": data_asigperfiles,
    }



@api_asigperfiles.route("/<int:id_asigperfiles>", methods=["GET"]) 
def get_only_asigperfiles(id_asigperfiles: str):
    """
    Create asigperfiles
    """
    asigperfiles = validate_asigperfiles(id_asigperfiles)
    if not asigperfiles:
        return jsonify({"errors": "No existe un registro con este id"}), 400
    
    data_asigperfiles= format_asigperfiles(asigperfiles)
    return {
            "message": "asigperfiles consulta exitosamente",
            "status": 1,
            "data": data_asigperfiles,
        }
