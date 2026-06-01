import csv
import os

ARCHIVO_CSV = "paises.csv"


# ====================== ARCHIVOS CSV ======================

def cargar_paises(nombre_archivo):
    if not os.path.exists(nombre_archivo):
        crear_archivo_csv(nombre_archivo)
        print(f"  [INFO] Archivo '{nombre_archivo}' creado vacío.")
        return []

    paises = []
    try:
        with open(nombre_archivo, mode="r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                try:
                    pais = {
                        "nombre": fila["nombre"].strip(),
                        "poblacion": int(fila["poblacion"]),
                        "superficie": int(fila["superficie"]),
                        "continente": fila["continente"].strip()
                    }
                    paises.append(pais)
                except (ValueError, KeyError):
                    continue
    except IOError:
        print(f"  [ERROR] No se pudo leer '{nombre_archivo}'.")
        return []

    return paises


def guardar_paises(nombre_archivo, paises):
    columnas = ["nombre", "poblacion", "superficie", "continente"]
    try:
        with open(nombre_archivo, mode="w", encoding="utf-8", newline="") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=columnas)
            escritor.writeheader()
            escritor.writerows(paises)
        return True
    except IOError as e:
        print(f"  [ERROR] No se pudo guardar: {e}")
        return False


def crear_archivo_csv(nombre_archivo):
    with open(nombre_archivo, mode="w", encoding="utf-8", newline="") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["nombre", "poblacion", "superficie", "continente"])


# ====================== ENTRADA DE DATOS ======================

def pedir_texto(mensaje, campo):
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print(f"  [ERROR] El campo '{campo}' no puede estar vacío.")


def pedir_entero(mensaje, campo):
    while True:
        valor_texto = input(mensaje).strip()
        if not valor_texto:
            print(f"  [ERROR] El campo '{campo}' no puede estar vacío.")
            continue
        try:
            valor = int(valor_texto)
            if valor <= 0:
                print(f"  [ERROR] '{campo}' debe ser mayor a cero.")
            else:
                return valor
        except ValueError:
            print(f"  [ERROR] '{valor_texto}' no es un número válido.")


# ====================== OPERACIONES PRINCIPALES ======================

def agregar_pais(paises):
    print("\n  ── Agregar nuevo país ──")
    nombre = pedir_texto("  Nombre del país: ", "nombre")
    poblacion = pedir_entero("  Población: ", "poblacion")
    superficie = pedir_entero("  Superficie (km²): ", "superficie")
    continente = pedir_texto("  Continente: ", "continente")

    if buscar_por_nombre_exacto(paises, nombre):
        print(f"\n  [ERROR] Ya existe un país llamado '{nombre}'.")
        return

    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }

    paises.append(nuevo_pais)
    if guardar_paises(ARCHIVO_CSV, paises):
        print(f"\n  ✓ País '{nombre}' agregado correctamente.")
    else:
        paises.remove(nuevo_pais)


def actualizar_pais(paises):
    print("\n  ── Actualizar país ──")
    nombre_buscar = pedir_texto("  Nombre del país: ", "nombre")
    pais = buscar_por_nombre_exacto(paises, nombre_buscar)

    if not pais:
        print(f"\n  [INFO] No se encontró '{nombre_buscar}'.")
        return

    print(f"\n  Datos actuales de '{pais['nombre']}':")
    print(f"    Población:  {pais['poblacion']:,}".replace(",", "."))
    print(f"    Superficie: {pais['superficie']:,} km²".replace(",", "."))

    print("\n  ¿Qué actualizar?")
    print("    1) Población")
    print("    2) Superficie")
    print("    0) Cancelar")
    opcion = input("  Opción: ").strip()

    if opcion == "1":
        pais["poblacion"] = pedir_entero("  Nueva población: ", "poblacion")
        campo = "Población"
    elif opcion == "2":
        pais["superficie"] = pedir_entero("  Nueva superficie: ", "superficie")
        campo = "Superficie"
    elif opcion == "0":
        return
    else:
        print("  [ERROR] Opción inválida.")
        return

    if guardar_paises(ARCHIVO_CSV, paises):
        print(f"\n  ✓ {campo} actualizada correctamente.")
    else:
        print("  [ERROR] No se pudo guardar el archivo.")


