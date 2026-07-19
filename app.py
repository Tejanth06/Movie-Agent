from agent import MovieAgent

agent = MovieAgent()

while True:

    user_message = input("\nYou: ")

    if user_message.lower() == "exit":
        print("👋 Goodbye!")
        break

    response = agent.chat(user_message)

    print("\nAgent:")
    print(response)