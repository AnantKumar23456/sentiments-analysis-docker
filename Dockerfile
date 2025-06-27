# FROM python:3.12
# WORKDIR /usr/local/app

# # Install the application dependencies
# COPY requirements.txt ./
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy in the source code
# COPY . .
# EXPOSE 5000

# # Setup an app user so the container doesn't run as the root user
# RUN useradd app
# USER app

# # CMD docker run -it 01_sentiments_analysis.py
# # CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]

# # CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]

# CMD ["uvicorn", "01_sentiment_analysis:app", "--host", "0.0.0.0", "--port", "8080"]








# FROM python:3.12
# WORKDIR /usr/local/app

# # Install dependencies
# COPY requirements.txt ./
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy source code
# COPY . .

# # Create NLTK directory and set environment variable
# RUN mkdir -p /home/app/nltk_data
# ENV NLTK_DATA=/home/app/nltk_data

# # Add a non-root user
# RUN useradd app
# USER app

# EXPOSE 8080

# # Run the app
# CMD ["uvicorn", "01_sentiment_analysis:app", "--host", "0.0.0.0", "--port", "8080"]






FROM python:3.12
WORKDIR /usr/local/app

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy your source code
COPY . .

# Create the NLTK directory and set permissions
RUN mkdir -p /home/app/nltk_data && chown -R 1000:1000 /home/app/nltk_data
ENV NLTK_DATA=/home/app/nltk_data

# Add a non-root user (UID 1000 so it matches chown)
RUN useradd -u 1000 app
USER app

EXPOSE 8080

# Start the FastAPI app
CMD ["uvicorn", "01_sentiment_analysis:app", "--host", "0.0.0.0", "--port", "8080"]