# ====================== BÚSQUEDAS ======================

def buscar_por_nombre_exacto(paises, nombre):
    nombre_lower = nombre.lower()
    for pais in paises:
        if pais["nombre"].lower() == nombre_lower:
            return pais
    return None


def buscar_paises(paises):
    print("\n  ── Buscar país ──")
    print("    1) Coincidencia exacta")
    print("    2) Coincidencia parcial")
    tipo = input("  Opción: ").strip()

    if tipo not in ("1", "2"):
        print("  [ERROR] Opción inválida.")
        return

    termino = pedir_texto("  Texto a buscar: ", "término").lower()
    resultados = []

    if tipo == "1":
        pais = buscar_por_nombre_exacto(paises, termino)
        if pais:
            resultados.append(pais)
    else:
        for pais in paises:
            if termino in pais["nombre"].lower():
                resultados.append(pais)

    if not resultados:
        print(f"\n  [INFO] No se encontraron resultados para '{termino}'.")
    else:
        print(f"\n  Se encontraron {len(resultados)} resultado(s):")
        mostrar_tabla(resultados)


# ====================== FILTROS ======================

def filtrar_paises(paises):
    print("\n  ── Filtrar países ──")
    print("    1) Por continente")
    print("    2) Por rango de población")
    print("    3) Por rango de superficie")
    opcion = input("  Opción: ").strip()

    if opcion == "1":
        resultados = filtrar_por_continente(paises)
    elif opcion == "2":
        resultados = filtrar_por_rango(paises, "poblacion", "Población")
    elif opcion == "3":
        resultados = filtrar_por_rango(paises, "superficie", "Superficie")
    else:
        print("  [ERROR] Opción inválida.")
        return

    if not resultados:
        print("\n  [INFO] No se encontraron países.")
    else:
        print(f"\n  Se encontraron {len(resultados)} país(es):")
        mostrar_tabla(resultados)


def filtrar_por_continente(paises):
    continentes = obtener_continentes_unicos(paises)
    if not continentes:
        return []

    print("\n  Continentes disponibles:")
    for i, cont in enumerate(continentes, 1):
        print(f"    {i}) {cont}")

    continente = pedir_texto("  Continente: ", "continente").lower()
    return [p for p in paises if p["continente"].lower() == continente]


def filtrar_por_rango(paises, campo, nombre_campo):
    print(f"\n  Filtrando por {nombre_campo}:")
    minimo = pedir_entero(f"  Mínimo: ", "mínimo")
    maximo = pedir_entero(f"  Máximo: ", "máximo")

    if minimo > maximo:
        print("  [ERROR] Mínimo no puede ser mayor que máximo.")
        return []

    return [p for p in paises if minimo <= p[campo] <= maximo]


def obtener_continentes_unicos(paises):
    return sorted({p["continente"] for p in paises})


# ====================== ORDENAMIENTO ======================

def ordenar_paises(paises):
    if not paises:
        print("\n  [INFO] No hay países para ordenar.")
        return

    print("\n  ── Ordenar por ──")
    print("    1) Nombre")
    print("    2) Población")
    print("    3) Superficie")
    criterio = input("  Opción: ").strip()

    print("\n  Dirección:")
    print("    1) Ascendente")
    print("    2) Descendente")
    direccion = input("  Opción: ").strip()

    if criterio not in ("1", "2", "3") or direccion not in ("1", "2"):
        print("  [ERROR] Opción inválida.")
        return

    clave = ["nombre", "poblacion", "superficie"][int(criterio) - 1]
    reverse = direccion == "2"

    paises_ordenados = sorted(paises, key=lambda p: p[clave], reverse=reverse)
    print(f"\n  Países ordenados por {clave.capitalize()} ({'Descendente' if reverse else 'Ascendente'}):")
    mostrar_tabla(paises_ordenados)


# ====================== ESTADÍSTICAS ======================

