import os

# Ruta al modelo Vosk
VOSK_MODEL_PATH = os.getenv("VOSK_MODEL_PATH", "models/vosk-model-small-es-0.42")

# Configuracion AMD
AMD_DECISION_TIMEOUT_SECONDS = 3.5  # Tiempo maximo para tomar decision
AMD_MIN_SPEECH_FOR_MACHINE = 2.5    # Si habla mas de 2.5s continuo = maquina

# Palabras clave que indican buzon de voz
VOICEMAIL_KEYWORDS = [
    # Espanol
    "mensaje", "buzón", "buzon", "tono", "ocupado", "disponible",
    "después del", "despues del", "deje su", "deja tu", "no se encuentra",
    "fuera de servicio", "no está disponible", "no esta disponible",
    "vuelva a llamar", "intentelo más tarde", "intentelo mas tarde",
    "número que usted marcó", "numero que usted marco",
    "en este momento", "por favor", "gracias por llamar",
    "horario de atención", "horario de atencion",
    "marque la extensión", "marque la extension",
    "bienvenido", "ha comunicado con", "ha llamado a",
    # Ingles (por si acaso)
    "voicemail", "leave a message", "after the tone", "beep",
    "not available", "please call back"
]

# Puerto del servidor
SERVER_HOST = os.getenv("AMD_HOST", "0.0.0.0")
SERVER_PORT = int(os.getenv("AMD_PORT", "8765"))
