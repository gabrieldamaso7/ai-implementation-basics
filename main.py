from llm_client import ask_llm, summarize_text, summarize_text_structured, decide_action

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
        decision = decide_action(text)

        print("\n--- Decision ---")
        print(decision)
        
        if decision["action"] == "summarize_text":
            result = summarize_text_structured(text)
        elif decision["action"] == "explain_text":
            result = ask_llm(text) 
        else:
            print("Request rejected: ", decision["reason"])
            return

        print("\n--- Result ---")
        print(result)

        #print("\n--- Summary ---")
        #print(f"\nSummary: {result['summary']}")
        #print(f"\nKey Points: ")
        #for p in result['key_points']:
        #    print(f"- {p}")
        #print(f"Confidence: {result['confidence']}")

        #user_input = input("Ask the LLM something: ")
        #answer = ask_llm(user_input)
        #print("\n--- LLM Response ---")
        #print(answer)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()