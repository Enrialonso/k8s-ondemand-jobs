FROM python:3.8-alpine
WORKDIR job
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "job.py"]