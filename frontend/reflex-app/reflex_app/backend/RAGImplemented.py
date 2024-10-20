import os
import openai
import chromadb
from dotenv import load_dotenv
from deepgram import DeepgramClient, SpeakOptions
from pydub import AudioSegment
from playsound import playsound

load_dotenv()

openai.api_key = os.getenv("OPEN_AI_API_KEY")
deepgram_api = os.getenv("DG_API_KEY")

client = chromadb.PersistentClient(path="diary_vectordb")
collection_name = "dairy-collection"
collection = client.get_or_create_collection(name=collection_name)

# Function to get embedding using OpenAI API
def get_embedding(text):
    response = openai.Embedding.create(
        input=text,
        model="text-embedding-ada-002"
    )
    return response['data'][0]['embedding']

# Function to split text into smaller chunks (e.g., sentences or paragraphs)
def split_text(text, chunk_size=100):
    words = text.split()
    chunks = [" ".join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]
    return chunks

# Process all text files in a folder, split into chunks, and store in ChromaDB
def process_documents(data_folder):
    for filename in os.listdir(data_folder):
        if filename.endswith(".txt"):
            file_path = os.path.join(data_folder, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()

                # Split text into chunks
                chunks = split_text(text, chunk_size=200)
                for i, chunk in enumerate(chunks):
                    embedding = get_embedding(chunk)
                    doc_id = f"{filename}_{i}"
                    collection.add(documents=[chunk], embeddings=[embedding], ids=[doc_id])

            print(f"Processed {filename}")

            # Move file to a processed folder
            destination = os.path.join(data_folder, 'embedding_generated')
            os.makedirs(destination, exist_ok=True)
            os.rename(file_path, os.path.join(destination, filename))

    print("All documents have been processed and stored in ChromaDB.")

# Query ChromaDB for similar documents based on the query
def query_documents(query_text, n_results=3):
    query_embedding = get_embedding(query_text)
    results = collection.query(query_embeddings=[query_embedding], n_results=n_results)
    return results['documents'][0] if 'documents' in results else []

# Generate a response using an LLM
def generate_llm_response(query, context_chunks):
    context = "\n".join(context_chunks)
    prompt = f"Based on the following context:\n{context}\nAnswer the following question, keep the answer simple and short:\n{query}"
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    
    return response['choices'][0]['message']['content']

# RAG pipeline: Retrieve relevant chunks from ChromaDB and generate response
def rag_pipeline(query):
    relevant_chunks = query_documents(query)
    return generate_llm_response(query, relevant_chunks)

# Generate text-to-speech using Deepgram API
def text_to_speech(response_text, output_file="output.wav"):
    deepgram = DeepgramClient(api_key=deepgram_api)
    options = SpeakOptions(model="aura-asteria-en", encoding="linear16", container="wav")
    speak_options = {"text": response_text}
    
    try:
        response = deepgram.speak.v("1").save(output_file, speak_options, options)
        print(response.to_json(indent=4))
    except Exception as e:
        print(f"Error during text-to-speech generation: {e}")

# Play the audio file
def play_audio(file_path):
    playsound(file_path)

# Example usage
if __name__ == "__main__":

    process_documents("./data")

    # Example query text for RAG pipeline
    query_text = "Why did I use rollercoaster in my project?"
    response_text = rag_pipeline(query_text)
    
    print(f"\nRAG Response: {response_text}\n")

    output_file = "output.wav"
    text_to_speech(response_text, output_file)
    play_audio(output_file)
