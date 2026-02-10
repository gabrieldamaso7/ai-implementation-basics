import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def summarize_text(text: str) -> str:
    if not text or not text.strip():
        raise ValueError("Text cannot be empty or whitespace.")
    
    prompt = ("You are a professional assistant.\n"
              "Summarize the following text in exactly 3 bullet points:\n"
              "Do not add new information.\n"
              f"{text}"
            )
    return ask_llm(prompt)

def ask_llm(prompt: str) -> str:
    if not prompt or not prompt.strip():
        raise ValueError("Prompt cannot be empty or whitespace.")
    
    system_propmt = (
        "You are a Senior AI Implementation Engineer."
    )

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
                {"role": "system", "content": system_propmt},
                {"role": "user", "content": prompt},
            ] ,
        temperature=0.2, # 0 for deterministic output, 1 for more creative output
        max_tokens=200, 
        timeout=10, # seconds  
    )
    usage = response.usage
    print(f"Tokens used: {usage.total_tokens}")

    # print(f"LLM Response: {response}")
    return response.choices[0].message.content