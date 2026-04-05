# python Image

FROM python:3.14-slim

# Set the working directory in the container

WORKDIR /app

# Copy the requirements file and install dependencies

COPY requirements.txt .

# Install dependencies using uv
RUN pip install uv
RUN uv venv
RUN uv pip install -r requirements.txt

# Copy application code
COPY . .

# Expose the port the server runs on
EXPOSE 8000

# Command to run the server
CMD ["uv", "run", "main.py"]
