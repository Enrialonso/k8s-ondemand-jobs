from uuid import uuid4

from kubernetes import client


def create_job_object():
    container = client.V1Container(
        name="job-python", image="python-job", image_pull_policy="Never"
    )
    template = client.V1PodTemplateSpec(
        metadata=client.V1ObjectMeta(labels={"name": "cron-job-python"}),
        spec=client.V1PodSpec(restart_policy="Never", containers=[container]),
    )
    spec = client.V1JobSpec(template=template, ttl_seconds_after_finished=60)
    job = client.V1Job(
        api_version="batch/v1",
        kind="Job",
        metadata=client.V1ObjectMeta(name=f"job-python-{str(uuid4())}"),
        spec=spec,
    )

    return job


def create_job(api_instance, job):
    api_response = api_instance.create_namespaced_job(body=job, namespace="default")
    print("Job created. status='%s'" % str(api_response.status))
