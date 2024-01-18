FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /backend
WORKDIR /backend
COPY requirements.txt /backend
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /backend
EXPOSE 5000
CMD [ "python", "app.py" ]