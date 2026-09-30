import sys
// Autor: Sergio <sergio@uco.es>
nombre = sys.argv[1] if len(sys.argv) > 1 else "Mundo"
print(f"Hola, {nombre}")