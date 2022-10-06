FROM python:3.10.6

WORKDIR /instagram
COPY . .

RUN pip install --upgrade pip
RUN pip install python-dotenv
RUN pip install -r requirements.txt

CMD [ "python3", "main.py" ]