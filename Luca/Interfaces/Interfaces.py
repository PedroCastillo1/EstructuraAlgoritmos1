# Interfaces generales

def interfaz_gestion_usuario():
    print("\n+--------------------------------------+")
    print("|           GESTIÓN DE USUARIOS        |")
    print("+--------------------------------------+")
    print("| Seleccione una opción:               |")
    print("| 1: Iniciar Sesión                    |")
    print("| -1: Salir del programa               |")
    print("+--------------------------------------+")

def interfaz_menu_admin():
    print("\n+--------------------------------------+")
    print("|         MENÚ DE USUARIO ADMIN        |")
    print("+--------------------------------------+")
    print("| 1: Crear cuenta                      |")
    print("| 2: Eliminar cuenta                   |")
    print("| 3: Ver usuario                       |")
    print("| 4: Cerrar sesión                     |")
    print("+--------------------------------------+")

def interfaz_menu_usuario_comun():
    print("\n+--------------------------------------+")
    print("|        MENÚ DE USUARIO COMÚN         |")
    print("+--------------------------------------+")
    print("| 1: Ingreso al Gestor de Eventos      |")
    print("| 2: Cerrar sesión                     |")
    print("+--------------------------------------+")

def interfaz_bienvenida_gestor_eventos():
    print("\n+--------------------------------------------------+")
    print("|           BIENVENIDO AL GESTOR DE EVENTOS        |")
    print("+--------------------------------------------------+")
    print("| 1: Crear un evento                               |")
    print("| 2: Ver evento                                    |")
    print("| 3: Eliminar evento                               |")
    print("| 4: Mostrar calendario                            |")
    print("| 5: Buscar evento                                 |")
    print("| 6: Ver historial de eventos                      |")
    print("| 7: Salir del gestor de eventos                   |")
    print("+--------------------------------------------------+")

# Interfaces individuales

def interfaz_iniciar_sesion():
    print("\n+--------------------------------------+")
    print("|            INICIAR SESIÓN            |")
    print("+--------------------------------------+")

def interfaz_salir_programa():
    print("\n+--------------------------------------+")
    print("|     Gracias por usar el programa.    |")
    print("|            ¡Hasta pronto!            |")
    print("+--------------------------------------+")

def interfaz_crear_cuenta():
    print("\n+--------------------------------------+")
    print("|         CREAR NUEVA CUENTA           |")
    print("+--------------------------------------+")

def interfaz_eliminar_cuenta():
    print("\n+--------------------------------------+")
    print("|         ELIMINAR UNA CUENTA          |")
    print("+--------------------------------------+")

def interfaz_ver_usuario():
    print("\n+--------------------------------------+")
    print("|         LISTA DE USUARIOS            |")
    print("+--------------------------------------+")

def interfaz_cerrar_sesion_admin():
    print("\n+--------------------------------------+")
    print("|  Sesión de administrador cerrada.    |")
    print("+--------------------------------------+")

def interfaz_ingreso_gestor_eventos():
    print("\n+--------------------------------------+")
    print("|      INGRESO AL GESTOR DE EVENTOS    |")
    print("+--------------------------------------+")

def interfaz_cerrar_sesion_usuario():
    print("\n+--------------------------------------+")
    print("|     Sesión de usuario cerrada.       |")
    print("+--------------------------------------+")

def interfaz_crear_evento():
    print("\n+--------------------------------------------------+")
    print("|              CREAR NUEVO EVENTO                  |")
    print("+--------------------------------------------------+")

def interfaz_ver_evento():
    print("\n+--------------------------------------------------+")
    print("|               VISUALIZAR EVENTO                  |")
    print("+--------------------------------------------------+")

def interfaz_eliminar_evento():
    print("\n+--------------------------------------------------+")
    print("|                ELIMINAR EVENTO                   |")
    print("+--------------------------------------------------+")

def interfaz_mostrar_calendario():
    print("\n+--------------------------------------------------+")
    print("|              MOSTRAR CALENDARIO                  |")
    print("+--------------------------------------------------+")

def interfaz_buscar_evento():
    print("\n+--------------------------------------------------+")
    print("|                BUSCAR EVENTO                     |")
    print("+--------------------------------------------------+")

def interfaz_ver_historial_eventos():
    print("\n+--------------------------------------------------+")
    print("|            HISTORIAL DE EVENTOS                  |")
    print("+--------------------------------------------------+")

def interfaz_salir_gestor_eventos():
    print("\n+--------------------------------------------------+")
    print("|       Saliendo del gestor de eventos...          |")
    print("+--------------------------------------------------+")

# Función principal

def main():
    while True:
        interfaz_gestion_usuario()
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            interfaz_iniciar_sesion()
            tipo_usuario = input("¿Eres admin o usuario? (admin/usuario): ").lower()

            if tipo_usuario == "admin":
                while True:
                    interfaz_menu_admin()
                    opcion_admin = input("Seleccione una opción: ")

                    if opcion_admin == "1":
                        interfaz_crear_cuenta()
                    elif opcion_admin == "2":
                        interfaz_eliminar_cuenta()
                    elif opcion_admin == "3":
                        interfaz_ver_usuario()
                    elif opcion_admin == "4":
                        interfaz_cerrar_sesion_admin()
                        break
                    else:
                        print("Opción inválida. Intente de nuevo.")

            elif tipo_usuario == "usuario":
                while True:
                    interfaz_menu_usuario_comun()
                    opcion_usuario = input("Seleccione una opción: ")

                    if opcion_usuario == "1":
                        interfaz_ingreso_gestor_eventos()
                        while True:
                            interfaz_bienvenida_gestor_eventos()
                            opcion_evento = input("Seleccione una opción: ")

                            if opcion_evento == "1":
                                interfaz_crear_evento()
                            elif opcion_evento == "2":
                                interfaz_ver_evento()
                            elif opcion_evento == "3":
                                interfaz_eliminar_evento()
                            elif opcion_evento == "4":
                                interfaz_mostrar_calendario()
                            elif opcion_evento == "5":
                                interfaz_buscar_evento()
                            elif opcion_evento == "6":
                                interfaz_ver_historial_eventos()
                            elif opcion_evento == "7":
                                interfaz_salir_gestor_eventos()
                                break
                            else:
                                print("Opción inválida. Intente de nuevo.")
                        break

                    elif opcion_usuario == "2":
                        interfaz_cerrar_sesion_usuario()
                        break
                    else:
                        print("Opción inválida. Intente de nuevo.")

            else:
                print("Tipo de usuario no reconocido.")

        elif opcion == "-1":
            interfaz_salir_programa()
            break

        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()
