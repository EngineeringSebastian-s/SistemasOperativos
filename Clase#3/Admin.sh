#!/bin/bash

# Verificar si el script se está ejecutando como superusuario
if [ "$(id -u)" -ne 0 ]; then
    echo "Este script debe ejecutarse como superusuario."
    exit 1
fi

# 1. Crear el usuario 'Sebastian' si no existe
if id "Sebastian" &>/dev/null; then
    echo "El usuario 'Sebastian' ya existe."
else
    echo "Creando el usuario 'Sebastian'..."
    useradd -m -s /bin/bash Sebastian
    echo "Usuario 'Sebastian' creado exitosamente."
fi

# 2. Asignar una contraseña al usuario 'Sebastian'
echo "Asignando una contraseña para el usuario 'Sebastian'..."
echo "Sebastian:Contraseña123" | chpasswd
echo "Contraseña asignada correctamente."

# 3. Otorgar permisos de escritura en su directorio home
echo "Otorgando permisos de escritura al directorio de 'Sebastian'..."
chmod 700 /home/Sebastian
chown Sebastian:Sebastian /home/Sebastian
echo "Permisos otorgados exitosamente."

# 4. Agregar al usuario 'Sebastian' a un grupo adicional si es necesario (opcional)
# echo "Agregando 'Sebastian' al grupo 'sudo' para permisos de administrador (opcional)..."
# usermod -aG sudo Sebastian
# echo "'Sebastian' agregado al grupo 'sudo'."

# 5. Verificar que el usuario se haya creado correctamente
echo "Verificando la creación del usuario 'Sebastian'..."
id Sebastian

echo "Script ejecutado correctamente."
