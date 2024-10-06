from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_anthropic import ChatAnthropic
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage

# Setup environment variables and messages
load_dotenv()

messages = [
    SystemMessage(content="Solve the following math problems"),
    HumanMessage(content="What is 81 divided by 9?"),
]


# ---- LangChain OpenAI Chat Model Example ----

# Create a ChatOpenAI model
model = ChatOpenAI(model="gpt-4o-2024-08-06")

# Invoke the model with messages
result = model.invoke(messages)
print(f"\n\n============================\nAnswer from OpenAI: {result.content}\n============================\n\n")


# # ---- Anthropic Chat Model Example ----

# # Create a Anthropic model
# # Anthropic models: https://docs.anthropic.com/en/docs/models-overview
# # model = ChatAnthropic(model="claude-3-opus-20240229")
# model = ChatAnthropic(model="claude-3-sonnet-20240229")

# result = model.invoke(messages)
# print(f"Answer from Anthropic: {result.content}")


# # ---- Google Chat Model Example ----

# # https://console.cloud.google.com/gen-app-builder/engines
# # https://ai.google.dev/gemini-api/docs/models/gemini
# model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

# result = model.invoke(messages)
# print(f"Answer from Google: {result.content}")
