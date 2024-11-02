# 🎥 Video Traductor Django & Generador de Subtítulos 📝

Este proyecto es una aplicación web construida en Django que permite generar subtítulos en el idioma original de un video y traducirlos al español. Solo debes subir el video, ¡y el sistema se encarga del resto! 🌍

## 🧰 Características

- 📝 **Generación automática de subtítulos**: Transcribe el audio del video.
- 🌎 **Traducción al español**: Traduce los subtítulos generados.
- 🎯 **Interfaz web fácil de usar**: Sube tu archivo de video desde el navegador y visualiza los resultados.
- ⚡ **Soporte para múltiples formatos de video**: Acepta formatos de video comunes como MP4, AVI, MOV, entre otros.

## 🚀 Requisitos

- Python 3.7 o superior
- Django 3.2 o superior
- Instalar dependencias del archivo `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

## 📝 Uso

1. Clona este repositorio:

    ```bash
    git clone https://github.com/alejandroponce00/video_traductor_django.git
    cd video_traductor_django
    ```

2. Realiza las migraciones de la base de datos:

    ```bash
    python manage.py migrate
    ```

3. Inicia el servidor:

    ```bash
    python manage.py runserver
    ```

4. Accede a la aplicación en tu navegador en [http://127.0.0.1:8000](http://127.0.0.1:8000) y sube tu video. 📁

## 📂 Estructura del proyecto

- `video_traductor_django/`: Contiene la configuración de Django y archivos principales del proyecto.
- `app/`: Aplicación principal donde está la lógica de generación y traducción de subtítulos.
- `media/`: Carpeta donde se almacenan los videos subidos y los subtítulos generados.
- `templates/`: Archivos HTML para la interfaz de usuario.
- `requirements.txt`: Archivo con las dependencias necesarias.

## 💡 Notas adicionales

- El tiempo de procesamiento depende de la duración del video y del rendimiento del servidor.
- Si encuentras problemas, no dudes en abrir un [issue](https://github.com/alejandroponce00/video_traductor_django/issues) en el repositorio.

## 📝 Contribuciones

¡Las contribuciones son bienvenidas! 🤝 Si deseas agregar nuevas características o mejorar el código, siéntete libre de hacer un fork del repositorio y abrir un pull request.

## 📄 Licencia

Este proyecto está licenciado bajo la [MIT License](LICENSE).

---

Hecho con ❤️ por [Alejandro Ponce](https://github.com/alejandroponce00)
