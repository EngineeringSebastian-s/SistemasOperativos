# SistemasOperativos

## 1. Introducción

Este documento describe una serie de prácticas realizadas como parte del curso de **Sistemas Operativos**, con el objetivo de aprender y poner en práctica conceptos clave relacionados con la administración de sistemas, gestión de memoria y manejo de procesos. Las prácticas se han llevado a cabo en entornos Linux, utilizando principalmente distribuciones como **Kali Linux** y **Ubuntu**. A lo largo de estas prácticas, se abordaron varios algoritmos fundamentales, tales como los de **gestión de memoria**, **memoria virtual** y **asignación de prioridades de procesos**, así como la manipulación de procesos y el uso de herramientas comunes en sistemas operativos Linux.

## 2. Objetivo del Ejercicio

El principal objetivo de las prácticas fue:

1. **Familiarizarse con el entorno Linux**: Realizar tareas administrativas, uso de comandos y comprender el manejo de procesos y recursos dentro del sistema operativo.
2. **Estudiar y simular algoritmos de gestión de memoria**: Implementar y analizar diversos algoritmos utilizados en la gestión de memoria dentro de un sistema operativo, como **paginación**, **segmentación**, y **memoria virtual**.
3. **Comprender la asignación de prioridades de procesos**: Analizar cómo el sistema operativo gestiona los procesos mediante asignación de prioridades para su ejecución, y experimentar con los algoritmos de planificación de procesos.
4. **Profundizar en los conceptos clave de la administración de recursos**: Explorar cómo un sistema operativo maneja los recursos limitados (memoria, CPU, etc.) y garantizar que los procesos se ejecuten de manera eficiente.

## 3. Detalle de las Prácticas Realizadas

### 3.1 Prácticas en Linux (Kali y Ubuntu)

Las primeras actividades del curso se centraron en el trabajo con las distribuciones **Kali Linux** y **Ubuntu**, dos sistemas basados en Linux ampliamente utilizados en el ámbito profesional. A través de estas prácticas se cubrieron los siguientes aspectos:

- **Manejo de terminal**: Uso de comandos básicos de Linux, como `ls`, `cd`, `cp`, `mv`, `rm`, y comandos más avanzados como `awk`, `grep`, `sed`, y `find` para la manipulación de archivos y procesamiento de texto.
- **Gestión de usuarios y permisos**: Ejercicios sobre cómo administrar usuarios, grupos, permisos de archivos y directorios (`chmod`, `chown`, `useradd`, `passwd`).
- **Monitoreo de procesos**: Uso de comandos como `ps`, `top`, `htop` y `kill` para observar el estado de los procesos y la memoria, y aprender a gestionarlos (suspender, finalizar, cambiar prioridad).
- **Configuración de redes**: Configuración básica de red, administración de interfaces de red y diagnóstico con herramientas como `ifconfig`, `netstat`, y `ping`.

### 3.2 Gestión de Memoria

Una parte fundamental del curso fue comprender cómo los sistemas operativos gestionan la memoria disponible. Algunas de las prácticas incluyen:

- **Paginación**: Implementación y simulación de **algoritmos de paginación** para manejar la memoria virtual. Se abordaron conceptos como **marcos de página** y **páginas de memoria**, y cómo el sistema operativo utiliza una tabla de páginas para gestionar la memoria.
- **Segmentación**: Implementación del algoritmo de **segmentación**, que permite dividir la memoria en segmentos lógicos, facilitando la organización de la memoria según el tipo de datos (código, datos, pila).
- **Memoria Virtual**: Simulación de la **memoria virtual**, que permite a los programas usar más memoria de la que está físicamente disponible, al mover páginas entre la memoria física y el disco duro según sea necesario. Se exploraron las técnicas que permiten optimizar el uso de la memoria, como la **paginación por demanda** y el uso de **memoria compartida**.

### 3.3 Asignación de Prioridades de Procesos

Otra parte esencial de las prácticas fue el estudio y la implementación de algoritmos que permiten gestionar la ejecución de procesos en el sistema operativo, dando prioridad a ciertos procesos según diversas estrategias:

- **Planificación de procesos**: Estudio de algoritmos de planificación de procesos como el **Round Robin (RR)**, **First Come First Served (FCFS)**, y **Shortest Job Next (SJN)**. Cada algoritmo tiene sus características en términos de eficiencia y prioridades de ejecución.
- **Asignación de prioridades**: Aprender cómo se asignan prioridades a los procesos mediante **prioridades estáticas** o **dinámicas**, y cómo el sistema operativo decide qué proceso debe ejecutarse en un momento determinado.
- **Simulación de colas de procesos**: Implementación de sistemas que simulan la cola de procesos y la ejecución en función de su prioridad. Se hizo especial énfasis en la **inversión de prioridades** y cómo resolver este tipo de problemas mediante técnicas como **prioridad heredada**.

## 4. Herramientas y Lenguajes Utilizados

Las herramientas y lenguajes utilizados en las prácticas incluyen:

- **Distribuciones Linux**: Kali Linux y Ubuntu fueron los entornos principales utilizados para realizar las prácticas.
- **Bash**: El scripting en Bash fue utilizado para automatizar tareas y simular algunos algoritmos de gestión de memoria y procesos.
- **Python**: Algunos de los ejercicios más complejos relacionados con la gestión de memoria y la asignación de prioridades de procesos fueron implementados en el lenguaje de programación Python.
- **Herramientas de administración de sistemas**: Se utilizaron herramientas de monitoreo y gestión de procesos y memoria como `top`, `ps`, `htop`, `free`, `vmstat`, `kill`, y otros.
