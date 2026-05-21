from app.config.settings import APP_NAME, APP_VERSION, ADMIN_USER
from app.usuarios.gestor import (
    registrar_usuario,
    listar_usuarios,
    buscar_por_nombre,
    buscar_por_correo
)
from app.usuarios.validaciones import ErrorValidacion

def mostrar_menu():
    print("\n" + "="*40)
    print(f"  {APP_NAME} v{APP_VERSION}")
    print(f"  Usuario admin: {ADMIN_USER}")
    print("="*40)
    print("1. Registrar usuario")
    print("2. Listar usuarios")
    print("3. Buscar por nombre")
    print("4. Buscar por correo")
    print("5. Salir")
    print("="*40)

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opcion: ").strip()

        if opcion == "1":
            nombre = input("Nombre: ")
            edad   = input("Edad: ")
            correo = input("Correo: ")
            try:
                u = registrar_usuario(nombre, edad, correo)
                print(f"Usuario '{u['nombre']}' registrado con id {u['id']}.")
            except (ErrorValidacion, ValueError) as e:
                print(f"Error: {e}")

        elif opcion == "2":
            usuarios = listar_usuarios()
            if not usuarios:
                print("No hay usuarios registrados.")
            else:
                print(f"\n{'ID':<5} {'Nombre':<20} {'Edad':>5} {'Correo':<30}")
                print("-" * 62)
                for u in usuarios:
                    print(f"{u['id']:<5} {u['nombre']:<20} {u['edad']:>5} {u['correo']:<30}")

        elif opcion == "3":
            termino = input("Nombre a buscar: ")
            resultados = buscar_por_nombre(termino)
            if resultados:
                for u in resultados:
                    print(f"  -> {u['id']} | {u['nombre']} | {u['edad']} | {u['correo']}")
            else:
                print("No se encontraron usuarios.")

        elif opcion == "4":
            correo = input("Correo a buscar: ")
            u = buscar_por_correo(correo)
            if u:
                print(f"  -> {u['id']} | {u['nombre']} | {u['edad']} | {u['correo']}")
            else:
                print("No se encontro ningun usuario con ese correo.")

        elif opcion == "5":
            print("Hasta luego.")
            break

        else:
            print("Opcion no valida.")

if __name__ == "__main__":
    main()