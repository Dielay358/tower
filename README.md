# Análisis Cinemático de una Grúa Torre

Infografía interactiva hecha con [Streamlit](https://streamlit.io) para una
feria de física. Muestra el diagrama de una grúa torre y tres calculadoras
en vivo: Movimiento Rectilíneo Uniforme (MRU), Movimiento Circular Uniforme
(MCU) y la transformación cinemática en el tambor del motor de izaje.

## Correrlo en tu computadora

```bash
pip install -r requirements.txt
streamlit run app.py
```

Esto abre automáticamente una pestaña en tu navegador en
`http://localhost:8501`.

## Publicarlo gratis desde GitHub (Streamlit Community Cloud)

1. Crea un repositorio nuevo en GitHub (puede ser público o privado) y sube
   estos tres archivos: `app.py`, `requirements.txt` y este `README.md`.
2. Entra a [share.streamlit.io](https://share.streamlit.io) e inicia sesión
   con tu cuenta de GitHub.
3. Haz clic en **New app**, elige tu repositorio, la rama (`main`) y el
   archivo principal (`app.py`).
4. Haz clic en **Deploy**. En un par de minutos tendrás una URL pública
   (algo como `https://tu-app.streamlit.app`) que puedes abrir desde
   cualquier dispositivo el día de la feria.

Cada vez que hagas `git push` con cambios a `app.py`, la app se actualiza
sola en la nube.