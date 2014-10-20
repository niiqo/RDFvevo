RDFvevo
=======

Aplicacion web django para la toma de asistencia.


Caracteristicas
---------------

  - Base de datos postgresql.
  - Hecho en python con django 1.7.


Postgresql
----------

Error 'FATAL:  Peer authentication failed for user "myuser"' al tratar de usar la base de datos por primera vez.

Se soluciono cambiando el archivo 'pg_hba.conf':

Cambiamos los valores 'ident' por 'trust' en 3 lineas.