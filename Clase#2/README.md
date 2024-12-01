### **Ejercicio de Filtrado y Manipulación de Archivos con `awk` en Linux**

Este ejercicio documenta los pasos realizados en un entorno Linux utilizando el comando `awk` para filtrar y manipular un archivo de texto llamado `nomina`. A través de estos pasos, se ha trabajado con el archivo para extraer información específica, concatenar datos, filtrar filas según diferentes criterios y redirigir los resultados a nuevos archivos.

#### **Objetivo del Ejercicio:**
El objetivo de este ejercicio es aprender a utilizar el comando `awk` y otros comandos de Linux para procesar, filtrar y modificar archivos de texto. Durante la práctica, se realizaron varias operaciones sobre un archivo de texto con información estructurada (por ejemplo, una lista de empleados) para extraer, combinar y guardar información relevante basada en diferentes condiciones.


### 1. **Abrir el archivo `nomina` con el editor `pico`**

#### Comando:
```bash
pico nomina
```

#### Explicación:
- **`pico`** es un editor de texto en modo terminal que permite modificar archivos. Al usar el comando `pico nomina`, se abre el archivo llamado `nomina` para poder visualizar o editar su contenido.
- El archivo `nomina` podría ser un archivo de texto con datos estructurados, por ejemplo, con información de empleados o salarios.

---

### 2. **Imprimir el primer campo (primer nombre) del archivo `nomina` usando `awk`**

#### Comando:
```bash
awk '{print $1}' nomina
```

#### Explicación:
- **`awk`** es una herramienta de procesamiento de texto que permite realizar operaciones en líneas de un archivo.
- El comando `awk '{print $1}' nomina` imprime solo el primer campo de cada línea del archivo `nomina`. El `$1` se refiere al primer campo en cada línea (por defecto, los campos están separados por espacios o tabulaciones).
- Este comando puede ser útil si deseas ver una lista de los primeros nombres de una lista de empleados, por ejemplo.

---

### 3. **Imprimir los primeros 4 campos y el sexto campo**

#### Comando:
```bash
awk '{print $1,$2,$3,$6}' nomina
```

#### Explicación:
- El comando `awk '{print $1,$2,$3,$6}'` imprime los primeros tres campos (`$1`, `$2`, `$3`) y el sexto campo (`$6`) de cada línea del archivo `nomina`.
- Esto puede ser útil cuando necesitas extraer columnas específicas (como el nombre, el apellido, el cargo y el salario de los empleados, por ejemplo).

---

### 4. **Concatenar sin espacios los primeros tres campos y el sexto campo**

#### Comando:
```bash
awk '{print $1 $2 $3 $6}' nomina
```

#### Explicación:
- El comando `awk '{print $1 $2 $3 $6}'` concatena directamente los primeros tres campos y el sexto campo sin agregar espacios entre ellos. Es decir, los campos serán pegados uno detrás de otro sin ningún separador.
- Este tipo de operación puede ser útil cuando necesitas crear identificadores únicos o combinaciones específicas de campos para procesarlos más adelante.

---

### 5. **Filtrar filas donde el tercer campo contiene "Rico"**

#### Comando:
```bash
awk '$3~ /Rico/ {print $0}' nomina
```

#### Explicación:
- El comando `awk '$3~ /Rico/ {print $0}'` filtra todas las líneas del archivo `nomina` donde el tercer campo contiene la palabra "Rico".
- El operador `~` indica que se está haciendo una comparación de texto con una expresión regular, por lo que este comando busca en el tercer campo cualquier línea que tenga la palabra "Rico" (independientemente de si está al principio, en el medio o al final).

---

### 6. **Guardar el resultado filtrado en un nuevo archivo (`nomina12`)**

#### Comando:
```bash
awk '$3~ /Rico/ {print $0}' nomina > nomina12
```

