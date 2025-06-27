# import nltk
# from nltk.sentiment import SentimentIntensityAnalyzer
# import ssl

# try:
#     _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#     pass
# else:
#     ssl._create_default_https_context = _create_unverified_https_context
# nltk.download('vader_lexicon') 
# nltk.download('punkt')

# def perform_semantic_analysis(text):
#     sid = SentimentIntensityAnalyzer()
#     sentiment_score = sid.polarity_scores(text)

#     if sentiment_score['compound'] >= 0.05:
#         return "Positive"
#     elif sentiment_score['compound'] <= -0.05:
#         return "Negative"
#     else:
#         return "Neutral"

# if __name__ == "__main__":
#     while True:
#         input_text = input("Enter the text for semantic analysis (type 'exit' to end): ")

#         if input_text.lower() == 'exit':
#             print("Exiting...")
#             break

#         result = perform_semantic_analysis(input_text)
#         print(f"Sentiment: {result}")



from fastapi import FastAPI
from pydantic import BaseModel
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import ssl

# Handle SSL issue for NLTK downloads
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

# Download required models
nltk.download('vader_lexicon')
nltk.download('punkt')

# Create Sentiment Analyzer
sid = SentimentIntensityAnalyzer()

# Initialize FastAPI
app = FastAPI()

# Request body model
class TextInput(BaseModel):
    text: str

# API route
@app.post("/analyze")
def analyze_sentiment(data: TextInput):
    sentiment_score = sid.polarity_scores(data.text)
    
    if sentiment_score['compound'] >= 0.05:
        sentiment = "Positive"
    elif sentiment_score['compound'] <= -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    
    return {
        "input_text": data.text,
        "sentiment": sentiment,
        "score": sentiment_score
    }
