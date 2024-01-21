# As Scrapy runs on Python, I choose the official Python 3 Docker image.
FROM python:3
# Set the working directory to /usr/src/app.
RUN mkdir /scrapy-code
WORKDIR /scrapy-code
ENV PYTHONPATH "${PYTHONPATH}:/scrapy-code"
 
# Copy the file from the local host to the filesystem of the container at the working directory.
COPY /scrapy/requirements.txt /scrapy-code
 
# Install Scrapy specified in requirements.txt.
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the project source code from the local host to the filesystem of the container at the working directory.
COPY . /scrapy-code
EXPOSE 8000
RUN pwd
# Run the crawler when the container launches.
CMD [ "python", "./mycrawler/go_spider.py" ]