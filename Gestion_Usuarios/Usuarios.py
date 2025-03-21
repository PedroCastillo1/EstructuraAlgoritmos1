Fin = -1
#Listas de Usuarios del Programa
Lista_Usuarios = ["Martin","luca","Pedro","Lucia","Tomas"]
Lista_Contraseñas = ["123","1234","2210","123456","1234567"]

def Menu_Interactivo_GestionUsuario():
    print("=================================================================================================")
    print("|                          BIENVENIDO AL PROGRAMA DE GESTION DE EVENTOS                         |")
    print("=================================================================================================")
    print("=================================================================================================")
    print("|                     SI USTED QUIERE INGRESAR A SU CUENTA, INGRESE EL VALOR 1                  |")
    print("=================================================================================================")
    print("=================================================================================================")
    print("|                     SI USTED QUIERE CREAR A SU CUENTA, INGRESE EL VALOR 2                     |")
    print("=================================================================================================")
    print("=================================================================================================")
    print("|                     SI USTED QUIERE VER LA LISTA DE CUENTAS, INGRESE EL VALOR 3               |")
    print("=================================================================================================")
    print("=================================================================================================")
    print("|                     SI USTED QUIERE TERMINAR EL PROGRAMA, INGRESE EL VALOR -1                 |")
    print("=================================================================================================")
    return

################################### FUNCIONES DE LAS OPCIONES DEL MENU DE USUARIOS ####################################
#================================================ OPCION 1 INICIAR SESESION =============================================
def INICIAR_SESION(Lista_Usuarios,Lista_Contraseñas):
    # 2 variables para verificar la cantidad de intentos de inicio de sesion
    Intentos = 0
    Max_Intentos = 3
    print("=================================================================================================")
    print("|                                         INICIAR SESION                                        |")
    print("=================================================================================================")
    # ingresamos por teclado 1 o Fin para iniciar sesion o querer volver a la interfaz de usuario
    Inicio = int (input("Si quiere iniciar sesion ponga 1, si quiere salir ponga -1:  "))
    # Verificamos que el valor sea el correspondiente para realizar las posibles opciones
    while(Inicio != Fin):
        # Verificamos que mientras no esten en esos 2 valores correctos tengra que ingresarlo nuevamente
        while((Inicio != 1) and (Inicio != Fin)):
            print("Ingresaste mal las opciones a elegir")
            Inicio = int (input("Si quiere iniciar sesion ponga 1, si quiere salir ponga -1"))
        # Si ingresa Fin significa que decidio salir del Programa
        if Inicio == Fin:
            print("Has decidido salir del programa.")
            return False
        # Aca vamos a estar verificando que no supere la cantidad de intentos permitidos para ingresar
        while(Intentos < Max_Intentos):
            # Pedimos sus datos a ingresar Nombre y Contraseña
            print("=================================================================================================")
            Nombre_Usuario = input("INGRESAR SU NOMBRE DE USUARIO: ")
            print("=================================================================================================")
            Contraseña_Usuario = input("INGRESAR SU CONTRASEÑA: ")
            # verificamos que dicho usuario ingresado exista dentro de nuestras listas
            if(Buscar_Usuario(Lista_Usuarios, Lista_Contraseñas, Nombre_Usuario, Contraseña_Usuario)):
                print("Inicio de sesión exitoso.")
                return True
            else:
                # Si no existe se incremente la variable intentos y se notifica
                Intentos += 1
                print(f"Intento fallido. Te quedan {Max_Intentos - Intentos} intentos.")
        # Si dichos intentos son mas de los permitidos, te devuelve a la interfaz principal
        if(Intentos >= Max_Intentos):
            print("Demasiados intentos fallidos. Sesión bloqueada.")
            return False
