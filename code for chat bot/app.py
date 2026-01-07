import streamlit as st
from main_logic import run_vlsi_ai
from diagram_generator import generate_diagram

st.set_page_config(page_title="VLSI AI Assistant")

st.title("🔌 AI-Powered VLSI & Electronics Assistant")

topic = st.text_input(
    "Enter VLSI / Electronics Topic",
    placeholder="e.g. CMOS Inverter"
)

level = st.selectbox(
    "Choose Explanation Level",
    ["Beginner", "Academic", "Interview"]
)

diagram_mode = st.checkbox("📐 Explain using Diagram")
generate_image = st.checkbox("🖼️ Generate Diagram Image")

if st.button("Generate Answer"):
    if not topic:
        st.warning("Please enter a topic.")
    else:
        if generate_image:
            with st.spinner("Generating diagram image..."):
                diagram = generate_diagram(topic)
                st.image(diagram, caption=f"{topic} Diagram", use_column_width=True)

        with st.spinner("Generating explanation..."):
            answer = run_vlsi_ai(topic, level, diagram_mode)

        st.markdown("### 📘 AI Explanation")
        st.write(answer)
