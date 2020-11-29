# Base Image
FROM python:3.7.9

# Copying contents to the container
COPY . ./app



#Installing Required packages for running application

RUN pip install --no-cache-dir -r app/requirements.txt

#Working directory
WORKDIR /app/src

EXPOSE 8000

# Command to execute docker container
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]







