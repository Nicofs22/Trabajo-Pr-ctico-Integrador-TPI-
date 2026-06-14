# Trabajo Práctico Integrador - Sistema de Gestión de Países

## Descripción

Aplicación de consola desarrollada en Python para la gestión de información de países utilizando archivos CSV como almacenamiento persistente.

El sistema permite administrar datos de distintos países, incluyendo nombre, población, superficie y continente.

## Funcionalidades

### Gestión de países
- Listar todos los países registrados.
- Agregar nuevos países.
- Actualizar población o superficie de un país existente.
- Validación de datos ingresados por el usuario.

### Búsquedas
- Búsqueda por coincidencia exacta.
- Búsqueda por coincidencia parcial.

### Filtros
- Filtrar por continente.
- Filtrar por rango de población.
- Filtrar por rango de superficie.

### Ordenamiento
- Ordenar por nombre.
- Ordenar por población.
- Ordenar por superficie.
- Orden ascendente o descendente.

### Estadísticas
- País con mayor población.
- País con menor población.
- Promedio de población.
- Promedio de superficie.
- Cantidad de países por continente.
- Total de países registrados.

### Persistencia de datos
- Lectura de datos desde archivo CSV.
- Guardado automático de cambios en archivo CSV.
- Creación automática del archivo si no existe.

## Tecnologías utilizadas

- Python 3
- Módulo `csv`
- Módulo `os`
- Programación estructurada

## Estructura de datos

Cada país contiene los siguientes campos:

| Campo | Tipo |
|---------|---------|
| nombre | Texto |
| poblacion | Entero |
| superficie | Entero |
| continente | Texto |

## Archivo de almacenamiento

El sistema utiliza el archivo:

```text
paises.csv
```

Formato:

```csv
nombre,poblacion,superficie,continente
Argentina,45376763,2780400,America
Brasil,213993437,8515767,America
```

## Ejecución

=======================================================
  Bienvenido al Sistema de Gestión de Países
=======================================================
  ✓ 31 países cargados.

=======================================================
      SISTEMA DE GESTIÓN DE PAÍSES - UTN
=======================================================
  1) Listar todos
  2) Agregar país
  3) Actualizar país
  4) Buscar país
  5) Filtrar
  6) Ordenar
  7) Estadísticas
  0) Salir
=======================================================
  Elegí una opción:
