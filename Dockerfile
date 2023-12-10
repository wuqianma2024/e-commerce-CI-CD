# Use an official Python runtime as a parent image
FROM python



# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1




# Install Google Chrome
RUN apt-get update && apt-get install -y wget gnupg2
RUN wget -q https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/120.0.6099.71/linux64/chrome-linux64.zip
RUN unzip chrome-linux64.zip -d /usr/bin
RUN rm chrome-linux64.zip

# Install ChromeDriver
RUN wget -q https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/120.0.6099.71/linux64/chromedriver-linux64.zip
RUN unzip chromedriver_linux64.zip -d /usr/bin
RUN rm chromedriver_linux64.zip

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
