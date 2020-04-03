FROM python:3.7.7-alpine3.10

WORKDIR /webinar

RUN mkdir templates
COPY handle_input.html templates/
COPY webinar.py .
COPY requirements.txt .

RUN pip install --upgrade pip && pip install --trusted-host pypi.python.org -r requirements.txt

ENV FLASK_APP webinar.py

CMD ["python", "webinar.py"]
