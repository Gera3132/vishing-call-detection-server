import boto3
import uuid

import os

AWS_ACCESS_KEY_ID = os.getenv(
    "AWS_ACCESS_KEY_ID"
)

AWS_SECRET_ACCESS_KEY = os.getenv(
    "AWS_SECRET_ACCESS_KEY"
)

BUCKET = os.getenv(
    "AWS_BUCKET_NAME"
)

REGION = os.getenv(
    "AWS_REGION"
)

s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=REGION
)


def subir_audio_s3(audio_file):

    nombre = f"audios/{uuid.uuid4()}.3gp"

    s3.upload_fileobj(
        audio_file,
        BUCKET,
        nombre
    )

    return f"https://{BUCKET}.s3.amazonaws.com/{nombre}"