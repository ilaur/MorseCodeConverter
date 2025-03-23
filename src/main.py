from morse_code import MorseCode

# Max characters limit for clear display of the output
MAX_LENGTH = 512

def main() -> None:
    """Main entry point of the program"""
    text_message = input("Input message (type '/exit' to close): ")
    morse_code = MorseCode()

    try:
        while text_message != "/exit":
            if len(text_message) > MAX_LENGTH:
                raise RuntimeError(f"Charaters limit of {MAX_LENGTH} exceeded.")
            print("Encoded Morse Code:")
            print(morse_code.encode(text_message))
            text_message = input("Input message: ")
    except RuntimeError as error:
        print(error)


if __name__ == "__main__":
    main()