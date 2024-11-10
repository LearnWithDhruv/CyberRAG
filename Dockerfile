# Use Python 3.11 as the base image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . .

# Expose a port if necessary (optional, for example if you want to expose an API endpoint)
# EXPOSE 8000

# Set environment variables if needed (optional)
# ENV MONGO_URI="your_mongodb_uri" CHROMA_PATH="path_to_chroma_vectors" OPENAI_API_KEY="your_openai_api_key"

# Run the main script
CMD ["python", "src/main.py"]
