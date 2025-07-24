from .runner.runner import Runner


def main():
    runner = Runner()
    print("Welcome to Career Mentor Agent 🚀 (type 'exit' to quit)")

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Good Bye")
            break

        result = runner.run(user_input)
        print(f"\nAgent ({result['agent']}): {result['response']}")


# def main():
#     print("Hello World")


# if __name__ == "__main__":
#     main()
