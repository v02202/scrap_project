FROM python:3
RUN mkdir /backend
WORKDIR /backend
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH "${PYTHONPATH}:/backend "
COPY /backend/requirements.txt /backend
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /backend
EXPOSE 5000
CMD [ "python", "app.py" ]