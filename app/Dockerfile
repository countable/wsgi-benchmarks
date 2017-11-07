FROM python:3

RUN apt-get update && apt-get install -y libev-dev

# Copying the requirements for installation to take
# advantage of the caching.
COPY requirements.txt .
RUN pip install -r ./requirements.txt
