## 🌀 Round Robin Scheduler Simulator

Simulador educativo del algoritmo de planificación **Round Robin**, implementado en Python. Permite modelar procesos con tiempos de llegada, operaciones de E/S, cambios de contexto y cuantums, generando métricas de desempeño y un diagrama de Gantt.

---

### 📂 Estructura del Proyecto

```
round_robin_simulator/
│
├── main.py                  # Punto de entrada con ejemplo de simulación
├── simulator.py             # Lógica principal del algoritmo Round Robin
├── process_utils.py         # Funciones auxiliares para manipulación de procesos
├── io_utils.py              # Manejo de operaciones de entrada/salida
├── metrics.py               # Cálculo y visualización de métricas
└── README.md                # Documentación del proyecto
```

---

### ⚙️ Características

* Simula planificación **Round Robin** con:

  * Quantum configurable
  * Tiempo de cambio de contexto
  * Operaciones de entrada/salida (I/O)
* Imprime la cola de listos por ciclo
* Calcula:

  * ⏱ Tiempo de retorno (Turnaround Time)
  * ⏳ Tiempo de espera (Waiting Time)
* Muestra un **diagrama de Gantt** textual
* Modular y fácilmente extensible

---

### 🚀 Cómo ejecutar

```bash
# Clona el repositorio (o copia los archivos localmente)
git clone https://github.com/EngineeringSebastian-s/SistemasOperativos.git
cd SistemasOperativos/round_robin/

# Ejecuta el archivo principal
python main.py
```

---

### 🧪 Ejemplo de configuración (`main.py`)

```python
processes = [
    {
        'id': 0,
        'arrival_time': 0,
        'cpu_time': 10,
        'remaining_time': 10,
        'io_times': [2, 2],
        'cpu_after_io': [1, 2]
    },
    {
        'id': 1,
        'arrival_time': 80,
        'cpu_time': 12,
        'remaining_time': 12,
        'io_times': [2],
        'cpu_after_io': [2]
    },
    {
        'id': 2,
        'arrival_time': 200,
        'cpu_time': 5,
        'remaining_time': 5,
        'io_times': [],
        'cpu_after_io': []
    }
]

quantum = 4
context_switch_time = 1
```

---

### 📊 Ejemplo de salida

```
Clock 0 ms: Ready queue: [0]
Clock 4 ms: Ready queue: [0]
Clock 7 ms: Ready queue: [0]
Clock 10 ms: Ready queue: [0, 1]
...

Gantt Chart:
Process 0: 0 ms -> 4 ms
Process 0: 5 ms -> 9 ms
Process 0: 10 ms -> 11 ms
...

Process Execution Results:
Process 0: Turnaround Time = 19 ms, Waiting Time = 6 ms
Process 1: Turnaround Time = 22 ms, Waiting Time = 8 ms
...

Average Turnaround Time: 20.33 ms
Average Waiting Time: 7.33 ms
```

---

### 🧠 ¿Cómo funciona?

* Se agregan procesos a la cola cuando su `arrival_time` <= reloj actual
* Se ejecuta un proceso por `quantum` o menos si su CPU restante es menor
* Si requiere E/S, se simula con `io_times` y se incrementa el `remaining_time` con `cpu_after_io`
* Se simulan cambios de contexto (`context_switch_time`)
* Al final se calcula el rendimiento del sistema

---

### 📚 Requisitos

* Python 3.7+
* No se requieren librerías externas

---

### ✍️ Autor

**Sebastián López Osorno**
Estudiante de Ingeniería Informática
Politécnico Jaime Isaza Cadavid
📧 [sebas@example.com](mailto:seabstianlopezosorno2005@gmail.com)

---

### ✅ Licencia

Este proyecto es de uso libre con fines educativos. Puedes modificarlo, compartirlo y adaptarlo bajo los términos de la [MIT License](LICENSE).
