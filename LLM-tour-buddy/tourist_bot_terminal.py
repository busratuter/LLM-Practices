from langchain.chat_models import ChatOllama
from langchain.schema import HumanMessage, SystemMessage
from langchain.memory import ConversationBufferMemory

llm = ChatOllama(model = "llama3.2:3b")

memory = ConversationBufferMemory(return_messages=True)

print("Welcome to the Tourist Guide Bot!")
print("I can help you with information about tourist attractions, local culture, and travel tips.")

while True:

    user_input = input("You: ")

    if user_input.lower() == "quit":
        print("Thank you for using the Tourist Guide Bot. Goodbye!")
        break

    memory.chat_memory.add_user_message(user_input)

    messages = [
        SystemMessage(content="You are a helpful and knowledgeable AI travel assistant specialized in Turkey. Your goal is to guide users through Turkey's rich history, cultural sites, local cuisine, traditions, transportation, and travel tips. Always provide clear, friendly, and accurate information. Offer personalized suggestions based on user preferences when possible. If users ask about cities, landmarks, food, or travel plans within Turkey, respond with relevant, engaging, and useful guidance.")
        ] + memory.load_memory_variables({})["history"] + [HumanMessage(content=user_input)]
    
    response = llm(messages)

    memory.chat_memory.add_ai_message(response.content)

    print(f"AI Guide: {response.content}")



    
