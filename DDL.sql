-- DROP SCHEMA public;

CREATE SCHEMA public AUTHORIZATION postgres;
-- public.departamento definition

-- Drop table

-- DROP TABLE public.departamento;

CREATE TABLE public.departamento (
	id bpchar(5) NOT NULL,
	nombre bpchar(50) NOT NULL,
	descripcion text NOT NULL,
	ubicación bpchar(3) NOT NULL,
	CONSTRAINT "Departamento_pkey" PRIMARY KEY (id)
);


-- public.puesto definition

-- Drop table

-- DROP TABLE public.puesto;

CREATE TABLE public.puesto (
	id bpchar(5) NOT NULL,
	nombre bpchar(50) NOT NULL,
	horas_trabajo int2 NOT NULL,
	dias_trabajo int2 NOT NULL,
	departamento bpchar(5) NULL,
	salario int4 NOT NULL,
	sub_departamento bpchar(20) NULL,
	CONSTRAINT "Puesto_pkey" PRIMARY KEY (id),
	CONSTRAINT puesto_departamento_fkey FOREIGN KEY (departamento) REFERENCES public.departamento(id) ON DELETE CASCADE ON UPDATE CASCADE
);


-- public.candidatos definition

-- Drop table

-- DROP TABLE public.candidatos;

CREATE TABLE public.candidatos (
	id bpchar(5) NOT NULL,
	nombre bpchar(100) NOT NULL,
	telefono bpchar(8) NOT NULL,
	puesto bpchar(5) NOT NULL,
	fecha_aplicacion date NOT NULL,
	años_experiencia int2 NOT NULL,
	CONSTRAINT "Candidatos_pkey" PRIMARY KEY (id),
	CONSTRAINT candidatos_puesto_fkey FOREIGN KEY (puesto) REFERENCES public.puesto(id)
);


-- public.empleado definition

-- Drop table

-- DROP TABLE public.empleado;

CREATE TABLE public.empleado (
	id bpchar(20) NOT NULL,
	nombre bpchar(100) NOT NULL,
	dpi bpchar(13) NOT NULL,
	puesto bpchar(5) NOT NULL,
	email bpchar(100) NULL,
	telefono bpchar(8) NOT NULL,
	ocupacion text NOT NULL,
	fecha_nacimiento date NOT NULL,
	fecha_entrada date NOT NULL,
	direccion text NOT NULL,
	fotografia bytea NOT NULL,
	CONSTRAINT "Empleado_pkey" PRIMARY KEY (id),
	CONSTRAINT empleado_puesto_fkey FOREIGN KEY (puesto) REFERENCES public.puesto(id) ON DELETE CASCADE ON UPDATE CASCADE
);


-- public.permiso definition

-- Drop table

-- DROP TABLE public.permiso;

CREATE TABLE public.permiso (
	no_permiso int4 NOT NULL,
	empleado bpchar(20) NOT NULL,
	motivo bpchar(20) NOT NULL,
	fecha_inicio date NOT NULL,
	fecha_fin date NOT NULL,
	dias_totales int2 NOT NULL,
	CONSTRAINT "Permiso_pkey" PRIMARY KEY (no_permiso),
	CONSTRAINT permiso_empleado_fkey FOREIGN KEY (empleado) REFERENCES public.empleado(id) ON DELETE CASCADE ON UPDATE CASCADE
);


-- public.reconocimiento definition

-- Drop table

-- DROP TABLE public.reconocimiento;

CREATE TABLE public.reconocimiento (
	id bpchar(5) NOT NULL,
	nombre bpchar(50) NULL,
	motivo text NULL,
	empleado bpchar(20) NULL,
	fecha date NULL,
	departamento bpchar(5) NULL,
	CONSTRAINT "Reconocimiento_pkey" PRIMARY KEY (id),
	CONSTRAINT reconocimiento_departamento_fkey FOREIGN KEY (departamento) REFERENCES public.departamento(id) ON DELETE CASCADE ON UPDATE CASCADE,
	CONSTRAINT reconocimiento_empleado_fkey FOREIGN KEY (empleado) REFERENCES public.empleado(id) ON DELETE CASCADE ON UPDATE CASCADE
);


-- public.desempeño definition

-- Drop table

-- DROP TABLE public.desempeño;

CREATE TABLE public.desempeño (
	empleado bpchar(20) NOT NULL,
	organizacion int4 NOT NULL,
	puntualidad int4 NOT NULL,
	responsabilidad int4 NOT NULL,
	compromiso int4 NOT NULL,
	conducta int4 NOT NULL,
	clasificacion char NOT NULL,
	CONSTRAINT "Desempeño_pkey" PRIMARY KEY (empleado),
	CONSTRAINT desempeño_empleado_fkey FOREIGN KEY (empleado) REFERENCES public.empleado(id) ON DELETE CASCADE ON UPDATE CASCADE
);
