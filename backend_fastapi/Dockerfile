FROM python:3.10-slim


COPY . /tomato_classifier/backend
#set working directory
WORKDIR /tomato_classifier/backend

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

#install dependencies
RUN pip install -r requirement.txt

EXPOSE 8000

ENTRYPOINT [ "python" ]
CMD ["main.py"]