import streamlit as 

# -----------------------------
#  BASE DE DATOS DE PREGUNTAS
# -----------------------------

preguntas = [
    {"texto": "¿Cúal es el grupo muscular que haces en el ejercico, jalon al pecho?",
     "opciones": ["pecho", "espalda", "biceps", "pierna"],
     "correcta": "espalda"},

    {"texto": "¿Cuantas partes tiene el hombro?",
     "opciones": ["1", "3", "4"],
     "correcta": "3"},

    {"texto": "¿Como se llama el ejercicio que trabaja la cabeza larga del tríceps?",
     "opciones": ["extension de triceps por encima de la cabeza", "fondos", "extension de triceps por delante del cuerpo", "curl predicador"],
     "correcta": "extension de triceps por encima de la cabeza"},

    {"texto": "¿Qué función tiene el biceps en ejercicios de pecho?",
     "opciones": ["ninguna", "ayuda a poder hacer más fuerza", "hace mejor la tecnica", "salchicha"],
     "correcta": "salchicha"},

    {"texto": "¿Cuántas repeticiones son ideales para ganar masa muscular?",
     "opciones": ["8", "12", "10", "4"],
     "correcta": "8"},

    {"texto": "¿Qué diferencia hay entre press inclinado y press plano?",
     "opciones": ["ninguna", "que uno trabaja la parte superior del pecho y otro la media", "que uno trabaja la parte baja del pecho y otro la del medio", "en los dos ejercicios hacen solo triceps"],
     "correcta": "que uno trabaja la parte superior del pecho y otro la media"},

    {"texto": "¿Cardio antes o después de las pesas?",
     "opciones": ["antes", "despues", "da igual", "nunca"],
     "correcta": "despues"},

    {"texto": "¿Es necesario tomar suplementos para progresar?",
     "opciones": ["no", "si", "depende"],
     "correcta": "no"},

    {"texto": "¿Cuando estas haciendo plancha que parte del cuerpo empieza a doler antes?",
     "opciones": ["abdomen", "espalda baja", "hombros", "antebrazos"],
     "correcta": "espalda baja"},
]

if "preguntas_mezcladas" not in st.session_state:
    preguntas_mezcladas = preguntas.copy()
    random.shuffle(preguntas_mezcladas)
    st.session_state.preguntas_mezcladas = preguntas_mezcladas

preguntas = st.session_state.preguntas_mezcladas


st.title("Examen Interactivo")
st.write("Responde y pulsa entregar para ver tu nota.")

# -----------------------------
#  FORMULARIO
# -----------------------------

with st.form("quiz_form"):

    respuestas_usuario = []

    for i, pregunta in enumerate(preguntas):

        st.subheader(f"Pregunta {i+1}")
        st.write(pregunta["texto"])

        # ✅ Opción correcta añadida
        opciones = ["-- Dejar en blanco --"] + pregunta["opciones"]

        eleccion = st.radio(
            "Elige una opción:",
            opciones,
            key=f"pregunta_{i}"
        )

        respuestas_usuario.append(eleccion)
        st.divider()

    boton_enviar = st.form_submit_button("Entregar examen")

# -----------------------------
# CORRECCIÓN
# -----------------------------

if boton_enviar:

    total = len(preguntas)
    puntuacion = 0
    informe = ""

    for i in range(total):

        correcta = preguntas[i]["correcta"]
        respuesta = respuestas_usuario[i]

        # ✅ Ahora sí detecta si está en blanco
        if respuesta == "-- Dejar en blanco --":
            informe += f"### Pregunta {i+1}\nSin responder.\n\n"
            

        if respuesta == correcta:
            puntuacion += 1
            informe += f"### Pregunta {i+1}\nCorrecta.\n\n"
        else:
            puntuacion -= 0.25  # Penalización
            informe += f"### Pregunta {i+1}\nIncorrecta.\nRespuesta correcta: **{correcta}**\n\n"

    # Cálculo sobre 10
    nota = (puntuacion / total) * 10

    if nota < 0:
        nota = 0

    nota = round(nota, 2)

    st.divider()

    # -----------------------------
    #  TABS (RESULTADO + INFORME)
    # -----------------------------

    tab1, tab2 = st.tabs(["📊 Resultado", "📄 Informe detallado"])

    with tab1:

        st.header(f"Nota final: {nota} / 10")

        if nota < 2:
            st.error("Muy insuficiente, Necesitas repasar mucho.")

        elif 2 <= nota < 5:
            st.error("Insuficiente, Sigue practicando.")

        elif 5 <= nota < 6:
            st.warning("Suficiente, Has aprobado por poco.")
            st.balloons()

        elif 6 <= nota < 7:
            st.success("Bien, Buen trabajo.")
            st.balloons()

        elif 7 <= nota < 9:
            st.success("Notable, Muy buen nivel.")
            st.balloons()

        elif 9 <= nota < 10:
            st.success("Sobresaliente, Excelente trabajo.")
            st.balloons()

        elif nota == 10:
            st.success("EXCELENTE, ¡Examen perfecto!")
            st.balloons()
            st.snow()
            

    with tab2:

        st.markdown("# Informe del examen")
        st.markdown(informe)
    with tab2:

        st.markdown("# Informe del examen")
        st.markdown(informe)
