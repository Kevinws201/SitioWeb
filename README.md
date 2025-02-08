# Sistema de Verificación de Estatus de Certificación Universitaria

## 📌 Descripción

Este proyecto es un software diseñado para verificar el estatus de certificación universitaria de los estudiantes. Su principal objetivo es proporcionar una herramienta eficiente y confiable para que los estudiantes consulten el estado de sus trámites de titulación. Esto reduce la carga de trabajo del personal administrativo y brinda mayor transparencia en el proceso.

## 🎯 Características

- ✅ **Automatización del seguimiento de trámites** - Permite a los estudiantes conocer el estado de su certificación sin depender de consultas presenciales.
- ✅ **Reducción de carga administrativa** - Optimiza el trabajo del personal al minimizar consultas repetitivas.
- ✅ **Acceso semipresencial** - Facilita la gestión de trámites de forma remota, reduciendo la necesidad de traslados innecesarios.
- ✅ **Flexibilidad y escalabilidad** - Adaptable a distintos flujos de trabajo institucionales y con posibilidad de integración con otras universidades.
- ✅ **Seguridad y privacidad** - Protección de datos personales y académicos, con acceso restringido a personal autorizado.

## 🛠️ Tecnologías Utilizadas

Actualmente, el proyecto utiliza las siguientes tecnologías:

- **Lenguaje de programación:** Python.
- **Frameworks y Librerías:** Django, Bootstrap.
- **Base de Datos:** MySQL.

## 🚀 Instalación y Uso

1. Clona el repositorio:
   ```
   git clone https://github.com/usuario/repositorio.git
   ```
2. Instalar Python sitio web oficial: https://www.python.org/downloads/
  
4. Descargar e instalar entorno virtual:
   ```
   pip install virtualenv
   virtualenv venv
   ```
5. Activar entorno virtual:
   ```
   .\venv\Scripts\activate
   ```
6. Instalar dependencias del proyecto:
   ```
   pip install -r requirements.txt
   ```
7. Configurar variables de entorno de la base de datos. 
  Crear archivo .env en directorio raiz junto a manage.py. 
  Configurar variables con nombre correcto segun tu servidor MySQL
   ```
   DB_NAME=mi_basededatos
   DB_USER=mi_usuario_mysql
   DB_PASSWORD=mi_contraseña_mysql
   DB_HOST=127.0.0.1
   DB_PORT=3306
   ```
8.  Realizar migraciones a la base de datos:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```
8. Ejecutar el programa:
   ```
   python manage.py runserver
   ```