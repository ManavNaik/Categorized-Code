import time
import google.generativeai as genai
from selenium import webdriver
from selenium.webdriver.common.by import By

QUIZ_URL = "http://127.0.0.1:5500/quiz%20app/index.html"

genai.configure(api_key="AIzaSyCtgb97jwTV7cnQa7VTRygzpA0JdiRtyuo")
model = genai.GenerativeModel("gemini-1.5-flash")

driver = webdriver.Chrome()
driver.get(QUIZ_URL)
time.sleep(2)

def ask_gemini(question, answers, multi):
    formatted = (
        f"Question: {question}\n"
        f"Choices:\n"
        + "\n".join(f"{i}. {a}" for i, a in enumerate(answers))
        + ("\nSelect ALL correct answers." if multi else "\nSelect the ONE correct answer.")
        + "\nGive me ONLY the index number(s) (comma separated) of the correct answer(s), nothing else."
    )
    response = model.generate_content(formatted)
    ans = response.text.strip().replace(' ', '').replace('.', '')
    return [int(i) for i in ans.split(',') if i.isdigit()]

while True:
    try:
        q_el = driver.find_element(By.CLASS_NAME, "question")
        answers_form = driver.find_element(By.CLASS_NAME, "answers")
        options = answers_form.find_elements(By.TAG_NAME, "input")
        labels = answers_form.find_elements(By.TAG_NAME, "label")
    except Exception:
        break

    question = q_el.text.split(":", 1)[-1].strip()
    answers = []
    for label in labels:
        answers.append(label.text.strip())
    if not answers:
        break

    input_type = options[0].get_attribute("type")
    multi = input_type == "checkbox"
    selected_indices = ask_gemini(question, answers, multi)

    for i, opt in enumerate(options):
        if i in selected_indices:
            opt.click()
        else:
            # Ensure unchecked for checkboxes
            if multi and opt.is_selected():
                opt.click()

    # Click submit
    submit_btn = driver.find_element(By.CLASS_NAME, "submit-btn")
    submit_btn.click()
    time.sleep(1)  # Adjust if needed for UI/JS lag

    # Check for end of quiz
    if "Quiz completed" in driver.page_source:
        print("Quiz finished.")
        break

# print(q_el.text)
time.sleep(10)
driver.quit()