opcion 1
---------------------------------------------------------------------
  NOMBRE                       POBLACIÓNSUPERFICIE (km²)  CONTINENTE  
  ---------------------------------------------------------------------
  Argentina                   45.376.763       2.780.400  America     
  Brasil                     213.993.437       8.515.767  America     
  Chile                       19.116.201         756.102  America     
  Colombia                    51.265.844       1.141.748  America     
  Mexico                     128.932.753       1.964.375  America     
  Peru                        33.359.418       1.285.216  America     
  Uruguay                      3.574.900         176.215  America     
  Venezuela                   28.301.696         912.050  America     
  Japon                      125.800.000         377.975  Asia        
  China                    1.412.600.000       9.596.960  Asia        
  India                    1.393.409.038       3.287.263  Asia        
  Corea del Sur               51.780.579         100.210  Asia        
  Indonesia                  273.523.615       1.904.569  Asia        
  Tailandia                   71.601.103         513.120  Asia        
  Alemania                    83.149.300         357.022  Europa      
  Francia                     67.391.582         643.801  Europa      
  Italia                      60.367.477         301.340  Europa      
  España                      47.351.567         505.990  Europa      
  Reino Unido                 67.886.011         243.610  Europa      
  Portugal                    10.295.909          92.212  Europa      
  Suecia                      10.402.070         450.295  Europa      
  Polonia                     38.386.000         312.679  Europa      
  Nigeria                    211.400.708         923.768  Africa      
  Etiopia                    120.283.026       1.104.300  Africa      
  Egipto                     102.334.404       1.001.449  Africa      
  Sudafrica                   60.041.994       1.219.090  Africa      
  Kenia                       54.985.698         580.367  Africa      
  Tanzania                    63.298.550         945.087  Africa      
  Australia                   25.788.215       7.692.024  Oceania     
  Nueva Zelanda                5.084.300         268.021  Oceania       
  ---------------------------------------------------------------------

  opcion 2 

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
    6) América
    7) África
    8) Oceanía
    9) Antártida
    0) Cancelar
  Elegí una opción: 4

  ✓ País 'Rumania' agregado correctamente.

  Presioná Enter para continuar...

    Elegí una opción: 3

  ── Actualizar país ──
  Nombre del país: Rumania 

  Datos actuales de 'Rumania':
    Población:  19.237.691
    Superficie: 238.397 km²

  ¿Qué actualizar?
    1) Población
    2) Superficie
    0) Cancelar
  Opción: 

   Elegí una opción: 4

  ── Buscar país ──
    1) Coincidencia exacta
    2) Coincidencia parcial
  Opción: 2
  Texto a buscar: ruman

  Se encontraron 1 resultado(s):
  ---------------------------------------------------------------------
  NOMBRE                       POBLACIÓNSUPERFICIE (km²)  CONTINENTE  
  ---------------------------------------------------------------------
  Rumania                     19.237.691         238.397  Europa      
  ---------------------------------------------------------------------

  Presioná Enter para continuar...

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
    6) América
    7) África
    8) Oceanía
    9) Antártida
    0) Cancelar
  Elegí una opción: 4

  Se encontraron 9 país(es):
  ---------------------------------------------------------------------
  NOMBRE                       POBLACIÓNSUPERFICIE (km²)  CONTINENTE  
  ---------------------------------------------------------------------
  Alemania                    83.149.300         357.022  Europa      
  Francia                     67.391.582         643.801  Europa      
  Italia                      60.367.477         301.340  Europa      
  España                      47.351.567         505.990  Europa      
  Reino Unido                 67.886.011         243.610  Europa      
  Portugal                    10.295.909          92.212  Europa      
  Suecia                      10.402.070         450.295  Europa      
  Polonia                     38.386.000         312.679  Europa      
  Rumania                     19.237.691         238.397  Europa      
  ---------------------------------------------------------------------

  Presioná Enter para continuar...

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

  Países ordenados por Nombre (Ascendente):
  ---------------------------------------------------------------------
  NOMBRE                       POBLACIÓNSUPERFICIE (km²)  CONTINENTE  
  ---------------------------------------------------------------------
  Alemania                    83.149.300         357.022  Europa      
  Angola                     122.220.000   1.215.616.516  Africa      
  Argentina                   45.376.763       2.780.400  America     
  Australia                   25.788.215       7.692.024  Oceania     
  Brasil                     213.993.437       8.515.767  America     
  Chile                       19.116.201         756.102  America     
  China                    1.412.600.000       9.596.960  Asia        
  Colombia                    51.265.844       1.141.748  America     
  Corea del Sur               51.780.579         100.210  Asia        
  Egipto                     102.334.404       1.001.449  Africa      
  España                      47.351.567         505.990  Europa      
  Etiopia                    120.283.026       1.104.300  Africa      
  Francia                     67.391.582         643.801  Europa      
  India                    1.393.409.038       3.287.263  Asia        
  Indonesia                  273.523.615       1.904.569  Asia        
  Italia                      60.367.477         301.340  Europa      
  Japon                      125.800.000         377.975  Asia        
  Kenia                       54.985.698         580.367  Africa      
  Mexico                     128.932.753       1.964.375  America     
  Nigeria                    211.400.708         923.768  Africa      
  Nueva Zelanda                5.084.300         268.021  Oceania     
  Peru                        33.359.418       1.285.216  America     
  Polonia                     38.386.000         312.679  Europa      
  Portugal                    10.295.909          92.212  Europa      
  Reino Unido                 67.886.011         243.610  Europa      
  Rumania                     19.237.691         238.397  Europa      
  Sudafrica                   60.041.994       1.219.090  Africa      
  Suecia                      10.402.070         450.295  Europa      
  Tailandia                   71.601.103         513.120  Asia        
  Tanzania                    63.298.550         945.087  Africa      
  Uruguay                      3.574.900         176.215  America     
  Venezuela                   28.301.696         912.050  America     
  ---------------------------------------------------------------------

  Presioná Enter para continuar...

    Elegí una opción: 7

  ── Estadísticas ──
Población:
     Mayor: China → 1.412.600.000
     Menor: Uruguay → 3.574.900
     Promedio: 156.954.370

Superficie promedio: 39.556.498 km²

Países por continente:
     Africa: 7
     America: 8
     Asia: 6
     Europa: 9
     Oceania: 2

Total de países: 32

  Presioná Enter para continuar...

  ======================================================
  Elegí una opción: 0

  ¡Hasta luego!

```bash
python tpi_paises.py
```

## Autores
Nicolas Sancholuz
Agustín Fernández

## Institución

Universidad Tecnológica Nacional (UTN)
Tecnicatura Universitaria en Programación
