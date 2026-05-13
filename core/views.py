#from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .s3_utils import subir_audio_s3
from .transcriber import transcribir_audio
from .predictor import predecir_texto


@csrf_exempt
def analyze_audio(request):
    print("Request recibida analyze_audio")

    if request.method != "POST":

        return JsonResponse({
            "error": "POST only"
        })

    try:
        print("Estamos en el try")
        audio = request.FILES.get("audio")

        if not audio:

            return JsonResponse({
                "error": "No audio"
            })

        # Subir S3
        print("Subiendo audio")
        audio_url = subir_audio_s3(audio)
        print("Audio subido:", audio_url)

        # Transcribir
        print("Transcribiendo...")
        texto = transcribir_audio(audio_url)
        print("Texto:", texto)

        # IA
        print("Calculando riesgo...")
        riesgo = predecir_texto(texto)
        print("Riesgo:", riesgo)

        return JsonResponse({

            "riesgo": riesgo,

            "transcripcion": texto
        })

    except Exception as e:

        return JsonResponse({

            "error": str(e)
        })
