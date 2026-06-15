# Trabajo Práctico Integrador - Sistema de Gestión de Países

## Descripción

Aplicación de consola desarrollada en Python para la gestión de información de países utilizando archivos CSV como almacenamiento persistente.

El sistema permite administrar datos de distintos países, incluyendo nombre, población, superficie y continente.

---

# Funcionalidades

## Gestión de Países

* Listar todos los países registrados.
* Agregar nuevos países.
* Actualizar población o superficie de un país existente.
* Validación de datos ingresados por el usuario.

## Búsquedas

* Búsqueda por coincidencia exacta.
* Búsqueda por coincidencia parcial.

## Filtros

* Filtrar por continente.
* Filtrar por rango de población.
* Filtrar por rango de superficie.

## Ordenamiento

* Ordenar por nombre.
* Ordenar por población.
* Ordenar por superficie.
* Orden ascendente o descendente.

## Estadísticas

* País con mayor población.
* País con menor población.
* Promedio de población.
* Promedio de superficie.
* Cantidad de países por continente.
* Total de países registrados.

## Persistencia de Datos

* Lectura de datos desde archivo CSV.
* Guardado automático de cambios en archivo CSV.
* Creación automática del archivo si no existe.

---

# Tecnologías Utilizadas

* Python 3
* Módulo `csv`
* Módulo `os`
* Programación estructurada

---

# Estructura de Datos

Cada país contiene los siguientes campos:

| Campo      | Tipo   |
| ---------- | ------ |
| nombre     | Texto  |
| poblacion  | Entero |
| superficie | Entero |
| continente | Texto  |

---

# Archivo de Almacenamiento

El sistema utiliza el archivo:

`paises.csv`

Formato:

```csv
nombre,poblacion,superficie,continente
Argentina,45376763,2780400,America
Brasil,213993437,8515767,America
```

---

# Ejecución del Sistema

## Inicio

```text
=======================================================
Bienvenido al Sistema de Gestión de Países
✓ 31 países cargados.
=======================================================
```

## Menú Principal

```text
=======================================================
SISTEMA DE GESTIÓN DE PAÍSES - UTN
=======================================================

1. Listar todos
2. Agregar país
3. Actualizar país
4. Buscar país
5. Filtrar
6. Ordenar
7. Estadísticas
0. Salir

Elegí una opción:
```

---

## Opción 1: Listar Países

```text
NOMBRE         POBLACIÓN      SUPERFICIE (km²)    CONTINENTE
Argentina      45.376.763     2.780.400           América
Brasil         213.993.437    8.515.767           América
Chile          19.116.201       756.102           América
```

---

## Opción 2: Agregar País

```text
Elegí una opción: 2

── Agregar nuevo país ──

Nombre del país: Rumania
Población: 19237691
Superficie (km²): 238397

Continentes disponibles:
1) Africa
2) America
3) Asia
4) Europa
5) Oceania
0) Cancelar

Elegí una opción: 4

✓ País 'Rumania' agregado correctamente.

Presioná Enter para continuar...
```

---

## Opción 3: Actualizar País

```text
Elegí una opción: 3

── Actualizar país ──

Nombre del país: Rumania

Datos actuales de 'Rumania':
Población: 19.237.691
Superficie: 238.397 km²

¿Qué actualizar?

1) Población
2) Superficie
0) Cancelar
```

---

## Opción 4: Buscar País

```text
Elegí una opción: 4

── Buscar país ──

1) Coincidencia exacta
2) Coincidencia parcial

Opción: 2
Texto a buscar: ruman

Se encontraron 1 resultado(s):

NOMBRE      POBLACIÓN      SUPERFICIE (km²)    CONTINENTE
Rumania     19.237.691       238.397          Europa

Presioná Enter para continuar...
```

---

## Opción 5: Filtrar Países

```text
Elegí una opción: 5

── Filtrar países ──

1) Por continente
2) Por rango de población
3) Por rango de superficie

Opción: 1

Continentes disponibles:
1) Africa
2) America
3) Asia
4) Europa
5) Oceania

Elegí una opción: 4
```

Resultado:

```text
Se encontraron 9 país(es):

Alemania
Francia
Italia
España
Reino Unido
Portugal
Suecia
Polonia
Rumania
```

---

## Opción 6: Ordenar Países

```text
Elegí una opción: 6

── Ordenar por ──

1) Nombre
2) Población
3) Superficie

Opción: 1

Dirección:
1) Ascendente
2) Descendente

Opción: 1
```

Resultado:

```text
Países ordenados por Nombre (Ascendente)

Alemania
Angola
Argentina
Australia
Brasil
Chile
China
Colombia
Corea del Sur
Egipto
España
...
```

---

## Opción 7: Estadísticas

```text
── Estadísticas ──

Población:
Mayor: China → 1.412.600.000
Menor: Uruguay → 3.574.900
Promedio: 156.954.370

Superficie promedio:
39.556.498 km²

Países por continente:
Africa: 7
America: 8
Asia: 6
Europa: 9
Oceania: 2

Total de países: 32
```

---

## Salida del Sistema

```text
Elegí una opción: 0

¡Hasta luego!
```

Ejecución:

```bash
python tpi_paises.py
```

---

# Autores

* Nicolás Sancholuz
* Agustín Fernández

---

# Institución

Universidad Tecnológica Nacional (UTN)

Tecnicatura Universitaria en Programación
