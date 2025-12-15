#!/bin/bash

# Script para ejecutar el servicio AMD

# Activar entorno virtual si existe
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# Variables de entorno
export VOSK_MODEL_PATH=${VOSK_MODEL_PATH:-"models/vosk-model-small-es-0.42"}
export AMD_HOST=${AMD_HOST:-"0.0.0.0"}
export AMD_PORT=${AMD_PORT:-"8765"}

echo "==================================="
echo "  AMD Service - Deteccion Buzon"
echo "==================================="
echo "Modelo: $VOSK_MODEL_PATH"
echo "Puerto: $AMD_PORT"
echo ""

# Ejecutar servidor
python -m app.main
