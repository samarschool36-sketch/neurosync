import streamlit as st
import random
from datetime import datetime

# --- App Configuration ---
st.set_page_config(page_title="NeuroSync", page_icon="🧠", layout="wide")

# --- Initialize Session State ---
if "attention_level" not in st.session_state:
    st.session_state.attention_level = 100
if "stress_level" not in st.session_state:
    st.session_state.stress_level = 0
if "routines" not in st.session_state:
    st.session_state.routines = []
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# --- Header ---
st.title("🧠 NeuroSync – AI Cognitive Support Companion")
st.markdown("Adaptive support for focus, learning, and emotional regulation.")

# --- Sidebar Navigation ---
menu = st.sidebar.radio("Navigate", [
    "AI Attention Tracker",
    "Dynamic Routine Builder",
    "Task Breakdown Engine",
    "Sensory Regulation Toolkit",
    "Parent & Educator Dashboard"
])

# --- AI Attention Tracker ---
if menu == "AI Attention Tracker":
    st.header("🎯 AI Attention Tracker")

    if st.button("Check Attention"):
        st.session_state.attention_level -= random.randint(5, 15)
        if st.session_state.attention_level < 50:
            suggestion = random.choice([
                "Take a 5-minute micro-break.",
                "Try a short breathing exercise.",
                "Adjust lighting or reduce noise."
            ])
        else:
            suggestion = "Attention stable. Keep going!"
        st.success(f"Attention Level: {st.session_state.attention_level}")
        st.info(suggestion)

    st.progress(st.session_state.attention_level / 100)

# --- Dynamic Routine Builder ---
elif menu == "Dynamic Routine Builder":
    st.header("📅 Dynamic Routine Builder")

    with st.form("routine_form"):
        task = st.text_input("Enter routine task:")
        time = st.time_input("Select time:")
        submitted = st.form_submit_button("Add Routine")
        if submitted and task:
            st.session_state.routines.append({"task": task, "time": str(time), "status": "pending"})
            st.success("Routine added successfully!")

    if st.session_state.routines:
        st.subheader("Your Routines")
        for i, r in enumerate(st.session_state.routines):
            st.write(f"🕒 {r['time']} — {r['task']} ({r['status']})")

# --- Task Breakdown Engine ---
elif menu == "Task Breakdown Engine":
    st.header("🧩 Task Breakdown Engine")

    task_input = st.text_area("Enter a large task or assignment:")
    if st.button("Break Down Task"):
        if task_input:
            subtasks = [f"Step {i+1}: {part.strip()}" for i, part in enumerate(task_input.split('.')) if part.strip()]
            st.session_state.tasks.append({"task": task_input, "subtasks": subtasks, "progress": 0})
            st.success("Task broken down successfully!")
            for sub in subtasks:
                st.write(f"- {sub}")
        else:
            st.warning("Please enter a task first.")

# --- Sensory Regulation Toolkit ---
elif menu == "Sensory Regulation Toolkit":
    st.header("🌈 Sensory Regulation Toolkit")

    if st.button("Check Stress Level"):
        st.session_state.stress_level += random.randint(0, 5)
        if st.session_state.stress_level > 7:
            suggestion = random.choice([
                "Try a deep breathing exercise.",
                "Take a short walk.",
                "Use a calming visual tool."
            ])
        else:
            suggestion = "Stress levels normal."
        st.metric("Stress Level", st.session_state.stress_level)
        st.info(suggestion)

# --- Parent & Educator Dashboard ---
elif menu == "Parent & Educator Dashboard":
    st.header("📊 Parent & Educator Dashboard")

    st.subheader("Attention & Stress Overview")
    col1, col2 = st.columns(2)
    col1.metric("Attention Level", st.session_state.attention_level)
    col2.metric("Stress Level", st.session_state.stress_level)

    st.subheader("Routines")
    if st.session_state.routines:
        for r in st.session_state.routines:
            st.write(f"🕒 {r['time']} — {r['task']} ({r['status']})")
    else:
        st.write("No routines added yet.")

    st.subheader("Tasks")
    if st.session_state.tasks:
        for t in st.session_state.tasks:
            st.write(f"📘 {t['task']}")
            for sub in t["subtasks"]:
                st.write(f" • {sub}")
    else:
        st.write("No tasks added yet.")
