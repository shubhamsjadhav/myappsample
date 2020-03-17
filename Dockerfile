FROM python:latest
WORKDIR .
EXPOSE 5000
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python3", "accessdb.py"]
