FROM python:3.8

# Set the working directory to the new directory
WORKDIR /app

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the script
CMD ["python", "main.py"]
