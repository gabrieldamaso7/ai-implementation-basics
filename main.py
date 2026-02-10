from llm_client import ask_llm, summarize_text

def main():

    print("paste text to summarize (end with an empty line):")

    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    text = "\n".join(lines)

    try:
        summary = summarize_text(text)
        print("\n--- Summary ---")
        print(summary)


        #user_input = input("Ask the LLM something: ")
        #answer = ask_llm(user_input)
        #print("\n--- LLM Response ---")
        #print(answer)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()