## Clase 24/08/2024

**Ejercicio de Gestión de Usuarios y Permisos en Kali Linux**

Este ejercicio documenta la ejecución de una serie de comandos en Kali Linux para realizar tareas de administración de usuarios, asignación de permisos y manipulación de archivos en la terminal. A continuación, se explica cada paso y los comandos utilizados en el ejercicio.

### 1. Creación de Usuarios

Se utilizaron los comandos `useradd` para crear varios usuarios en el sistema, asignándolos a grupos específicos y configurando sus directorios home y shells predeterminados.

**Comandos ejecutados:**
```bash
useradd -g Linux25 -d /home/labor -m -s /bin/bash Anacreta
useradd -g Matematicas -d /home/prac -m -s /bin/bash Marcela
useradd -g Fisica -d /home/ejer -m -s /bin/bash Lorena
```

- Se crearon tres usuarios: **Anacreta**, **Marcela**, y **Lorena**.
- A cada usuario se le asignó un grupo específico (`Linux25`, `Matematicas`, y `Fisica`, respectivamente).
- Los usuarios fueron configurados con un directorio home específico y una shell predeterminada (`/bin/bash`).

### 2. Establecimiento de Contraseñas para los Usuarios

Se utilizaron los comandos `passwd` para establecer contraseñas para los usuarios recién creados.

**Comandos ejecutados:**
```bash
passwd Anacreta
passwd Marcela
passwd Lorena
```

- Se establecieron contraseñas para cada uno de los usuarios: **Anacreta**, **Marcela**, y **Lorena**.

### 3. Manipulación de Archivos y Modificación de Permisos

Con el comando `chmod` se modificaron los permisos de varios archivos en los directorios de los usuarios. Se les asignó un permiso de lectura y escritura (permiso `666`).

**Comandos ejecutados:**
```bash
chmod 666 /home/labor/datos1
chmod 666 /home/prac/datos2
chmod 666 /home/ejer/datos3
```

- Se cambió el permiso de los archivos `datos1`, `datos2`, y `datos3` a `666`, lo que permite que todos los usuarios puedan leer y escribir en esos archivos.

### 4. Operaciones de Archivos: Visualización y Búsqueda

Se utilizaron varios comandos para manipular los archivos, tales como `cat`, `grep`, `more`, `wc` y `vi`.

**Comandos ejecutados:**
```bash
cat datos1 /home/prac/datos2 /home/ejer/datos3 | grep Opita
cat datos1 /home/prac/datos2 /home/ejer/datos3 | grep Opita | wc -l
more datos1
vi datos1
```

- **`cat`**: Muestra el contenido de los archivos de texto.
- **`grep`**: Filtra las líneas que contienen la palabra "Opita" en el contenido de los archivos.
- **`wc -l`**: Cuenta el número de líneas en los archivos que contienen el término "Opita".
- **`more`**: Muestra el contenido de un archivo, permitiendo la navegación página por página.
- **`vi`**: Permite editar los archivos.

### 5. Comprobación de Permisos y Propiedades de Archivos

El comando `ls -l` fue utilizado para ver los detalles de los archivos, incluidos sus permisos, propietario y grupo.

**Comandos ejecutados:**
```bash
ls -l datos1
ls -l datos2
ls -l datos3
```

- Estos comandos permitieron verificar los permisos y las propiedades de los archivos `datos1`, `datos2`, y `datos3`.

### Propósito y Objetivo del Ejercicio

Este ejercicio tiene como objetivo enseñar y practicar los comandos básicos de administración de usuarios y manejo de archivos en Kali Linux, particularmente enfocados en:

1. **Gestión de Usuarios y Grupos**: Cómo agregar usuarios a grupos y configurar sus entornos.
2. **Manipulación de Archivos**: Uso de comandos como `cat`, `grep`, `more`, `wc`, y `vi` para visualizar, filtrar, y editar archivos.
3. **Control de Permisos**: Cómo modificar los permisos de los archivos usando `chmod`.
4. **Comprobación de Permisos y Propiedades**: Uso de `ls -l` para visualizar información detallada sobre archivos y directorios.

### Recomendaciones y Buenas Prácticas

- Siempre verificar los permisos de los archivos antes de realizar cambios con `chmod`.
- Utilizar `grep` con patrones adecuados para filtrar correctamente el contenido de archivos grandes.
- Realizar un seguimiento adecuado de los cambios realizados en los archivos y usuarios para evitar posibles problemas de seguridad.

### Conclusiones

Este ejercicio proporciona una base sólida para la administración de usuarios y archivos en un sistema Linux, lo cual es esencial para tareas de seguridad y mantenimiento de sistemas operativos en entornos de servidores o de pruebas como Kali Linux.