#================================================ OPCION 2 CREAR =============================================
def CREAR_SESSION():
    print("=================================================================================================")
    print("|                                         CREAR SESION                                          |")
    print("=================================================================================================")
    print("=================================================================================================")
    Nombre_Usuario = input("INGRESAR SU NOMBRE DE USUARIO = ")
    print("=================================================================================================")
    #Aca vamos a verificar que dicho nombre no se encuentre dentro de las listas de Usuarios
    while not(Verificar_Existencia_Usuario(Lista_Usuarios,Nombre_Usuario)):
        print("=================================================================================================")
        print("|                                 INGRESAR NUEVAMENTE SU NOMBRE                                 |")
        print("=================================================================================================")
        print("=================================================================================================")
        Nombre_Usuario = input("INGRESAR SU NOMBRE DE USUARIO = ")
        print("=================================================================================================")
    #Si no exite el Nombre puede crearse la cuenta y podemos pedir ahora la Contraseña
    print("=================================================================================================")
    Contraseña_Usuario = input("INGRESAR SU CONTRASEÑA DE USUARIO = ")
    print("=================================================================================================")
    # Dicho Usuario y Contraseña van a ser agregadas a las listas
    Agregar_Usuario(Lista_Usuarios,Lista_Contraseñas,Nombre_Usuario,Contraseña_Usuario)
    return
#=================================== OPCION 3 IMPRIMIR LISTAS DE USUARIOS =========================================
def Imprimir_Listas_Usuarios(Lista_Usuarios, Lista_Contraseñas):
    print("=================================================================================================")
    print("|                                         IMPRIMIR LISTAS                                        |")
    print("=================================================================================================")
    # Vamos a recorrer ambas listas hasta el final de ellas y vamos a imprimir el contenido.
    print("Lista de Usuarios Registrados:", end=" ")
    for i in range(len(Lista_Usuarios)):
        print(Lista_Usuarios[i], end=" ")
    print() 
    print("---------------------------------------")
    print("Lista de Contraseñas Registradas:", end=" ")
    for i in range(len(Lista_Contraseñas)):
        print('*' * len(Lista_Contraseñas[i]), end=" ")
    print()
    print("=================================================================================================")
    return
################################### FUNCIONES DE LAS OPCIONES DEL MENU DE USUARIOS ####################################

########################################## FUNCIONES DE USUARIOS #####################################################
def Verificar_Existencia_Usuario(Lista_Usuarios,Nombre_Usuario):
    #Inicializamos una varible indice en 0 para posicionarnos en el comienzo de la lista
    i = 0
    # mientras i no llegue a el fin de la lista y El Usuario sea distinto a el Usuario ingresado 
    while((i < len(Lista_Usuarios)) and (Lista_Usuarios[i] != Nombre_Usuario)):
        #Incrementamos el indice para seguir buscando se existe el Usario ingresado
        i = i + 1
    # Aca verificamos si Salimos porque llegamos al final de la lista o porque encontramos que existe
    if(i < len(Lista_Usuarios)):
        print("EL NOMBRE YA SE ENCUENTRA UTILIZANDOSE, POR FAVOR INTENTE CON OTRO NUEVO")
        return False
    print("EL NOMBRE SE ENCUENTA DISPONIBLE :) ")
    return True

def Agregar_Usuario(Lista_Usuarios,Lista_Contraseñas,Nombre_Usuario,Contraseña_Usuario):
    #Aca agregamos al final de las listas el nuevo Usuario y Contraseña 
    Lista_Usuarios.append(Nombre_Usuario)
    Lista_Contraseñas.append(Contraseña_Usuario) 
    return Lista_Usuarios,Lista_Contraseñas

def Verificacion_Menu(Valor_Mini_Interfaz):
    #Aca creamos una funcion para que si el usuario elige mal las opciones que intente nuevamente
    while((Valor_Mini_Interfaz != 1) and (Valor_Mini_Interfaz != 2) and (Valor_Mini_Interfaz != 3) and (Valor_Mini_Interfaz != Fin)):
        print("=================================================================================================")
        print("|                        INGRESASTE MAL EL VALOR DE LAS OPCIONES                                |")
        print("|                             INTENTAR NUEVAMENTE POR FAVOR                                     |")
        print("=================================================================================================")
        print("=================================================================================================")
        Valor_Mini_Interfaz = int (input("INGRESAR SU VALOR POR FAVOR = "))
        print("=================================================================================================")
    return

