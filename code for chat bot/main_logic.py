from search import search_web
from extractor import extract_text
from prompts import (
    vlsi_system_prompt,
    vlsi_user_prompt,
    diagram_explanation_prompt
)
from ai_engine import generate_answer

def run_vlsi_ai(query, level, diagram_mode=False):
    urls = search_web(query)

    combined_text = ""
    for url in urls:
        combined_text += extract_text(url)

    if diagram_mode:
        system_prompt = diagram_explanation_prompt(query, level)
        user_prompt = f"Use this reference content if needed:\n{combined_text[:4000]}"
    else:
        system_prompt = vlsi_system_prompt(level)
        user_prompt = vlsi_user_prompt(query, combined_text)

    answer = generate_answer(system_prompt, user_prompt)
    return answer
