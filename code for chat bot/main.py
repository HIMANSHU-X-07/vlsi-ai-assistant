from search import search_web
from extractor import extract_text
from prompts import vlsi_system_prompt, vlsi_user_prompt
from ai_engine import generate_answer

def run_vlsi_ai():
    query = input("Enter VLSI/Electronics topic: ")
    level = input("Choose level (Beginner / Academic / Interview): ")

    print("\nSearching trusted sources...\n")
    urls = search_web(query)

    combined_text = ""
    for url in urls:
        combined_text += extract_text(url)

    system_prompt = vlsi_system_prompt(level)
    user_prompt = vlsi_user_prompt(query, combined_text)

    print("Generating VLSI-focused answer...\n")
    answer = generate_answer(system_prompt, user_prompt)

    print("===== AI RESPONSE =====\n")
    print(answer)

if __name__ == "__main__":
    run_vlsi_ai()
