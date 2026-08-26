import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

st.set_page_config(
    page_title="Análisis Cinemático de una Grúa Torre",
    layout="wide",
)

st.title("Análisis Cinemático de una Grúa Torre")
st.caption("Feria de Física — Ingeniería Industrial")

st.markdown(
    """
En el ámbito de la ingeniería industrial, la optimización de los tiempos y la
eficiencia de los procesos son fundamentales. La cinemática, al ser la rama
que estudia el movimiento sin importar las masas o fuerzas que lo producen,
sirve como una herramienta clave para planificar, predecir y optimizar cómo
se desplazan los materiales en un entorno productivo, como una obra de
construcción civil.

En el funcionamiento de la grúa torre, la cinemática aplicada permite
calcular los **tiempos de ciclo**: cuánto tarda el gancho en trasladar una
carga desde un punto de origen hasta su destino final, combinando distintas
velocidades operativas para maximizar la productividad y evitar cuellos de
botella.
"""
)

st.divider()

# ---------------------------------------------------------------------------
# Estado inicial de los sliders (para poder animar el dibujo con ellos)
# ---------------------------------------------------------------------------

st.subheader("Diagrama de la grúa")

col_diagram, col_controls = st.columns([1.3, 1])

with col_controls:
    st.markdown("**Controles del diagrama**")
    carro_pos = st.slider(
        "Posición del carro en la pluma (m)", 0.0, 20.0, 10.0, 0.5,
        help="Desplaza el carro de distribución a lo largo de la pluma (MRU horizontal)",
    )
    gancho_alt = st.slider(
        "Altura del gancho bajo la pluma (m)", 1.0, 15.0, 6.0, 0.5,
        help="Sube o baja el gancho de izaje (MRU vertical)",
    )
    giro_ang = st.slider(
        "Ángulo de giro de la pluma (°)", 0, 360, 45, 5,
        help="Orienta la pluma sobre la corona de giro (MCU)",
    )

with col_diagram:
    fig, ax = plt.subplots(figsize=(6, 5))
    ax.set_xlim(-12, 12)
    ax.set_ylim(-14, 8)
    ax.set_aspect("equal")
    ax.axis("off")

    # Torre vertical
    ax.plot([0, 0], [0, 6], color="#2C2C2A", linewidth=4)
    # Base
    ax.plot([-1.2, 1.2], [0, 0], color="#2C2C2A", linewidth=4)

    # Pluma rotada según el ángulo de giro
    theta = np.radians(giro_ang)
    pluma_len = 10
    x_end = pluma_len * np.cos(theta)
    y_end = pluma_len * np.sin(theta) * 0.15  # aplanado para vista lateral
    ax.plot([0, x_end], [6 + y_end, 6], color="#2C2C2A", linewidth=3)
    ax.plot([0, -x_end * 0.35], [6 + y_end, 6], color="#2C2C2A", linewidth=2, alpha=0.5)

    # Corona de giro
    corona = patches.Circle((0, 6), 0.5, facecolor="#5DCAA5", edgecolor="#0F6E56")
    ax.add_patch(corona)

    # Posición del carro a lo largo de la pluma
    frac = carro_pos / pluma_len
    carro_x = frac * x_end
    carro_y = 6 + frac * y_end
    carro = patches.Rectangle(
        (carro_x - 0.4, carro_y - 0.2), 0.8, 0.4,
        facecolor="#85B7EB", edgecolor="#185FA5",
    )
    ax.add_patch(carro)

    # Cable y gancho
    ax.plot([carro_x, carro_x], [carro_y - 0.2, carro_y - gancho_alt],
             color="#888780", linewidth=1, linestyle="--")
    gancho = patches.Rectangle(
        (carro_x - 0.4, carro_y - gancho_alt - 0.4), 0.8, 0.4,
        facecolor="#F0997B", edgecolor="#D85A30",
    )
    ax.add_patch(gancho)
    ax.text(carro_x, carro_y - gancho_alt - 0.9, "carga",
            ha="center", fontsize=9, color="#4A1B0C")

    ax.set_title("Vista esquemática de la grúa torre", fontsize=11)
    st.pyplot(fig)

st.divider()

# ---------------------------------------------------------------------------
# Calculadoras cinemáticas
# ---------------------------------------------------------------------------

st.subheader("Calculadoras cinemáticas")

tab_mru, tab_mcu, tab_transf = st.tabs([
    "Movimiento Rectilíneo Uniforme",
    "Movimiento Circular Uniforme",
    "Transformación Cinemática",
])

with tab_mru:
    st.markdown(
        "Rige los desplazamientos en línea recta: el movimiento horizontal "
        "del carro de distribución y el movimiento vertical del gancho de izaje."
    )
    st.latex(r"v = \frac{d}{t}")

    c1, c2 = st.columns(2)
    d = c1.slider("Distancia d (m)", 1.0, 40.0, 12.0, 0.5, key="mru_d")
    t = c2.slider("Tiempo t (s)", 1.0, 60.0, 20.0, 0.5, key="mru_t")

    v = d / t
    st.metric("Velocidad lineal v", f"{v:.2f} m/s")

with tab_mcu:
    st.markdown(
        "Rige la orientación o giro de la grúa sobre su eje principal, "
        "la corona de giro."
    )
    st.latex(r"\omega = \frac{\Delta \theta}{\Delta t}")

    c1, c2 = st.columns(2)
    ang = c1.slider("Ángulo Δθ (°)", 10, 360, 90, 5, key="mcu_a")
    t2 = c2.slider("Tiempo Δt (s)", 1.0, 60.0, 15.0, 0.5, key="mcu_t")

    omega = np.radians(ang) / t2
    st.metric("Velocidad angular ω", f"{omega:.3f} rad/s")

with tab_transf:
    st.markdown(
        "Ocurre en el tambor del motor de izaje: un movimiento rotacional "
        "puro se convierte en un movimiento rectilíneo del cable."
    )
    st.latex(r"v = \omega \cdot r")

    c1, c2 = st.columns(2)
    w = c1.slider("ω del tambor (rad/s)", 1.0, 20.0, 8.0, 0.5, key="tr_w")
    r = c2.slider("Radio del tambor r (cm)", 2.0, 20.0, 8.0, 0.5, key="tr_r")

    v_izaje = w * (r / 100)
    st.metric("Velocidad de izaje del gancho", f"{v_izaje:.2f} m/s")

st.divider()
st.caption(
    "Informe de Proyecto — Análisis Cinemático de una Grúa Torre. "
    "Hecho con Streamlit."
)
