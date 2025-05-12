import streamlit as st
import random

all_questions_data = [
    {
        "question": "Wer gilt als Erfinder des World Wide Web (WWW)?",
        "choices": ["Bill Gates", "Steve Jobs", "Tim Berners-Lee", "Mark Zuckerberg"],
        "correct_answer": "Tim Berners-Lee"
    },
    {
        "question": "Welches Unternehmen entwickelte das Betriebssystem Android?",
        "choices": ["Apple", "Microsoft", "Google", "Amazon"],
        "correct_answer": "Google"
    },
    {
        "question": "Wie wird der Hauptprozessor eines Computers oft bezeichnet?",
        "choices": ["GPU", "RAM", "CPU", "ROM"],
        "correct_answer": "CPU"
    },
    {
        "question": "Was ist die Abkürzung für den Speicher, der Daten temporär für schnelle Zugriffe speichert?",
        "choices": ["HDD", "SSD", "RAM", "USB"],
        "correct_answer": "RAM"
    },
    {
        "question": "Welches Programmierparadigma betont die Verwendung von Objekten und Klassen?",
        "choices": ["Prozedurale Programmierung", "Funktionale Programmierung", "Objektorientierte Programmierung", "Logische Programmierung"],
        "correct_answer": "Objektorientierte Programmierung"
    },
    {
        "question": "Wie heißt das Netzwerk, das Computer über große geografische Entfernungen verbindet?",
        "choices": ["LAN", "WLAN", "PAN", "WAN"],
        "correct_answer": "WAN"
    },
    {
        "question": "Welche Programmiersprache wird oft für Data Science und Machine Learning verwendet?",
        "choices": ["Java", "C++", "Python", "JavaScript"],
        "correct_answer": "Python"
    },
    {
        "question": "Was ist ein Algorithmus?",
        "choices": ["Ein Computerbauteil", "Eine Art von Virus", "Eine Schritt-für-Schritt-Anleitung zur Lösung eines Problems", "Ein soziales Netzwerk"],
        "correct_answer": "Eine Schritt-für-Schritt-Anleitung zur Lösung eines Problems"
    },
    {
        "question": "Wer prägte den Begriff 'künstliche Intelligenz' (KI)?",
        "choices": ["Alan Turing", "John McCarthy", "Ada Lovelace", "Charles Babbage"],
        "correct_answer": "John McCarthy"
    },
    {
        "question": "Was ist die Maßeinheit für die Bildschirmauflösung?",
        "choices": ["Hertz", "Pixel", "Byte", "Volt"],
        "correct_answer": "Pixel"
    }
]

if "quiz_data" not in st.session_state:
    st.session_state.quiz_data = random.sample(all_questions_data, 5)
    st.session_state.index = 0
    st.session_state.score = 0
    st.session_state.show_feedback = False
    st.session_state.answers = {}

num_questions = len(st.session_state.quiz_data)

if st.session_state.index < num_questions:
    current_question_data = st.session_state.quiz_data[st.session_state.index]
    question = current_question_data["question"]
    correct_answer = current_question_data["correct_answer"]

    if f"choices_{st.session_state.index}" not in st.session_state:
        shuffled_choices = current_question_data["choices"][:]
        random.shuffle(shuffled_choices)
        st.session_state[f"choices_{st.session_state.index}"] = shuffled_choices
    choices = st.session_state[f"choices_{st.session_state.index}"]

    st.title("Technologie-Quiz")
    st.progress((st.session_state.index + 1) / num_questions)
    st.subheader(f"Punktestand: {st.session_state.score}")
    st.header(f"Frage {st.session_state.index + 1} von {num_questions}")
    st.write(question)
    selected = st.radio("Wähle eine Antwort:", choices, key=st.session_state.index)

    if st.button("Antwort abschicken"):
        st.session_state.show_feedback = True
        st.session_state.answers[st.session_state.index] = selected

        if selected == correct_answer:
            st.session_state.score += 1
            st.success("Richtig!")
        else:
            st.error(f"Falsch. Richtige Antwort: {correct_answer}")

    if st.session_state.show_feedback:
        next_button_label = "Nächste Frage"
        if st.session_state.index == num_questions - 1:
            next_button_label = "Ergebnisse anzeigen"  # Ändere den Text für die letzte Frage

        if st.button(next_button_label):
            st.session_state.index += 1
            st.session_state.show_feedback = False
            st.rerun()

else:
    st.success("Quiz beendet!")
    st.subheader(f"Dein finaler Punktestand: {st.session_state.score} von {num_questions}")
    st.subheader("Auflistung der Endergebnisse:")
    for i in range(num_questions):
        question_data = st.session_state.quiz_data[i]
        question = question_data["question"]
        correct = question_data["correct_answer"]
        user_answer = st.session_state.answers.get(i, "Nicht beantwortet")
        if user_answer == correct:
            st.write(f"**Frage {i + 1}:** {question} - Deine Antwort: **{user_answer}** (Richtig)")
        else:
            st.write(f"**Frage {i + 1}:** {question} - Deine Antwort: **{user_answer}** (Falsch, richtige Antwort: {correct})")

    if st.button("Quiz neu starten"):
        st.session_state.pop("quiz_data")
        st.session_state.index = 0
        st.session_state.score = 0
        st.session_state.show_feedback = False
        st.session_state.answers = {}
        for i in range(len(all_questions_data)):
            key = f"choices_{i}"
            if key in st.session_state:
                st.session_state.pop(key)
        st.rerun()