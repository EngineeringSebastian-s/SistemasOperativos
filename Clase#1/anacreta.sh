#!/bin/bash
# anacreta_script.sh
# Este script simula acciones realizadas por el usuario 'Anacreta' en su sesión, comenzando con el cambio a su cuenta.

# Cambiar a la cuenta de usuario 'Anacreta'
echo "Cambiando a la cuenta de usuario 'Anacreta'..."
su - Anacreta

# Crear o editar el archivo 'datos1' usando el editor 'pico' (o nano)
echo "Editando el archivo 'datos1' con el editor pico..."
pico datos1

# Mostrar el contenido del archivo 'datos1' usando el comando 'more' para verlo en pantalla paginada
echo "Mostrando el contenido de 'datos1' con more..."
more datos1

# Listar los detalles del archivo 'datos1' en formato largo para verificar sus permisos y propiedades
echo "Listando los detalles de 'datos1'..."
ls -l datos1

# Cambiar los permisos de 'datos1' para lectura y escritura para todos los usuarios (666)
echo "Cambiando permisos de 'datos1' a 666 (lectura y escritura para todos)..."
chmod 666 datos1

# Listar de nuevo los detalles de 'datos1' para confirmar el cambio de permisos
echo "Listando los detalles de 'datos1' después de cambiar permisos..."
ls -l datos1

# Listar los detalles del archivo '/etc/cat' si existe
echo "Listando los detalles del archivo '/etc/cat' (si existe)..."
ls -l /etc/cat

# Buscar el término 'Opita' en varios archivos y contar el número de coincidencias usando 'wc -l'
echo "Contando las ocurrencias de 'Opita' en 'datos1', '/home/prac/datos2' y '/home/ejer/datos3'..."
cat datos1 /home/prac/datos2 /home/ejer/datos3 | grep Opita | wc -l

# Mostrar todas las líneas que contienen 'Opita' en 'datos1', '/home/prac/datos2' y '/home/ejer/datos3'
echo "Mostrando las líneas que contienen 'Opita' en los archivos..."
cat datos1 /home/prac/datos2 /home/ejer/datos3 | grep Opita

# Abrir el editor 'vi' (esta línea requiere interacción manual, si se ejecuta desde un script puede quedarse en espera)
echo "Abriendo el editor 'vi' (esto requiere intervención manual y puede detener el script)."
vi

# Repetir la búsqueda de 'Opita' en los archivos después de salir de 'vi'
echo "Repitiendo la búsqueda de 'Opita' después de salir de vi..."
cat datos1 /home/prac/datos2 /home/ejer/datos3 | grep Opita

# Contar de nuevo las ocurrencias de 'Opita' después de salir de vi
echo "Recontando las ocurrencias de 'Opita' después de salir de vi..."
cat datos1 /home/prac/datos2 /home/ejer/datos3 | grep Opita | wc -l

echo "Script de Anacreta completado."
