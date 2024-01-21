FROM python:3
RUN mkdir /backend-code
WORKDIR /backend-code
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH "${PYTHONPATH}:/backend-code "
COPY /backend/requirements.txt /backend-code
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /backend-code
EXPOSE 5000
CMD [ "python", "app.py" ]