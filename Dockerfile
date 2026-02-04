#This is the building stage where I'm specifying Python
FROM python:3.12-slim AS builder

#I'm setting the working directory
WORKDIR /app

# This copies the requirements first to leverage Docker cache
COPY requirements.txt .

# This will install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# This copies the app code
COPY . .

#Now this is the runtime stage where it's mostly the same steps
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy installed dependencies from builder
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /app /app

#I'm installing pytest in the runtime
RUN pip install --no-cache-dir pytest

# This port will be for Docker (configurable via env)
ENV PORT=5050
EXPOSE ${PORT}

# This runs the app
CMD ["python", "flaskcoursework_app.py"]
