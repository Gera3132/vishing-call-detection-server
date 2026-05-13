import os
from sentence_transformers import SentenceTransformer
from joblib import load
import logging

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(
    BASE_DIR,
    "modelos",
    "classifier_lr_balanced.joblib"
)

logging.warning("Cargando SBERT...")

sbert = SentenceTransformer(
    "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
    cache_folder="/opt/render/project/.cache"
)

print("Cargando clasificador...")

clf = load(MODEL_PATH)

logging.warning("Modelo cargado correctamente")


def predecir_texto(texto):

    emb = sbert.encode(
        [texto],
        normalize_embeddings=True
    )

    proba = clf.predict_proba(emb)[0][1]

    return round(float(proba) * 100, 2)