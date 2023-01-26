FROM python:3.9

ENV WORKDIR_NAME=simple_app
WORKDIR /$WORKDIR_NAME

COPY ./requirements.txt /$WORKDIR_NAME/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /$WORKDIR_NAME/requirements.txt

COPY ./ /$WORKDIR_NAME

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]