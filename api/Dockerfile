FROM python:3.8-alpine
ENV PORT_API=8000
WORKDIR api
COPY . .
RUN pip install -r requirements.txt
EXPOSE ${PORT_API}
CMD ["python", "api.py"]