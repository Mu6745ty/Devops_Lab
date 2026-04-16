# 1. Base image (lightweight Python 3.9)
FROM python:3.9-slim


# 2. Set working directory inside container
WORKDIR /app


# 3. Copy requirements file first (for caching dependencies)
COPY requirements.txt .


# 4. Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt


# 5. Copy all project files into container
COPY . .


# 6. Expose Flask port
EXPOSE 5000


# 7. Run the application
CMD ["python", "app.py"]
