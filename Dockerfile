FROM python:3-slim


WORKDIR /app
COPY . /app

RUN pip install --upgrade pip
RUN pip install -Ur /app/requirements.txt && \
    pip install -e .

ENTRYPOINT ["photo-album"]