import sys
// Autor: Sergio <sergio@uco.es>

from HolaMundo import HolaMundo

nombre = sys.argv[1] if len(sys.argv) > 1 else "Mundo"
print(HolaMundo(nombre))