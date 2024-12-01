#!/bin/bash

# Script para ejecutar tareas relacionadas con el usuario 'Sebastian'

# 1. Ingresar como el usuario 'Sebastian'
echo "Iniciando sesión como el usuario 'Sebastian'..."
su - Sebastian -c "echo 'Sesión iniciada como Sebastian'"

# 2. Crear el archivo 'Nomina' y agregar contenido
echo "Creando archivo 'Nomina' en el directorio de Sebastian..."
su - Sebastian -c "echo -e 'Rufina!Toro!Moreno!860000!Secretaria!Ninguno!860000!Soltera\nCinforosa!García!Moreno!1700000!Programador!Tecnóloga!1700000!Casada\nMatea!Patiño!Moreno!3000000!Analista!Ingeniera!3000000!Soltera' > /home/practicas44/Nomina"

# 3. Mostrar el contenido del archivo 'Nomina'
echo "Mostrando el contenido del archivo 'Nomina' en el directorio de Sebastian..."
su - Sebastian -c "cat /home/practicas44/Nomina"

# 4. Filtrar el archivo usando 'awk' para mostrar solo el primer campo
echo "Filtrando el archivo 'Nomina' para mostrar solo el primer campo..."
su - Sebastian -c "awk -F '!' '{print \$1}' /home/practicas44/Nomina"

# 5. Filtrar el archivo usando 'awk' con delimitador '!' y mostrar el primer campo
echo "Filtrando el archivo con 'awk' usando '!' como delimitador..."
su - Sebastian -c "awk -F '!' '{print \$1}' /home/practicas44/Nomina"

# 6. Filtrar el archivo con condiciones específicas
echo "Filtrando el archivo 'Nomina' con condiciones específicas..."
su - Sebastian -c "awk -F '!' '\$1!~ /Matea/ && \$2~ /^P/ {print \$0}' /home/practicas44/Nomina"

# 7. Guardar el resultado filtrado en un nuevo archivo 'Nomina22'
echo "Guardando el resultado filtrado en 'Nomina22'..."
su - Sebastian -c "awk -F '!' '\$2~ /Toro/ && \$6~ /a\$/' /home/practicas44/Nomina > /home/practicas44/Nomina22"

# 8. Ver el contenido de 'Nomina22'
echo "Mostrando el contenido de 'Nomina22'..."
su - Sebastian -c "cat /home/practicas44/Nomina22"

# 9. Realizar más filtrados y guardar en otros archivos como 'Nomina30', 'Nomina31', etc.
echo "Filtrando más datos y guardando en 'Nomina30'..."
su - Sebastian -c "awk -F '!' '\$2~ /Restrepo/ || \$4<900000 {print \$0}' /home/practicas44/Nomina > /home/practicas44/Nomina30"

echo "Mostrando el contenido de 'Nomina30'..."
su - Sebastian -c "cat /home/practicas44/Nomina30"

# 10. Realizar un filtrado final y guardar en 'Nomina34'
echo "Filtrando por condiciones finales y guardando en 'Nomina34'..."
su - Sebastian -c "awk -F '!' '\$1!~ /Cinforosa/ && \$4>=950000 && \$4<=2600000 {print \$0}' /home/practicas44/Nomina > /home/practicas44/Nomina34"

# 11. Mostrar el contenido de 'Nomina34'
echo "Mostrando el contenido de 'Nomina34'..."
su - Sebastian -c "cat /home/practicas44/Nomina34"

echo "Tareas relacionadas con el usuario 'Sebastian' completadas."
