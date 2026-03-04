
import random

# --- BASE DE DATOS GLOBAL ---

usuarios_sistema = [] 
usuarios_servicio = [] 

# --- FUNCION DE REGISTRO DE USUARIOS ---

def registrar_usuarios():  
    print("--- REGISTRO DE USUARIOS ---")
    nuevo = {}
    nuevo["correo"] = input("Correo: ")
    nuevo["password"] = input("Password: ")

    usuarios_sistema.append(nuevo)
    print("usuario registrado con exito")

# --- FUNCION DE INICIO DE SESIÓN ---

def iniciar_sesion():

    intentos = 3
    
    while intentos > 0:
        print("--- INICIO DE SESIÓN ---")
        print("Intentos disponibles:", intentos)
        
        correo = input("Correo: ")
        password = input("Password: ")
        
        encontrado = False
        
        # Paso 3: Recorrer la lista para validar credenciales
        for usuario in usuarios_sistema:
            if usuario["correo"] == correo and usuario["password"] == password:
                encontrado = True
                break 
        
        # Paso 4: Validar si el acceso fue exitoso o no
        if encontrado:
            print("Login exitoso. Bienvenido al sistema.")
            return True 
        else:
            intentos -= 1
            if intentos > 0:
                print("Credenciales incorrectas. Intentos restantes:", intentos)
            else:
                print("Cuenta bloqueada temporalmente.")
                return False 
    
    return False  # ← red de seguridad
            
# --- REGISTRO DE N DICCIONARIOS (Los 10 usuarios) ---

def generar_usuarios_servicio():
    nombres = ["Mafe", "Juan", "Maricela", "Andrés", "Lucía", "Carlos", "Elena", "Ricardo", "Patricia", "Fernando"]
    
    for i in range(1, 11):
        # Generamos los 30 consumos (un mes)
        consumos_mes = []
        for dia in range(30):
            consumos_mes.append(random.randint(10, 50))
            
        # Creamos el diccionario con la estructura pedida
        usuario = {
            "id": i,
            "nombre": nombres[i-1],
            "documento": random.randint(10000000, 99999999),
            "estrato": random.randint(1, 6),
            "consumoEnergetico": consumos_mes,
            "estado": random.choice(["ACTIVO", "SUSPENDIDO"])
        }
        usuarios_servicio.append(usuario)

# FUNCIÓN PARA ORDENAR POR CONSUMO (Menor a Mayor)

def ordenar_por_consumo():
    # Usamos una función lambda para decirle a sort que sume los consumos
    # y ordene por ese resultado
    usuarios_servicio.sort(key=lambda usuario: sum(usuario["consumoEnergetico"]))
    print("--- USUARIOS ORDENADOS POR CONSUMO (MENOR A MAYOR) ---")
    for usuario in usuarios_servicio:
        total = sum(usuario["consumoEnergetico"])
        print(f"ID: {usuario['id']} | Nombre: {usuario['nombre']} | Total: {total} KWH")


# --- MENÚ PRINCIPAL ---

def menu_principal():
    generar_usuarios_servicio()

    opcion = 0

    while opcion != 3:
        print("========== MENÚ DE INICIO ==========")
        print("1. Registrarse")
        print("2. Iniciar Sesión")
        print("3. Salir")
        
        opcion = int(input("Elija una opción: "))

        if opcion == 1:
            registrar_usuarios()
        elif opcion == 2:
            sesion_ok = iniciar_sesion()
            if sesion_ok:
                menu_consumo()  
        elif opcion == 3:
            print("Saliendo del sistema... ¡Hasta pronto!")
        else:
            print("Opción no válida. Intente de nuevo.")

# --- MENU CONSUMO ---

def menu_consumo(): 
    opcion = 0
    while opcion != 2:
        print("========== MENÚ DEL SISTEMA ==========")
        print("1. Ver usuarios ordenados por consumo")
        print("2. Cerrar sesión")
        opcion = int(input("Elija una opción: "))
        if opcion == 1:
            ordenar_por_consumo()
        elif opcion == 2:
            print("Sesión cerrada.")
        else:
            print("Opción no válida.")

menu_principal()







    



