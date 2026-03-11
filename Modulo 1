"""
Sistema de Gestión de Cursos Universitarios
Etapa 1 - Aplicación de Consola
"""

# ─────────────────────────────────────────
#  Configuración del sistema
# ─────────────────────────────────────────
USUARIO_ADMIN = "admin"
CONTRASENA_ADMIN = "uni123"

alumnos = {}  # { nombre: cantidad_de_cursos }


# ─────────────────────────────────────────
#  Utilidades de presentación
# ─────────────────────────────────────────
def separador(caracter="─", longitud=50):
    print(caracter * longitud)

def encabezado(titulo):
    separador("═")
    print(f"  {titulo.upper()}")
    separador("═")

def pausa():
    input("\n  Presione ENTER para continuar...")


# ─────────────────────────────────────────
#  Módulo de autenticación
# ─────────────────────────────────────────
def iniciar_sesion():
    encabezado("Sistema Universitario de Cursos")
    print("  Por favor, ingrese sus credenciales.\n")

    intentos = 3
    while intentos > 0:
        usuario = input("  Usuario    : ").strip()
        contrasena = input("  Contraseña : ").strip()

        if usuario == USUARIO_ADMIN and contrasena == CONTRASENA_ADMIN:
            print("\n  ✔  Acceso concedido. Bienvenido, admin.\n")
            pausa()
            return True
        else:
            intentos -= 1
            print(f"\n  ✘  Credenciales incorrectas. Intentos restantes: {intentos}\n")

    print("\n  Acceso bloqueado. Demasiados intentos fallidos.")
    return False


# ─────────────────────────────────────────
#  Opción 1 – Dar de alta un alumno
# ─────────────────────────────────────────
def alta_alumno():
    encabezado("Registrar nuevo alumno")

    nombre = input("  Nombre del alumno : ").strip()
    if not nombre:
        print("  ✘  El nombre no puede estar vacío.")
        pausa()
        return

    if nombre.lower() in [a.lower() for a in alumnos]:
        print(f"  ✘  El alumno '{nombre}' ya está registrado.")
        pausa()
        return

    while True:
        try:
            cantidad = int(input("  Cantidad de cursos : "))
            if cantidad < 0:
                print("  ✘  La cantidad no puede ser negativa.")
            else:
                break
        except ValueError:
            print("  ✘  Ingrese un número válido.")

    alumnos[nombre] = cantidad
    separador()
    print(f"  ✔  Alumno '{nombre}' registrado con {cantidad} curso(s).")
    pausa()


# ─────────────────────────────────────────
#  Opción 2 – Ver listado de alumnos
# ─────────────────────────────────────────
def ver_listado():
    encabezado("Listado de alumnos")

    if not alumnos:
        print("  No hay alumnos registrados aún.")
        pausa()
        return

    print(f"  {'N°':<5} {'Nombre':<30} {'Cursos':>8}")
    separador()
    for i, (nombre, cursos) in enumerate(alumnos.items(), start=1):
        print(f"  {i:<5} {nombre:<30} {cursos:>8}")
    separador()
    print(f"  Total de alumnos registrados: {len(alumnos)}")
    pausa()


# ─────────────────────────────────────────
#  Opción 3 – Ver cursos por alumno
# ─────────────────────────────────────────
def ver_cursos_por_alumno():
    encabezado("Consultar cursos por alumno")

    if not alumnos:
        print("  No hay alumnos registrados aún.")
        pausa()
        return

    nombre = input("  Ingrese el nombre del alumno : ").strip()

    # Búsqueda insensible a mayúsculas
    coincidencia = next((k for k in alumnos if k.lower() == nombre.lower()), None)

    if coincidencia:
        separador()
        print(f"  Alumno : {coincidencia}")
        print(f"  Cursos : {alumnos[coincidencia]}")
        separador()
    else:
        print(f"  ✘  No se encontró el alumno '{nombre}'.")

    pausa()


# ─────────────────────────────────────────
#  Menú principal
# ─────────────────────────────────────────
def menu_principal():
    while True:
        encabezado("Menú Principal")
        print("  1. Registrar nuevo alumno")
        print("  2. Ver listado de alumnos")
        print("  3. Ver cursos por alumno")
        print("  0. Salir")
        separador()

        opcion = input("  Seleccione una opción: ").strip()

        if opcion == "1":
            alta_alumno()
        elif opcion == "2":
            ver_listado()
        elif opcion == "3":
            ver_cursos_por_alumno()
        elif opcion == "0":
            separador("═")
            print("  Sesión finalizada. Hasta luego.")
            separador("═")
            break
        else:
            print("\n  ✘  Opción inválida. Intente nuevamente.")
            pausa()


# ─────────────────────────────────────────
#  Punto de entrada
# ─────────────────────────────────────────
if __name__ == "__main__":
    if iniciar_sesion():
        menu_principal()