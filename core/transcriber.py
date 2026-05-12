import boto3
import time
import requests
import uuid

import os

AWS_ACCESS_KEY_ID = os.getenv(
    "AWS_ACCESS_KEY_ID"
)

AWS_SECRET_ACCESS_KEY = os.getenv(
    "AWS_SECRET_ACCESS_KEY"
)

REGION = "us-east-1"

BUCKET = "TU_BUCKET"

transcribe = boto3.client(
    "transcribe",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=REGION
)


def transcribir_audio(audio_uri):

    job_name = f"job-{uuid.uuid4()}"

    transcribe.start_transcription_job(
        TranscriptionJobName=job_name,
        Media={
            "MediaFileUri": audio_uri
        },
        MediaFormat="3gp",
        LanguageCode="es-MX"
    )

    while True:

        status = transcribe.get_transcription_job(
            TranscriptionJobName=job_name
        )

        estado = status["TranscriptionJob"]["TranscriptionJobStatus"]

        if estado == "COMPLETED":

            url = status["TranscriptionJob"][
                "Transcript"
            ]["TranscriptFileUri"]

            data = requests.get(url).json()

            texto = data["results"]["transcripts"][0]["transcript"]

            return texto

        elif estado == "FAILED":

            return "ERROR"

        time.sleep(2)