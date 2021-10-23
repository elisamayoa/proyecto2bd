#PROGRAMA PARA POBLAR BD
#Elisa Samayoa, 20710

import psycopg2
from faker import Faker
import rstr
import random


try:
    conexion a bd
    connection = psycopg2.connect(user="postgres",
                                  password="123",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="cocacolarrhh")
    cursor = connection.cursor()
    
    #INSERCION TABLA DEPARTAMENTO
    
    insertdep1 = "INSERT INTO departamento VALUES('1', 'Departamento de Producción','Departamento encargado de dirigir y liderar todas las operaciones llevadas a cabo para fabricar productos','B13')"
    insertdep2 = "INSERT INTO departamento VALUES('2', 'Departamento de Marketing', 'Departamento encargado de incrementar el volumen de ventas, la cuota de mercado y los beneficios obtenidos', 'A12')"
    insertdep3 = "INSERT INTO departamento VALUES('3', 'Departamento de Finanzas', 'Departamento encargado de revisar la confiabilidad e integridad de la información financiera', 'B44')"
    insertdep4 = "INSERT INTO departamento VALUES('4', 'Departamento de Recursos Humanos', 'Departamento encargado gestionar programas de reclutamiento, selección, capacitación y desarrollo.', 'C11' )"
    cursor.execute(insertdep1);
    cursor.execute(insertdep2);
    cursor.execute(insertdep3);
    cursor.execute(insertdep4);
    connection.commit()
    
    #INSERCION TABLA PUESTO
    #RECURSOS HUMANOS
    insertpuestos0 = "INSERT INTO puesto VALUES('1', 'Presidente de la Junta Directiva', 8, 6, null, 35000, null)"
    insertpuestos1 = "INSERT INTO puesto VALUES('2', 'Director de Recursos Humanos', 8, 6, '4', 25000, null )"
    insertpuestos2 = "INSERT INTO puesto VALUES('3', 'Técnico de selección de personal', 8, 5, '4', 15000, null )"
    insertpuestos3 = "INSERT INTO puesto VALUES('4', 'Técnico de formación', 8, 5, '4', 10000, null )"
    insertpuestos4 = "INSERT INTO puesto VALUES('5', 'Técnico de comunicación interna', 8, 5, '4', 10000, null )"
    #PRODUCCIÓN
    insertpuestos5 = "INSERT INTO puesto VALUES('6', 'Gerente Industrial', 8, 5, '1', 20000, 'Industria' )"
    insertpuestos6 = "INSERT INTO puesto VALUES('7', 'Operario', 10, 6, '1', 8000, 'Industria' )"
    insertpuestos7 = "INSERT INTO puesto VALUES('8', 'Supervisores', 8, 6, '1', 10000, 'Control de Calidad' )"
    insertpuestos8 = "INSERT INTO puesto VALUES('9', 'Encargado de mantenimiento', 8, 6, '1', 10000, 'Recursos' )"
    #MARKETING
    insertpuestos9  = "INSERT INTO puesto VALUES('10', 'Director de Marketing', 10, 5, '2', 20000, null )"
    insertpuestos10 = "INSERT INTO puesto VALUES('11', 'Publicista', 8, 5, '2', 10000, 'Publicidad' )"
    insertpuestos11 = "INSERT INTO puesto VALUES('12', 'Diseñador', 6, 5, '2', 8000, 'Publicidad' )"
    insertpuestos12 = "INSERT INTO puesto VALUES('13', 'Vendedor', 8, 6, '2', 8000, 'Ventas' )"
    #FINANZAS
    insertpuestos13  = "INSERT INTO puesto VALUES('14', 'Director de Finanzas', 8, 5, '3', 20000, null )"
    insertpuestos14  = "INSERT INTO puesto VALUES('15', 'Auditor', 7, 5, '3', 15000, 'Contabilidad' )"
    insertpuestos15  = "INSERT INTO puesto VALUES('16', 'Asesores', 7, 5, '3', 15000, 'Egresos' )"
    insertpuestos16  = "INSERT INTO puesto VALUES('17', 'Analistas', 8, 5, '3', 15000, 'Ingresos' )"
    
    cursor.execute(insertpuestos0);
    cursor.execute(insertpuestos1);
    cursor.execute(insertpuestos2);
    cursor.execute(insertpuestos3);
    cursor.execute(insertpuestos4);
    cursor.execute(insertpuestos5);
    cursor.execute(insertpuestos6);
    cursor.execute(insertpuestos7);
    cursor.execute(insertpuestos8);
    cursor.execute(insertpuestos9);
    cursor.execute(insertpuestos10);
    cursor.execute(insertpuestos11);
    cursor.execute(insertpuestos12);
    cursor.execute(insertpuestos13);
    cursor.execute(insertpuestos14);
    cursor.execute(insertpuestos15);
    cursor.execute(insertpuestos16);
    
    connection.commit()
    
    
    #INSERCION TABLA EMPLEADOS
    def fotow():
        foto= 'C:\\Users\\elisa\\Desktop\\UVG\\Semestre IV\\Bases de datos\\Proyecto 2\\womanpic.jpg'
        with open(foto,'rb') as f:
            filedata=f.read()
            b=bytes(filedata).hex()
        return(b)

    def fotom():
        foto= 'C:\\Users\\elisa\\Desktop\\UVG\\Semestre IV\\Bases de datos\\Proyecto 2\\manpic.jpg'
        with open(foto,'rb') as f:
            filedata=f.read()
            b=bytes(filedata).hex()
        return(b)
    
    fake = Faker()
    insertempl1 = """ INSERT INTO empleado (id, nombre, dpi, puesto, email, telefono, ocupacion, fecha_nacimiento, fecha_entrada, direccion, fotografia) VALUES (%s,%s,%s, %s,%s,%s, %s,%s,%s,%s,%s)"""
    ri1 = ('1', fake.name_female(), rstr.digits(13), '1', fake.email(), rstr.digits(8), fake.job(), fake.date_of_birth(), fake.date(), fake.address(), fotow())
    cursor.execute(insertempl1, ri1) 
    connection.commit();
    
    #INSERCION MUJERES
    cuenta = 1
    def contador():
        global cuenta
        cuenta+=1
    
    for i in range(500000):
        job = random.randint(2, 17)
        contador()        
        insertemplw = """ INSERT INTO empleado (id, nombre, dpi, puesto, email, telefono, ocupacion, fecha_nacimiento, fecha_entrada, direccion, fotografia) VALUES (%s,%s,%s, %s,%s,%s, %s,%s,%s,%s,%s)"""
        riw = (str(cuenta), fake.name_female(), rstr.digits(13), str(job), fake.email(), rstr.digits(8), fake.job(), fake.date_of_birth(), fake.date(), fake.address(), fotow())
        cursor.execute(insertemplw, riw) 
        connection.commit();
    #INSERCION HOMBRES
    cuentaM = 500001
    def contadorM():
        global cuentaM
        cuentaM+=1
    
    for i in range(500000):
        jobM = random.randint(2, 17)
        contadorM()        
        insertemplm = """ INSERT INTO empleado (id, nombre, dpi, puesto, email, telefono, ocupacion, fecha_nacimiento, fecha_entrada, direccion, fotografia) VALUES (%s,%s,%s, %s,%s,%s, %s,%s,%s,%s,%s)"""
        rim = (str(cuentaM), fake.name_male(), rstr.digits(13), str(jobM), fake.email(), rstr.digits(8), fake.job(), fake.date_of_birth(), fake.date(), fake.address(), fotom())
        cursor.execute(insertemplm, rim) 
        connection.commit();
    
    #INSERTAR DESEMPEÑO
    cuentaDw = 1
    def contadorDw():
        global cuentaDw
        cuentaDw+=1
    for i in range(1000):
        contadorDw()
        insertempldw = """ INSERT INTO desempeño (empleado, organizacion, puntualidad, responsabilidad, compromiso,conducta, clasificacion) VALUES (%s,%s,%s,%s,%s,%s,%s)"""
        ridw = (str(cuentaDw), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.choice('ABC'))
        cursor.execute(insertempldw, ridw) 
        connection.commit();
        
    cuentaDm = 748001
    def contadorDm():
        global cuentaDm
        cuentaDm+=1   
    for i in range(500):
        contadorDm()
        insertempldm = """ INSERT INTO desempeño (empleado, organizacion, puntualidad, responsabilidad, compromiso,conducta, clasificacion) VALUES (%s,%s,%s,%s,%s,%s,%s)"""
        ridm = (str(cuentaDm), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.choice('ABC'))
        cursor.execute(insertempldm, ridm) 
        connection.commit();
        
    #INSERTAR CANDIDATOS
    cuentaC = 0
    def contadorC():
        global cuentaC
        cuentaC+=1
    
    for i in range(1000):
        jobC = random.randint(2, 17)
        contadorC()        
        insertemplC = """ INSERT INTO candidatos (id, nombre, telefono, puesto, fecha_aplicacion, años_experiencia) VALUES (%s,%s,%s, %s,%s,%s)"""
        riC = (str(cuentaC), fake.name(), rstr.digits(8), str(jobC), fake.date(), random.randint(2, 20))
        cursor.execute(insertemplC, riC) 
        connection.commit();
    print("listo")
    #INSERTAR Permisos
    cuentaP = 0
    def contadorP():
        global cuentaP
        cuentaP+=1
    
    for i in range(1000):
        emplp = random.randint(1, 1000)
        mylist = ["vacaciones", "duelo", "enfermedad"]
        contadorP()
        insertP = """ INSERT INTO PERMISO (no_permiso, empleado, motivo, fecha_inicio, fecha_fin, dias_totales) VALUES (%s,%s,%s, %s,%s,%s)"""
        riP = (str(cuentaP), str(emplp), random.choice(mylist), fake.date(), fake.date(), random.randint(1,20))
        cursor.execute(insertP, riP) 
        connection.commit();
    
    #INSERTAR RECONOCIMIENTOS
    cuentaR = 0
    def contadorR():
        global cuentaR
        cuentaR+=1
    
    for i in range(500):
        emplp = random.randint(1, 1000)
        dep= random.randint(1,4)
        mylist = ["Empleado del Mes", "Mayores Ventas", "Empleado del año", "Mejor Publicidad"]
        contadorR()
        insertR = """ INSERT INTO RECONOCIMIENTO (id, nombre, motivo, empleado, fecha, departamento) VALUES (%s,%s,%s, %s,%s,%s)"""
        riR = (str(cuentaR), random.choice(mylist), fake.text(), str(emplp), fake.date(), str(dep))
        cursor.execute(insertR, riR) 
        connection.commit();
    import base64
    
    
    def foto_women(fotodb):
        fotobytes=byteas()
        x=base64.b64decode(fotobytes)
        with open('imgw.png','wb') as f:
            f.write(x)

    foto_women()
    cv2.imshow('Logo OpenCV',imagen)
    
    # closing database connection.
    cursor.close()
    connection.close()
    

except (Exception, psycopg2.Error) as error:
    print("Failed", error)

finally:
    print("PostgreSQL connection is closed")