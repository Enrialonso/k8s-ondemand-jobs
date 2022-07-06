import json
import os
import socket

from flask import Flask
from kubernetes import client, config
from loguru import logger

from utils import create_job_object, create_job

app = Flask(__name__)


@app.route("/status")
def status():
    return "OK!"


@app.route("/")
def home():
    return f"flask-api - on host: {socket.gethostname()}"


@app.route("/get-pods")
def get_pods():
    config.load_incluster_config()
    k8s_api = client.CoreV1Api()
    res = k8s_api.list_namespaced_pod(namespace="default")
    pods = []
    for i in res.items:
        pods.append(i.metadata.name)
        logger.warning(f"{i.metadata.namespace}\t{i.metadata.name}")
    return json.dumps(pods, default=str)


@app.route("/launch-job")
def launch_job():
    if os.getenv("LOCAL"):
        config.load_config()
    else:
        config.load_incluster_config()
    batch_v1 = client.BatchV1Api()
    job = create_job_object()
    create_job(batch_v1, job)
    return "OK!"


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.getenv("PORT_API") if os.getenv("PORT_API") else "8000"),
    )
