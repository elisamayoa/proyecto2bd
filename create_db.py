
#    Universidad del Valle de Guatemala   Elisa María Samayoa Chávez
#    Bases de Datos                       Carné 20710
#    Proyecto No.2                        19.10.2021


#importar Postgresql

import psycopg2

from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Conexión con postgresql

con = psycopg2.connect("user=postgres password='123'");
con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT);

# Obtener en cursor de la db

cursor          = con.cursor();
name_Database   = "CocaColaRRHH";

 
# Crear base de datos

sqlCreateDatabase = "create database "+name_Database+";"

# Create a table in PostgreSQL database

cursor.execute(sqlCreateDatabase);