#!/bin/bash

# Usuario: Anacarota

# Filtrando las filas de "Soltera" y salario mayor a 800000
awk '$7~ /Soltera/ &&  $6>800000 {print $0}' nomina > nomina18

# Filtrando por el campo 2 que contenga "Ruiz" o donde el salario (campo 6) sea menor que 1800000
awk '$2~ /Ruiz/ || $6<1800000 {print $0}' nomina > nomina16

# Filtrando las filas con el campo 6 mayor que 1600000 y el nombre que termine en "a"
awk '$7~ /Soltera/ &&  $6>800000 && $1~ /a$/ {print $0}' nomina > nomina22
