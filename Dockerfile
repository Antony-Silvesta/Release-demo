# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Install dependencies
RUN apt-get update && \
    apt-get install -y wget unzip xvfb gnupg curl && \
    apt-get clean

# Install Chrome
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && \
    apt-get install -y google-chrome-stable

# Install Chrome WebDriver (make sure the version matches the Chrome version)
RUN CHROME_VERSION=$(google-chrome --version | awk '{print $3}') && \
    wget -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/$CHROME_VERSION/chromedriver_linux64.zip && \
    unzip /tmp/chromedriver.zip -d /usr/local/bin/ && \
    rm /tmp/chromedriver.zip

# Install Python packages (Selenium and other dependencies)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Set display port to avoid the need for a real display
ENV DISPLAY=:99

# Copy the test script to the container
COPY web_test.py /usr/src/app/

# Set the working directory
WORKDIR /usr/src/app/

# Run the Selenium tests
CMD ["python", "./web_test.py"]
