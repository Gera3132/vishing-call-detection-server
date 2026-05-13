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

print("BUCKET:", BUCKET)
print("REGION:", REGION)
print("ACCESS KEY:", AWS_ACCESS_KEY_ID)

s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=REGION
)


def subir_audio_s3(audio_file):

    try:

        nombre = f"audios/{uuid.uuid4()}.mp4"

        print("Subiendo archivo:", nombre)

        s3.upload_fileobj(
            audio_file,
            BUCKET,
            nombre
        )

        print("SUBIDA EXITOSA")

        return f"https://{BUCKET}.s3.amazonaws.com/{nombre}"

    except Exception as e:

        print("ERROR S3:", str(e))

        raise e