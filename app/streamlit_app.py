# app/streamlit_app.py
import sys
import os

# Add project root to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


import streamlit as st
from agent.social_agent import generate_caption, generate_post_ideas, generate_calendar


st.set_page_config(page_title="AI Social Media Agent", layout="centered")
st.title("📱 Social Media Agent (Caption · Ideas · Calendar)")

st.sidebar.header("Modes")
mode = st.sidebar.radio("Select Mode", ["Generate Caption", "Post Ideas", "Content Calendar"])

if mode == "Generate Caption":
    st.header("Generate Caption")
    topic = st.text_input("Topic (e.g., new product, motivational post, eco bottle):")
    tone = st.text_input("Tone (e.g., friendly, professional, humorous):", value="Friendly")
    if st.button("Generate Caption"):
        if not topic.strip():
            st.error("Please enter a topic.")
        else:
            with st.spinner("Generating..."):
                caption = generate_caption(topic, tone)
            st.subheader("Caption")
            st.write(caption)

elif mode == "Post Ideas":
    st.header("Generate Post Ideas")
    niche = st.text_input("Niche (e.g., fitness, travel, education):")
    n = st.slider("Number of ideas", 3, 15, 5)
    if st.button("Generate Ideas"):
        if not niche.strip():
            st.error("Please enter a niche.")
        else:
            with st.spinner("Generating ideas..."):
                ideas = generate_post_ideas(n, niche)
            st.subheader("Ideas")
            st.write(ideas)

elif mode == "Content Calendar":
    st.header("7-Day Content Calendar")
    niche = st.text_input("Niche for the calendar:")
    if st.button("Generate Calendar"):
        if not niche.strip():
            st.error("Please enter a niche.")
        else:
            with st.spinner("Generating calendar..."):
                cal = generate_calendar(niche)
            st.subheader("7-Day Calendar")
            st.write(cal)