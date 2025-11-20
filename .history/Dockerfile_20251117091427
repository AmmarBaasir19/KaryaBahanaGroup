## Base Image for Streamlit 
FROM python:3.10-slim

## Set working directory
WORKDIR /app_streamlit

## Install OS Dependencies for OpenCV 
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglu1-mesa \
    libopengl0 \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender1 \
    mesa-utils \
    && rm -rf /var/lib/apt/lists/*

## Copy requirements file 
COPY requirements.txt .

## Install Dependencies
RUN pip install --no-cache-dir -r requirements.txt

##Copy all projects file
COPY . .

## Expose Streamlit ports
EXPOSE 8505 

# Run Streamlit 
CMD ["streamlit", "run", "MainNew.py", "--server.address=0.0.0.0"]