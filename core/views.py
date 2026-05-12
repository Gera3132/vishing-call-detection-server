#from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .s3_utils import subir_audio_s3
from .transcriber import transcribir_audio
from .predictor import predecir_texto


@csrf_exempt
def analyze_audio(request):

    if request.method != "POST":

        return JsonResponse({
            "error": "POST only"
        })

    try:

        audio = request.FILES.get("audio")

        if not audio:

            return JsonResponse({
                "error": "No audio"
            })

        # Subir S3
        audio_url = subir_audio_s3(audio)

        # Transcribir
        texto = transcribir_audio(audio_url)

        # IA
        riesgo = predecir_texto(texto)

        return JsonResponse({

            "riesgo": riesgo,

            "transcripcion": texto
        })

    except Exception as e:

        return JsonResponse({

            "error": str(e)
        })
