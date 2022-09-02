FROM python:3-buster
RUN pip install --upgrade pip
WORKDIR /code
RUN pip install Pillow
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./src ./src/
COPY ./src/main.py ./main.py
COPY ./src/app/app.py ./app.py
CMD ["python", "main.py"]
