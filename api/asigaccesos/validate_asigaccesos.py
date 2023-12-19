
from pydantic import BaseModel
from typing import Optional

class asigaccesosCreate(BaseModel):
		id_asigaccesos:	Optional[int] = None
		id_usuario:	Optional[int] = None
		id_asigperfiles:	Optional[int] = None
		id_asigroles:	Optional[int] = None
		fecha_creacion:	Optional[str] = None
		estado:	Optional[int] = None
  


class asigaccesosUpdate(BaseModel):
		id_asigaccesos:	Optional[int] = None
		id_usuario:	Optional[int] = None
		id_asigperfiles:	Optional[int] = None
		id_asigroles:	Optional[int] = None
		fecha_creacion:	Optional[str] = None
		estado:	Optional[int] = None
 
