from text_utils import analyze_text, count_words


def main():
    try:
        user_input = input("Enter a message: ")
        result = analyze_text(user_input)
        for key, value in result.items():
            print(f"{key}: {value}")

        word_count = count_words(user_input)
        print(f"Word count: {word_count}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()