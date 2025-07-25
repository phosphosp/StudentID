FROM python:3.11-slim

# install git
RUN apt-get update && apt-get install -y git

# set global Git identity
RUN git config --global user.name "Cornelius Fam Kai Rui" \
    && git config --global user.email "2301868@sit.singaporetech.edu.sg"

# set working directory
WORKDIR /app

# copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy app code
COPY . .

# expose port
EXPOSE 5000

# run Flask app
CMD ["python", "app/main.py"]