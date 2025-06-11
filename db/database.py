from sqlalchemy import create_engine


#variable cadena de conexion:
MARIADB_URL= 'mysql+pymysql://root:admin@localhost:3315/Evidencia_BD_Emprendly'

#crear el objeto de conexion la base de datos
engine= create_engine(MARIADB_URL) 