def mostrar_estadisticas(paises):
    if not paises:
        print("\n  [INFO] No hay datos para estadísticas.")
        return

    print("\n  ── Estadísticas ──")

    # Población
    max_p = max(paises, key=lambda p: p["poblacion"])
    min_p = min(paises, key=lambda p: p["poblacion"])
    prom_p = sum(p["poblacion"] for p in paises) / len(paises)

    print("  📊 Población:")
    print(f"     Mayor: {max_p['nombre']} → {max_p['poblacion']:,}".replace(",", "."))
    print(f"     Menor: {min_p['nombre']} → {min_p['poblacion']:,}".replace(",", "."))
    print(f"     Promedio: {int(prom_p):,}".replace(",", "."))

    # Superficie
    prom_s = sum(p["superficie"] for p in paises) / len(paises)
    print(f"\n  🗺️  Superficie promedio: {int(prom_s):,} km²".replace(",", "."))

    # Por continente
    conteo = {}
    for p in paises:
        conteo[p["continente"]] = conteo.get(p["continente"], 0) + 1

    print("\n  🌍 Países por continente:")
    for cont in sorted(conteo):
        print(f"     {cont}: {conteo[cont]}")

    print(f"\n  Total de países: {len(paises)}")


# ====================== VISUALIZACIÓN ======================

def listar_todos(paises):
    if not paises:
        print("\n  [INFO] No hay países registrados.")
        return
    print(f"\n  ── Lista completa ({len(paises)} países) ──")
    mostrar_tabla(paises)


def mostrar_tabla(paises):
    if not paises:
        print("  (Sin resultados)")
        return

    ancho_n = 22
    ancho_p = 16
    ancho_s = 16
    ancho_c = 12

    sep = "  " + "-" * (ancho_n + ancho_p + ancho_s + ancho_c + 3)
    print(sep)
    print(f"  {'NOMBRE':<{ancho_n}}{'POBLACIÓN':>{ancho_p}}{'SUPERFICIE (km²)':>{ancho_s}}  {'CONTINENTE':<{ancho_c}}")
    print(sep)

    for p in paises:
        pob = f"{p['poblacion']:,}".replace(",", ".")
        sup = f"{p['superficie']:,}".replace(",", ".")
        print(f"  {p['nombre']:<{ancho_n}}{pob:>{ancho_p}}{sup:>{ancho_s}}  {p['continente']:<{ancho_c}}")
    print(sep)


# ====================== MENÚ ======================

def mostrar_menu():
    print("\n" + "=" * 55)
    print("      SISTEMA DE GESTIÓN DE PAÍSES - UTN")
    print("=" * 55)
    print("  1) Listar todos")
    print("  2) Agregar país")
    print("  3) Actualizar país")
    print("  4) Buscar país")
    print("  5) Filtrar")
    print("  6) Ordenar")
    print("  7) Estadísticas")
    print("  0) Salir")
    print("=" * 55)


def obtener_opcion():
    validas = {"0", "1", "2", "3", "4", "5", "6", "7"}
    while True:
        op = input("  Elegí una opción: ").strip()
        if op in validas:
            return op
        print("  [ERROR] Opción inválida.")


def main():
    print("\n" + "=" * 55)
    print("  Bienvenido al Sistema de Gestión de Países")
    print("=" * 55)

    paises = cargar_paises(ARCHIVO_CSV)
    print(f"  ✓ {len(paises)} países cargados.")

    while True:
        mostrar_menu()
        opcion = obtener_opcion()

        if opcion == "0":
            print("\n  ¡Hasta luego!")
            break
        elif opcion == "1":
            listar_todos(paises)
        elif opcion == "2":
            agregar_pais(paises)
        elif opcion == "3":
            actualizar_pais(paises)
        elif opcion == "4":
            buscar_paises(paises)
        elif opcion == "5":
            filtrar_paises(paises)
        elif opcion == "6":
            ordenar_paises(paises)
        elif opcion == "7":
            mostrar_estadisticas(paises)

        input("\n  Presioná Enter para continuar...")


if __name__ == "__main__":
    main()