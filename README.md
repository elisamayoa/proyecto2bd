# proyecto2bd
Proyecto No. 2 de Bases de Datos. Diseño e implementación de base de datos para RRHH

La base de datos cocacolarrhh tiene siete tablas: empleado, departamento, puesto, desempeño, candidatos, reconocimientos y permisos. 
 
  →Para crear la base de datos se utilizar el archivo create_db.py, donde se deben *cambiar la información del usuario y la contraseña* para hacer la conexión con postgresql. Se *importa la librería psycopg2.*
  
  →El DDL.sql contiene los queries para la creación de tablas definiendo sus llaves primarias y foráneas
  
  →Para poblar la bd se utiliza el inser_data.py, del cual se deben *importar las librerías random, rstr, faker y psycopg2.*
  *Es importante cambiar la ruta de las imágenes antes de correr el programa*, esto se encuentra a partir de la línea 75 en el código.  
 
 →Las imágenes se pueden visualizar en la columna fotografia de la tabla empleado
 
 →Se puede usar el archivo view_image.py para poder ver cómo se hace la conversión de bytes a imagen
 
 →Los queries realizados de inserción, actualización y eliminación se encuentran en el archivo consultas.sql

