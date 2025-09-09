Actividad 1, Misael Ancan - Christian Díaz

En esta actividad creamos una pagina para seleccionar profesionales, los pasos que seguimos para el desarrollo fueron:

1. Inicialización del Proyecto
Se creó el proyecto base con:
```bash
django-admin startproject.
```
Luego se generó una aplicación dentro del proyecto con:
```bash
py manage.py startapp.
```

3. Estructura de Páginas
Se diseñaron tres páginas principales:
Página central: muestra imágenes de los dos integrantes. Al hacer clic en cada imagen, se redirige al currículum correspondiente.

Currículum 1: contiene un formulario para ingresar habilidades, nivel de dominio y correo electrónico.

Currículum 2: permite ingresar nombre, apellido, correo y uno o más números de teléfono.

Se añadieron botones de navegación en cada página para moverse entre ellas fácilmente.

4. Estilos Visuales
Se creó un archivos styles.css para aplicar estilos personalizados a las páginas HTML, mejorando la presentación visual de las paginas web. 
5. Modelado de Datos
Se definieron modelos en models.py para almacenar la información ingresada en los formularios:

Modelo para Página 1: habilidades, nivel y correo.

Modelo para Página 2: nombre, apellido, correo y números de teléfono (permitiendo múltiples entradas).

6. Migraciones y Base de Datos
Se ejecutaron las migraciones con:
```bash
py manage.py makemigrations
```
```bash
py manage.py migrate
```
Esto generó las tablas necesarias en la base de datos para guardar la información de los formularios.

7. Almacenamiento de Datos
Al enviar los formularios desde cada página de currículum, los datos se guardan automáticamente en la base de datos.
Esto permite consultar, administrar o extender la información posteriormente.

8. Los usuarios de Administrador de la base de datos en sqlite3
son:

   nombre de usuario: christian
    contraseña: 1234

    nombre de usuario: misael
    contraseña: 12345
