# Clase 02/11/2024

El ejercicio realizado tuvo como objetivo principal la práctica y el entendimiento de comandos esenciales en sistemas operativos basados en Linux, específicamente en la manipulación de archivos y usuarios mediante el uso de herramientas como awk, cat, passwd, y useradd. Durante la sesión, se trabajó en la creación de usuarios, asignación de grupos y modificación de archivos, lo que permitió conocer las técnicas básicas de administración de sistemas y gestión de datos.

Se abordaron tanto tareas administrativas, realizadas desde la cuenta de superusuario (root), como tareas operativas, ejecutadas desde una cuenta de usuario normal, para familiarizarse con el manejo de permisos y la ejecución de procesos. Además, se centró en la extracción y filtrado de datos dentro de archivos de texto (como el archivo de nómina Nomina) mediante el uso de expresiones regulares y comandos de filtrado avanzados.

#### **1. Acciones del Administrador (root)**

**1.1 Acceso como root:**

Se inicia sesión como superusuario (root) mediante el comando `sudo su`.

```bash
sudo su
```

**1.2 Visualización del archivo `/etc/passwd`:**

Se muestra el contenido del archivo `/etc/passwd`, que contiene información sobre los usuarios del sistema.

```bash
cat /etc/passwd
```

El resultado muestra la configuración de usuarios, como `root`, `daemon`, `bin`, entre otros.

**1.3 Creación de un nuevo grupo:**

Se crea un grupo llamado `linuxpero56`.

```bash
groupadd linuxpero56
```

**1.4 Verificación del contenido del archivo `/etc/passwd`:**

Tras la creación del grupo, se vuelve a verificar el archivo `/etc/passwd` para comprobar los usuarios en el sistema. No se ve ninguna diferencia significativa en la salida de este archivo.

```bash
cat /etc/passwd
```

**1.5 Visualización del archivo `/etc/group`:**

El archivo `/etc/group` contiene información sobre los grupos del sistema. Se visualiza para confirmar la creación del grupo `linuxpero56`.

```bash
cat /etc/group
```

**1.6 Creación de un nuevo usuario:**

Se crea un nuevo usuario llamado `Sebastian`, con el grupo `linuxpero56`, una carpeta home ubicada en `/home/practicas44` y con el shell `/bin/bash`. La opción `-m` asegura que se cree el directorio home del usuario.

```bash
useradd -g linuxpero56 -d /home/practicas44 -m -s /bin/bash Sebastian
```

**1.7 Verificación del archivo `/etc/passwd`:**

Se revisa el archivo `/etc/passwd` nuevamente y se confirma que el usuario `Sebastian` ha sido creado exitosamente.

```bash
cat /etc/passwd
```

**1.8 Cambio de contraseña para el usuario `Sebastian`:**

Se establece una contraseña para el usuario `Sebastian`.

```bash
passwd Sebastian
```

---

#### **2. Acciones de Sebastián (usuario normal)**

**2.1 Cambio al usuario `Sebastian`:**

Se realiza el cambio de usuario al usuario `Sebastian` con el comando `su -`.

```bash
su - Sebastian
```

Se ingresa la contraseña y se accede al entorno de usuario de `Sebastian`.

**2.2 Edición de un archivo de texto (`Nomina`):**

Se utiliza el editor `pico` para abrir el archivo `Nomina`.

```bash
pico Nomina
```

**2.3 Visualización del contenido del archivo `Nomina`:**

Se observa el contenido del archivo `Nomina`, que contiene una lista de empleados con sus datos separados por el símbolo `!`.

```bash
cat Nomina
```

**2.4 Comandos `awk` para manipular el contenido del archivo:**

Se usan varios comandos `awk` para filtrar y mostrar datos específicos del archivo `Nomina`:

- **Filtrado por el primer campo (primer nombre):**
  ```bash
  awk '{print $1}' Nomina
  ```

- **Filtrado por el primer campo usando un delimitador personalizado (¡):**
  ```bash
  awk -F '!' '{print $1}' Nomina
  ```

- **Visualización de todas las líneas sin modificaciones:**
  ```bash
  awk -F '!' '{print $0}' Nomina
  ```

