#!/bin/bash

# Usuario: Rufina

# Filtrando por nombre que empiece con "R", el campo 2 que termine en "o", el campo 3 que termine en "z" y que sea Soltera
awk '$1~ /^R/ && $2~ /o$/ && $3~ /z$/ && $7~ /Soltera/ {print $0}' nomina > nomina20

# Filtrando filas donde el campo 2 contiene "Toro" y el campo 6 es mayor que 1600000
awk '$2~ /Toro/ && $6>1600000 {print $0}' nomina > nomina14

# Comprobando los permisos del archivo nomina22
ls -l nomina22
