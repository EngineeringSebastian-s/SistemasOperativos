#!/bin/bash
# marcela_script.sh
# Este script simula las acciones realizadas por el usuario 'Marcela' en su sesión, comenzando con el cambio a su cuenta.

# Cambiar a la cuenta de usuario 'Marcela'
echo "Cambiando a la cuenta de usuario 'Marcela'..."
su - Marcela

# Crear o editar el archivo 'datos2' usando el editor 'pico' (o nano)
echo "Editando el archivo 'datos2' con el editor pico..."
pico datos2

# Mostrar el contenido del archivo 'datos2' usando el comando 'more' para verlo en pantalla paginada
echo "Mostrando el contenido de 'datos2' con more..."
more datos2

# Cambiar los permisos de 'datos2' para lectura y escritura para todos los usuarios (666)
echo "Cambiando permisos de 'datos2' a 666 (lectura y escritura para todos)..."
chmod 666 datos2

# Listar los detalles del archivo 'datos2' en formato largo para verificar sus permisos y propiedades
echo "Listando los detalles de 'datos2' después de cambiar permisos..."
ls -l datos2

echo "Script de Marcela completado."
