# Urban Grocers – Pruebas Automatizadas de API

## Descripción
Este proyecto automatiza pruebas de regresión sobre el parámetro `"name"` en la API utilizada para crear kits de usuarios. Su objetivo es garantizar que la aplicación maneje correctamente entradas válidas y no válidas, permitiendo detectar errores tempranamente y facilitando la integración de nuevos tipos de datos o la expansión hacia otros parámetros del JSON de la solicitud.

El proyecto demuestra buenas prácticas de **testing**, asegurando confiabilidad y calidad en la API mientras se optimiza la mantenibilidad y escalabilidad de las pruebas.

## Tecnologías y Herramientas
- Python 3.13  
- Pytest 8.4.1  
- PyCharm 2025.1.3  
- Control de versiones con Git/GitHub  

## Técnicas y Estructura
- **Estructura modular:** Separación de pruebas, datos y funciones auxiliares para mejorar la mantenibilidad y reutilización del código.  
- **Pruebas positivas y negativas:** Validación de límites, caracteres especiales, espacios y números.  
- **Aserciones con Pytest:** Verificación de códigos de respuesta HTTP y contenido JSON para asegurar resultados correctos.  
- **Preparación para expansión:** Diseño que facilita la inclusión de nuevos parámetros y escenarios de prueba.  

## Prerrequisitos
1. Tener instalado **Python 3.13**.  
2. Instalar **Pytest** desde tu entorno de desarrollo o con el siguiente comando:  
   ```sh
   pip install pytest
   ```

## Ejecución de Pruebas   
1. Clona el repositorio
  ```sh
   git clone https://github.com/Kevsql/Urban_Grocers_Automated_API_tests.git
   ```
2. Configura la variable `URL_SERVICE` en `configuration.py` con la URL del servidor.
3. Ejecuta las pruebas desde el archivo `create_kit_name_kit_test.py`
