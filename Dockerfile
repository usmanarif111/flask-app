#Base Image
FROM python:3.11

#Working Directory
WORKDIR /app

#COPY Code
COPY . .

#Required Libraries
RUN pip install -r requirements.txt

# RUN
CMD ["python","app.py"]
