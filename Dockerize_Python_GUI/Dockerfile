FROM python:3.9-slim

WORKDIR /app

# To use requirement.txt file
# COPY requirement.txt . 

# RUN pip install -r requirement.txt

# Copy from this directory into working directory
COPY . . 

RUN apt-get update && apt-get install -y libx11-6 libext-dev libxrender-dev libxinerama-dev libxrandr-dev libxcursor-dev libxtst-dev tk-dev && rm- rf /var/lib/apt/lists/*

CMD ["python", "main.py"]