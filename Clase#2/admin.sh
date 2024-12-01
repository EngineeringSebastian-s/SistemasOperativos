#!/bin/bash

# Usuario: root (kali)

# Abriendo el archivo "nomina" con pico
pico nomina

# Imprimiendo solo el primer campo (primer nombre)
awk '{print $1}' nomina

# Imprimiendo los primeros 4 campos y el campo 6
awk '{print $1,$2,$3,$6}' nomina

# Concatenando sin espacios los campos
awk '{print $1 $2 $3 $6}' nomina

# Filtrando solo las filas con la palabra "Rico" en el tercer campo
awk '$3~ /Rico/ {print $0}' nomina

# Filtrando y guardando el resultado en nomina12
awk '$3~ /Rico/ {print $0}' nomina > nomina12

# Visualizando el contenido de nomina12
more nomina12

# Filtrando filas donde el campo 2 contiene "Toro" y el campo 6 es mayor que 1600000
awk '$2~ /Toro/ && $6>1600000 {print $0}' nomina

# Filtrando y guardando el resultado en nomina14
awk '$2~ /Toro/ && $6>1600000 {print $0}' nomina > nomina14

# Filtrando filas donde el campo 2 contiene "Ruiz" o el campo 6 es menor a 1800000
awk '$2~ /Ruiz/ || $6<1800000 {print $0}' nomina > nomina16

# Filtrando por Soltera y salario mayor a 800000
awk '$7~ /Soltera/ &&  $6>800000 {print $0}' nomina

# Filtrando por nombre que termine en "a", el campo 2 que empiece con "t" y que sea Analista y Casada
awk '$1~ /a$/ && $2~ /^t/ && $5~ /Analista/ && $7~ /Casada/ {print $0}' nomina > nomina22

# Comprobando los permisos del archivo nomina22
ls -l nomina22
