--insertar

insert into empleado (id, nombre, dpi, puesto, email, telefono, ocupacion, fecha_nacimiento, fecha_entrada, direccion, fotografia) values('8594852', 'Celia Juarez', '8745216985412', '2', 'eesg@gmail.com', '84596215',  'Secretaria', '1989-10-10', '2000-02-12', 'Zona 1, Ciudad de Guatemala', pg_read_binary_file('C:\\Users\\elisa\\Desktop\\UVG\\Semestre IV\\Bases de datos\\Proyecto 2\\womanpic.jpg'));
select * from empleado where id = '8594852';

--update 
update empleado set nombre = 'Helena Dominguez' where id = '8594852';
select * from empleado where id = '8594852';

--delete 
delete from empleado where id = '8594852';
select * from empleado where id = '8594852';

--