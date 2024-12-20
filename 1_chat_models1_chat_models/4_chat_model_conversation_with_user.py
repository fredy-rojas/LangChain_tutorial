from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage

# Load environment variables from .env
load_dotenv()

# Create a ChatOpenAI model
model = ChatOpenAI(model="gpt-4o-2024-08-06")


chat_history = []  # Use a list to store messages

# Set an initial system message (optional)
system_message = SystemMessage(content="You are a helpful AI assistant.")
chat_history.append(system_message)  # Add system message to chat history

# Chat loop
print("================= START CHAT =================\n\n")
while True:
    query = input("\nYou: ")
    if query.lower() == "exit":
        print("\n\n================= END CHAT =================\n\n")
        break
    chat_history.append(HumanMessage(content=query))  # Add user message

    # Get AI response using history
    result = model.invoke(chat_history)
    response = result.content
    chat_history.append(AIMessage(content=response))  # Add AI message

    print(f"\nAI: {response}")


print("================= Message History =================")
print(chat_history)
