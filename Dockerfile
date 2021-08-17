FROM python:3.9

WORKDIR /app
COPY pyproject.toml poetry.lock main.py ./

RUN pip install --no-cache-dir poetry==1.2.0a2 && \
    poetry config virtualenvs.create false --local && \
    poetry install --no-root --without dev

CMD [ "gunicorn", "--bind=0.0.0.0:8000", "--access-logfile=-", "--error-logfile=-", "main:app" ]
