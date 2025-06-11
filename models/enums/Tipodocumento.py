#enum: Tipo de dato personalizado
#us: restringir variables
# solo a algunos valores 
from enum import Enum

class Tipodocumento(Enum):
    CC = "Cedula Ciudadania"
    TI = "Tarjeta Identidad"
    CE = "Cedula Extranjeria"
    RC = "Registro Civil"