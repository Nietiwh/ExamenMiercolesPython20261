
import random

# Acceso al Sistema

def registrar_credenciales():
    usuarios_sistema = []
    print("--- REGISTRO DE SEGURIDAD ---")
    # Registramos 2 usuarios para la prueba
    for i in range(1):
        nuevo = {}
        print("Registro del usuario:", i + 1)
        nuevo["correo"] = input("Correo: ")
        nuevo["password"] = input("Password: ")
        usuarios_sistema.append(nuevo)
    return usuarios_sistema


# LOGIN (Máximo 3 intentos)

def login(base_datos):
    intentos = 3
    while intentos > 0:
        print("Ingresa tus credenciales")
        u_ingresado = input("Correo: ")
        p_ingresado = input("Password: ")

        acceso = False
        for usuario in base_datos:
            if usuario["correo"] == u_ingresado and usuario["password"] == p_ingresado:
                acceso = True
        
        if acceso:
            print("Login exitoso")
            return True
        else:
            intentos = intentos - 1
            print("Credenciales incorrectas.")

    print("Cuenta bloqueada temporalmente")
    return False

# Usuarios del servicio público de energía

def generar_usuarios_servicio():
    usuarios_servicio = []
    nombres = ["Mafe", "Juan", "Maricela", "Andres", "Lucia", "Carlos", "Elena", "Ricardo", "Patricia", "Fernando"]
    estados = ["ACTIVO", "SUSPENDIDO"]

    for i in range(1, 11):
        usuario = {
            "id": i,
            "nombre": nombres[i-1], 
            "documento": random.randint(10000000, 99999999),
            "estrato": random.randint(1, 6),
            # 30 consumos aleatorios (un mes)
            "consumoEnergetico": [random.randint(10, 50) for _ in range(30)],
            "estado": random.choice(estados)
        }
        usuarios_servicio.append(usuario)
    return usuarios_servicio

    usuarios_servicio.insert(1, "Mafe")
    print(usuarios_servicio)

    usuarios_servicio.remove(2, "Juan")
    print(usuarios_servicio)

    usuarios_servicio.pop(3)
    print(usuarios_servicio)

    usuarios_servicio.sort()
    print(usuarios_servicio)

#MENÚ

def mostrar_reporte(lista_clientes):
    print("\n--- REPORTE DE CONSUMO ENERGÉTICO ---")
    for cliente in lista_clientes:
        total_kwh = sum(cliente["consumoEnergetico"])
        
        print("\nCliente:", cliente["nombre"])
        print("Estrato:", cliente["estrato"])
        print("Consumo Total:", total_kwh, "KWH")
        
        if cliente["estrato"] <= 2:
            print("Estado: SUBSIDIADO")
        elif cliente["estrato"] >= 5:
            print("Estado: CONTRIBUYENTE")
        else:
            print("Estado: TARIFA PLENA")
        
        if cliente["estado"] == "SUSPENDIDO":
            print("ALERTA: SERVICIO SUSPENDIDO")

#Llamando a las funciones para ejecutar el programa

#Registro inicial
credenciales = registrar_credenciales() 

#Validación de acceso
if login(credenciales):
    datos_energia = generar_usuarios_servicio()
    mostrar_reporte(datos_energia)