def Verificacion_Menu_Stocks(Menu):
    #Aca creamos una funcion para que si el usuario elige mal las opciones que intente nuevamente
    while((Menu != 1) and (Menu != 2) and (Menu != 3) and (Menu != 4) and (Menu != 5) and (Menu != Fin)):
        print("=================================================================================================")
        print("|                        INGRESASTE MAL EL VALOR DE LAS OPCIONES                                |")
        print("|                             INTENTAR NUEVAMENTE POR FAVOR                                     |")
        print("=================================================================================================")
        Menu = int (input("Ingrese la Opcion elegida: "))
    return

def Buscar_Usuario(Lista_Usuarios, Lista_Contraseñas, Nombre_Usuario, Contraseña_Usuario):
    #Inicializamos una varible indice en 0 para posicionarnos en el comienzo de la lista
    i = 0
    # mientras i no llegue a el fin de la lista y El Usuario sea distinto a el Usuario ingresado
    while ((i < len(Lista_Usuarios)) and (Lista_Usuarios[i] != Nombre_Usuario)):
        #Incrementamos el indice para seguir buscando se existe el Usario ingresado
        i = i + 1
    # Aca verificamos si Salimos porque llegamos al final de la lista o porque encontramos que existe
    if(i < len(Lista_Usuarios)):
        #Creamos una variable para guardar la posicion del Usuario para luego buscarla en la misma posicion en Contraseña
        Pos = i
        # Si es igual el valor ingresado por teclado con el valor guardado en esa posicion significa que el ingreso a sido realizado correctamente
        if Lista_Contraseñas[Pos] == Contraseña_Usuario:
            return True
    return False
########################################## FUNCIONES DE USUARIOS ###############################################

###################################   PROGRAMA PRINCIPAL     ###################################################
Menu_Interactivo_GestionUsuario()
print("=================================================================================================")
Valor_Mini_Interfaz = int (input("INGRESAR SU VALOR POR FAVOR = "))
print("=================================================================================================")

while(Valor_Mini_Interfaz != Fin):
    Verificacion_Menu(Valor_Mini_Interfaz)
    if(Valor_Mini_Interfaz == 1):   
        while(INICIAR_SESION(Lista_Usuarios,Lista_Contraseñas)):
            Menu = int (input("Ingrese la Opcion elegida: "))
            while(Menu != Fin):
                print("HOLA MUNDOO")

                Menu = int (input("Ingrese la Opcion elegida: "))




            print("USTED A CERRADO SESSION.")

    if(Valor_Mini_Interfaz == 2):
        CREAR_SESSION()
    if(Valor_Mini_Interfaz == 3):
        Imprimir_Listas_Usuarios(Lista_Usuarios, Lista_Contraseñas)  
    Menu_Interactivo_GestionUsuario()
    print("=================================================================================================")
    Valor_Mini_Interfaz = int (input("INGRESAR SU VALOR POR FAVOR = "))
    print("=================================================================================================")
print("USTED A FINALIZADO EL PROGRAMA, HASTA LUEGOO")
###################################   PROGRAMA PRINCIPAL     ###################################################





"""
if(Valor_Mini_Interfaz == 1):   
        while(INICIAR_SESION(Lista_Usuarios,Lista_Contraseñas)):
            

            # ACA ADENTRO VA ESTAR EN GESTOR DE EVENTOS Y TODAS SUS FUNCINALIDADES. EJEMPLO...

            #
            Menu_Interactivo_ControlStock()
            Menu = int (input("Ingrese la Opcion elegida: "))
            while(Menu != Fin):
                Verificacion_Menu_Stocks(Menu)
                if(Menu == 1):
                    Stock_total = CREAR_PRODUCTO(Stock_total)

                if(Menu == 2):
                    ELIMINAR_PRODUCTO()
                
                if(Menu == 3):
                    ACTUALIZAR_PRODUCTO()

                if(Menu == 4):
                    retirar_stock()

                if(Menu == 5):
                    IMPRIMIR_STOCK()

                Menu_Interactivo_ControlStock()
                Menu = int (input("Ingrese la Opcion elegida: "))"
            #

            print("USTED A CERRADO SESSION.")"
"""