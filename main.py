from llm_client import ask_llm

def main():

    try:
        user_input = input("Ask the LLM something: ")
        answer = ask_llm(user_input)
        print("\n--- LLM Response ---")
        print(answer)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()