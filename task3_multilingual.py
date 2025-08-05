from googletrans import Translator

# Dummy knowledge base
knowledge_base = {
    "what is python": "Python is a popular programming language.",
    "what is ai": "AI stands for Artificial Intelligence.",
    "what is machine learning": "Machine learning is a subset of AI focused on algorithms that learn from data."
}

# Function to get answer
def get_answer(question):
    question = question.lower().strip()
    return knowledge_base.get(question, "I'm sorry, I don't know the answer to that.")

# Multilingual response function
def multilingual_chat():
    translator = Translator()
    
    print("Multilingual Chatbot (type 'exit' to quit)")
    print("You can ask questions like: 'What is Python?', 'What is AI?', etc.")
    
    while True:
        user_input = input("\nAsk a question: ")
        if user_input.lower() == 'exit':
            break
        
        # Detect language
        detected = translator.detect(user_input)
        src_lang = detected.lang
        
        # Translate question to English
        translated_question = translator.translate(user_input, src='auto', dest='en').text
        print(f"Detected language: {src_lang} | Translated to English: {translated_question}")
        
        # Get answer
        answer = get_answer(translated_question)
        
        # Translate answer back to original language
        translated_answer = translator.translate(answer, src='en', dest=src_lang).text
        print(f"Answer ({src_lang}): {translated_answer}")

# Run the chatbot
if __name__ == "__main__":
    multilingual_chat()
