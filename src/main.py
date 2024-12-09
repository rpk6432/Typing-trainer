import time
from logic import load_texts, count_errors, calculate_speed

def main():
    texts = load_texts("data/texts.json")
    text = texts["easy"]
    print("Type the following text:")
    print(text)

    input("Press Enter to start...")
    start_time = time.time()
    user_input = input("> ")
    elapsed_time = time.time() - start_time

    errors = count_errors(text, user_input)
    speed = calculate_speed(len(user_input), elapsed_time)

    print(f"\nResults:\nErrors: {errors}\nSpeed: {speed:.2f} characters per minute")

if __name__ == "__main__":
    main()