#### Explicación:
- Este comando es una extensión del anterior. Utiliza la redirección de salida `>` para guardar el resultado filtrado en un nuevo archivo llamado `nomina12`.
- Esto es útil si deseas conservar los resultados del filtrado en un archivo separado para revisarlos o procesarlos más adelante.

---

### 7. **Ver el contenido del archivo `nomina12`**

#### Comando:
```bash
more nomina12
```

#### Explicación:
- El comando `more nomina12` muestra el contenido del archivo `nomina12` de manera paginada, lo que te permite ver los resultados del filtrado, uno por uno.
- `more` es útil para leer archivos grandes sin tener que abrir todo el contenido de una sola vez.

---

### 8. **Filtrar filas con "Toro" en el segundo campo y salario mayor a 1,600,000**

#### Comando:
```bash
awk '$2~ /Toro/ && $6>1600000 {print $0}' nomina
```

#### Explicación:
- El comando `awk '$2~ /Toro/ && $6>1600000 {print $0}'` filtra las líneas donde el segundo campo contiene la palabra "Toro" y donde el salario (campo 6) es mayor a 1,600,000.
- Este filtro puede ser útil para buscar registros de personas con un apellido específico (como "Toro") y un salario por encima de un umbral.

---

### 9. **Guardar el resultado filtrado en el archivo `nomina14`**

#### Comando:
```bash
awk '$2~ /Toro/ && $6>1600000 {print $0}' nomina > nomina14
```

#### Explicación:
- Similar al paso 6, este comando guarda el resultado del filtro anterior en un nuevo archivo llamado `nomina14`. La redirección `>` se utiliza para crear y escribir en el archivo de salida.

---

### 10. **Filtrar por "Ruiz" en el segundo campo o salario menor a 1,800,000**

#### Comando:
```bash
awk '$2~ /Ruiz/ || $6<1800000 {print $0}' nomina > nomina16
```

#### Explicación:
- El comando `awk '$2~ /Ruiz/ || $6<1800000 {print $0}'` filtra las filas donde el segundo campo contiene la palabra "Ruiz" o el salario (campo 6) es menor que 1,800,000.
- El operador `||` se utiliza para indicar que cualquier condición verdadera (es decir, si el campo 2 contiene "Ruiz" o el salario es menor a 1,800,000) hace que la línea sea incluida en el resultado.

---

### 11. **Filtrar por "Soltera" en el séptimo campo y salario mayor a 800,000**

#### Comando:
```bash
awk '$7~ /Soltera/ &&  $6>800000 {print $0}' nomina
```

#### Explicación:
- Este comando filtra las filas donde el campo 7 contiene "Soltera" y el salario (campo 6) es mayor a 800,000.
- El operador `&&` indica que ambas condiciones deben cumplirse para que la línea sea incluida en el resultado.

---

### 12. **Filtrar por nombres que terminen en "a", campo 2 empiece con "t", sea "Analista" en el campo 5, y "Casada" en el campo 7**

#### Comando:
```bash
awk '$1~ /a$/ && $2~ /^t/ && $5~ /Analista/ && $7~ /Casada/ {print $0}' nomina > nomina22
```

#### Explicación:
- Este comando realiza un filtro más complejo utilizando varias condiciones:
  - `$1~ /a$/` filtra los nombres que terminan en "a".
  - `$2~ /^t/` filtra el campo 2 para aquellos que comienzan con "t".
  - `$5~ /Analista/` filtra las filas donde el campo 5 contiene la palabra "Analista".
  - `$7~ /Casada/` filtra las filas donde el campo 7 contiene la palabra "Casada".
- El resultado se guarda en el archivo `nomina22`.

---

### 13. **Verificar los permisos del archivo `nomina22`**

#### Comando:
```bash
ls -l nomina22
```

#### Explicación:
- El comando `ls -l nomina22` muestra una lista detallada de los permisos del archivo `nomina22`.
- Esto es útil para verificar si el archivo tiene los permisos adecuados para ser leído, modificado o ejecutado.


