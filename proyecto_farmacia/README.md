# Sistema de Puntos de Interés Geoespaciales - Villa Canales

Este proyecto es una aplicación web contenerizada para el registro y consulta de puntos de interés (POIs) utilizando capacidades geoespaciales.

## Arquitectura
El sistema utiliza una arquitectura de microservicios compuesta por:
* **Base de Datos:** PostgreSQL 15 + PostGIS para almacenamiento geográfico.
* **Backend:** FastAPI (Python) para la API REST.
* **Frontend:** HTML5 + Leaflet.js para el mapa interactivo.
* **Proxy Reverso:** Nginx para centralizar las peticiones.

## Requisitos
* Docker y Docker Compose instalados.

## Instrucciones de Uso
1. Clonar o descargar esta carpeta.
2. Abrir una terminal en la raíz del proyecto.
3. Ejecutar el comando:
   ```bash
   sudo docker-compose up -d
   ```
4. Acceder en el navegador a: **http://localhost**

## Funcionalidades
* **Visualización:** El mapa carga automáticamente 5 puntos iniciales mediante seeding.
* **Registro:** Haz clic en cualquier parte del mapa y usa el formulario lateral para guardar nuevos puntos.
* **Persistencia:** Los datos se mantienen gracias a volúmenes de Docker incluso si se apaga el sistema.
