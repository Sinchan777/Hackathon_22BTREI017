from src.voice import VoiceEngine
from src.search import WebSearch

def main():
    voice = VoiceEngine()
    searcher = WebSearch()
    
    print("Assistant ready. Ask your question...")
    while True:
        try:
            query = voice.listen()
            if not query:
                continue
                
            result = searcher.simple_search(query)
            voice.speak(result[:300])
            
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break