"""
Script de prueba para el detector AMD
Simula diferentes escenarios de llamada
"""
import sys
sys.path.insert(0, '.')

from app.amd_detector import AMDDetector

def test_detector():
    print("Cargando modelo Vosk...")
    detector = AMDDetector()
    print("Modelo cargado!\n")

    # Casos de prueba
    test_cases = [
        # (texto, duracion_habla, resultado_esperado)
        ("hola", 0.5, "HUMAN"),
        ("alo", 0.3, "HUMAN"),
        ("digame", 0.4, "HUMAN"),
        ("si bueno", 0.6, "HUMAN"),
        ("quien habla", 0.8, "HUMAN"),

        ("el numero que usted marco no se encuentra disponible", 3.5, "MACHINE"),
        ("deje su mensaje despues del tono", 2.8, "MACHINE"),
        ("buzon de voz por favor deje su mensaje", 3.0, "MACHINE"),
        ("gracias por llamar en este momento no podemos atenderle", 4.0, "MACHINE"),
        ("bienvenido ha comunicado con el buzon de mensajes", 3.5, "MACHINE"),

        ("", 0, "UNKNOWN"),
    ]

    print("=" * 60)
    print("PRUEBAS DE DETECCION AMD")
    print("=" * 60)

    passed = 0
    failed = 0

    for texto, duracion, esperado in test_cases:
        result = detector.analyze_transcription(texto, duracion)

        status = "OK" if result["result"] == esperado else "FAIL"
        if status == "OK":
            passed += 1
        else:
            failed += 1

        print(f"\n[{status}] Texto: '{texto[:40]}...' " if len(texto) > 40 else f"\n[{status}] Texto: '{texto}'")
        print(f"     Esperado: {esperado}, Obtenido: {result['result']} (confianza: {result['confidence']:.2f})")
        print(f"     Razon: {result['reason']}")

    print("\n" + "=" * 60)
    print(f"RESULTADO: {passed}/{passed+failed} pruebas pasaron")
    print("=" * 60)

    return failed == 0


if __name__ == "__main__":
    success = test_detector()
    sys.exit(0 if success else 1)
