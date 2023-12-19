
from pydantic import BaseModel
from typing import Optional

class asigrolesCreate(BaseModel):
		id_asigroles:	Optional[int] = None
		id_rol:	Optional[int] = None
		id_permiso:	Optional[int] = None
		fecha_creacion:	Optional[str] = None
		estado:	Optional[int] = None
  


class asigrolesUpdate(BaseModel):
		id_asigroles:	Optional[int] = None
		id_rol:	Optional[int] = None
		id_permiso:	Optional[int] = None
		fecha_creacion:	Optional[str] = None
		estado:	Optional[int] = None
 
