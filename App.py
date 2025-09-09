import streamlit as st
from datetime import datetime

# Título de la aplicación
st.set_page_config(page_title="Agenda de Reuniones", page_icon="📅", layout="centered")
st.title("📅 Agenda de Reuniones")

# Inicializamos la lista de reuniones en la sesión
if "agenda" not in st.session_state:
    st.session_state.agenda = []

st.subheader("➕ Programar nueva reunión")

# Inputs para programar la reunión
with st.form("form_reunion"):
    asunto = st.text_input("Asunto de la reunión")
    fecha = st.date_input("Fecha")
    hora = st.time_input("Hora")
    submit = st.form_submit_button("Guardar reunión")

# Guardar en la agenda
if submit:
    if asunto.strip() == "":
        st.warning("⚠️ Debes ingresar un asunto para la reunión.")
    else:
        nueva_reunion = {
            "asunto": asunto,
            "fecha": fecha.strftime("%d/%m/%Y"),
            "hora": hora.strftime("%H:%M")
        }
        st.session_state.agenda.append(nueva_reunion)
        st.success(f"✅ Reunión '{asunto}' guardada para el {fecha} a las {hora}")

# Mostrar reuniones agendadas
st.subheader("📌 Reuniones programadas")

if st.session_state.agenda:
    for i, reunion in enumerate(st.session_state.agenda, start=1):
        st.write(f"**{i}. {reunion['asunto']}** — 📅 {reunion['fecha']} 🕒 {reunion['hora']}")
else:
    st.info("No hay reuniones programadas todavía.")