- **Filtrado con condiciones sobre los campos:**

  - Filtrado con condiciones de nombre y apellido:
    ```bash
    awk -F '!' '$1!~ /Matea/ && $2~ /^P/ {print $0}' Nomina
    ```

  - Filtrado con condiciones sobre el segundo y sexto campo (apellido y estado civil):
    ```bash
    awk -F '!' '$2~ /Toro/ && $6~ /a$/ {print $0}' Nomina
    ```

  - Guardar el resultado en un nuevo archivo `Nomina22`:
    ```bash
    awk -F '!' '$2~ /Toro/ && $6~ /a$/ {print $0}' Nomina > Nomina22
    ```

  - Visualización del archivo generado:
    ```bash
    cat Nomina22
    ```

  - Filtrado por condiciones sobre los campos de salario y estado civil:
    ```bash
    awk -F '!' '$2~ /Restrepo/ || $4<900000 {print $0}' Nomina
    ```

  - Guardado de los resultados en `Nomina30`:
    ```bash
    awk -F '!' '$2~ /Restrepo/ || $4<900000 {print $0}' Nomina > Nomina30
    ```

  - Filtrado por salario y estado civil:
    ```bash
    awk -F '!' '$8!~ /Soltera/ && $4>688000 {print $0}' Nomina
    ```

  - Filtrado por estado civil y apellido:
    ```bash
    awk -F '!' '$8!~ /Soltera/ && $4>688000 && $1!~ /^R/ {print $0}' Nomina
    ```

  - Guardado de resultados en un archivo `Nomina31`:
    ```bash
    awk -F '!' '$8!~ /Soltera/ && $4>688000 && $1!~ /^R/ {print $0}' Nomina > Nomina31
    ```

  - Visualización del archivo generado:
    ```bash
    cat Nomina31
    ```

  - Filtrado por las condiciones de nombre, apellido y salario:
    ```bash
    awk -F '!' '$1~ /a$/ && $2!~ /^T/  && $3~ /z$/ {print $0}' Nomina
    ```

  - Guardado de los resultados en `Nomina32`:
    ```bash
    awk -F '!' '$1~ /a$/ && $2!~ /^T/  && $3~ /z$/ {print $0}' Nomina > Nomina32
    ```

  - Visualización del archivo generado:
    ```bash
    cat Nomina32
    ```

  - Filtrado por apellido y nombre:
    ```bash
    awk -F '!' '$2!~ /o$/ && $3~ /^P/  && $5!~ /Analista/ {print $0}' Nomina
    ```

  - Guardado de resultados en `Nomina33`:
    ```bash
    awk -F '!' '$2!~ /o$/ && $3~ /^P/  && $5!~ /Analista/ {print $0}' Nomina > Nomina33
    ```

  - Visualización del archivo generado:
    ```bash
    cat Nomina33
    ```

  - Filtrado con condiciones en el apellido y salario:
    ```bash
    awk -F '!' '$2~ /^T/ || $3~ /r$/ {print $2,$3,$1,$4}' Nomina
    ```

  - Filtrado de usuarios con ciertas condiciones:
    ```bash
    awk -F '!' '$1!~ /Cinforosa/ && $4>=950000 && $4<=2600000  {print $0}' Nomina
    ```

  - Guardado de resultados en `Nomina34`:
    ```bash
    awk -F '!' '$1!~ /Cinforosa/ && $4>=950000 && $4<=2600000  {print $0}' Nomina > Nomina34
    ```

  - Visualización del archivo generado:
    ```bash
    cat Nomina34
    ```

**2.2 Visualización del archivo `/etc/passwd` usando `awk`:**

Se realizan varias consultas utilizando el comando `awk` para extraer información sobre los usuarios del sistema desde el archivo `/etc/passwd`:

- **Mostrar todos los usuarios del sistema:**
  ```bash
  awk -F ':' '{print $0}' /etc/passwd
  ```

- **Mostrar solo los nombres de usuario:**
  ```bash
  awk -F ':' '{print $1}' /etc/passwd
  ```

- **Mostrar los IDs de usuario (UID):**
  ```bash
  awk -F ':' '{print $3}' /etc/passwd
  ```

- **Filtrar los usuarios cuyo nombre comience con `C`:**
  ```bash
  awk -F ':' '$1~ /^C/ {print $1}' /etc/passwd
  ```

- **Filtrar usuarios con ciertas condiciones sobre nombre y UID:**
  ```bash
  awk -F ':' '$1~ /^C/ && $1~ /a$/ && $3>250 {print $0}' /etc/passwd
  ```

- **Filtrar usuarios con ciertas condiciones sobre UID:**
  ```bash
  awk -F ':' '$1!~ /^S/ && $1!~ /a$/ && $3<600 {print $0}' /etc/passwd
  ```

- **Mostrar los usuarios con el shell `nologin`:**
  ```bash
  awk -F ':' '$7~ /nologin$/ {print $0}' /etc/passwd
  ```
