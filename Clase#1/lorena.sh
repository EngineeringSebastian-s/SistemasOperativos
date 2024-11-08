#!/bin/bash
# lorena_script.sh
# Este script simula acciones realizadas por el usuario 'Lorena' en su sesión, comenzando con el cambio a su cuenta.

# Cambiar a la cuenta de usuario 'Lorena'
echo "Cambiando a la cuenta de usuario 'Lorena'..."
su - Lorena

# Crear o editar el archivo 'datos3' usando el editor 'pico' (o nano)
echo "Editando el archivo 'datos3' con el editor pico..."
pico datos3

# Mostrar el contenido del archivo 'datos3' usando el comando 'more' para verlo en pantalla paginada
echo "Mostrando el contenido de 'datos3' con more..."
more datos3

# Cambiar los permisos de 'datos3' para lectura y escritura para todos los usuarios (666)
echo "Cambiando permisos de 'datos3' a 666 (lectura y escritura para todos)..."
chmod 666 datos3

# Listar los detalles del archivo 'datos3' en formato largo para verificar sus permisos y propiedades
echo "Listando los detalles de 'datos3' después de cambiar permisos..."
ls -l datos3

echo "Script de Lorena completado."
