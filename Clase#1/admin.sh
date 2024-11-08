#!/bin/bash
# admin_script.sh
# Este script debe ser ejecutado con privilegios de administrador para crear usuarios y ajustar permisos de archivos binarios.

# Mostrar el contenido del archivo /etc/passwd, que contiene información de las cuentas de usuario del sistema.
echo "Mostrando el contenido de /etc/passwd:"
cat /etc/passwd
echo -e "\n------------------------------------\n"

# Mostrar el contenido del archivo /etc/group, que contiene información sobre los grupos del sistema.
echo "Mostrando el contenido de /etc/group:"
cat /etc/group
echo -e "\n------------------------------------\n"

# Crear usuario 'Anacreta' en el grupo 'Linux25' con directorio de inicio y shell /bin/bash
echo "Creando usuario 'Anacreta' en el grupo 'Linux25'..."
useradd -g Linux25 -d /home/labor -m -s /bin/bash Anacreta

# Crear usuario 'Marcela' en el grupo 'Matematicas' con directorio de inicio y shell /bin/bash
echo "Creando usuario 'Marcela' en el grupo 'Matematicas'..."
useradd -g Matematicas -d /home/prac -m -s /bin/bash Marcela

# Establecer la contraseña para el usuario 'Anacreta'
echo "Estableciendo contraseña para 'Anacreta':"
passwd Anacreta

# Establecer la contraseña para el usuario 'Marcela'
echo "Estableciendo contraseña para 'Marcela':"
passwd Marcela

# Crear usuario 'Lorena' en el grupo 'Fisica' con directorio de inicio y shell /bin/bash
echo "Creando usuario 'Lorena' en el grupo 'Fisica'..."
useradd -g Fisica -d /home/ejer -m -s /bin/bash Lorena

# Establecer la contraseña para el usuario 'Lorena'
echo "Estableciendo contraseña para 'Lorena':"
passwd Lorena

# Cambiar a la carpeta /bin para modificar permisos de ciertos archivos en /usr/bin
cd /bin

# Modificar permisos de archivos binarios en /usr/bin para restringir o permitir su uso
echo "Modificando permisos de los archivos en /usr/bin para acceso restringido..."

# Dar permisos 747 a cat (lectura, escritura y ejecución para el dueño, lectura y ejecución para otros)
chmod 747 /usr/bin/cat
echo "Permisos para /usr/bin/cat ajustados a 747."

# Dar permisos 555 a grep (solo lectura y ejecución para todos los usuarios)
chmod 555 /usr/bin/grep
echo "Permisos para /usr/bin/grep ajustados a 555."

# Dar permisos 555 a wc (solo lectura y ejecución para todos los usuarios)
chmod 555 /usr/bin/wc
echo "Permisos para /usr/bin/wc ajustados a 555."

# Dar permisos 555 a more (solo lectura y ejecución para todos los usuarios)
chmod 555 /usr/bin/more
echo "Permisos para /usr/bin/more ajustados a 555."

# Dar permisos 555 a less (solo lectura y ejecución para todos los usuarios)
chmod 555 /usr/bin/less
echo "Permisos para /usr/bin/less ajustados a 555."

# Dar permisos 555 a nl (solo lectura y ejecución para todos los usuarios)
chmod 555 /usr/bin/nl
echo "Permisos para /usr/bin/nl ajustados a 555."

echo "Script completado. Usuarios creados y permisos ajustados."
