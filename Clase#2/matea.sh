#!/bin/bash

# Usuario: Matea

# Filtrando filas donde el campo 2 contiene "Toro" y el campo 6 es mayor que 1600000
awk '$2~ /Toro/ && $6>1600000 {print $0}' nomina > nomina14

# Filtrando solo las filas con la palabra "Rico" en el tercer campo
awk '$3~ /Rico/ {print $0}' nomina > nomina12

# Filtrando las filas de "Soltera" y salario mayor a 800000
awk '$7~ /Soltera/ && $6>800000 {print $0}' nomina > nomina18
