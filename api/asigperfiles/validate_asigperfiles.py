
from pydantic import BaseModel
from typing import Optional

class asigperfilesCreate(BaseModel):
		id_asigperfiles:	Optional[int] = None
		id_perfiles:	Optional[int] = None
		id_funcionalidad:	Optional[int] = None
		fecha_creacion:	Optional[str] = None
		estado:	Optional[int] = None
  


class asigperfilesUpdate(BaseModel):
		id_asigperfiles:	Optional[int] = None
		id_perfiles:	Optional[int] = None
		id_funcionalidad:	Optional[int] = None
		fecha_creacion:	Optional[str] = None
		estado:	Optional[int] = None
 
