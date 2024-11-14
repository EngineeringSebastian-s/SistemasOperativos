import java.util.*;

public class Main {
    public static void main(String[] args) {
        int totalProcesses = getValidInput("Ingrese el total de procesos:", 1, Integer.MAX_VALUE);
        int quantum = getValidInput("Ingrese el valor del quantum (ms):", 1, Integer.MAX_VALUE);
        int contextSwitchTime = getValidInput("Ingrese el valor del tiempo de intercambio (ms):", 1, Integer.MAX_VALUE);
        List<Process> processes = new ArrayList<>();
        for (int i = 0; i < totalProcesses; i++) {
            int arrivalTime = getValidInput("\tIngrese el tiempo de llegada del proceso " + (i) + " (ms):", 0, Integer.MAX_VALUE);

            int cpuTimeInQuantums = getValidInput("\tIngrese el tiempo total necesario en CPU (quantums) del proceso " + (i) + ":", 1, Integer.MAX_VALUE);
            int cpuTime = cpuTimeInQuantums * quantum;

            int ioPhases = getValidInput("\tIngrese la cantidad de entradas/salidas (E/S) del proceso " + (i) + ":", 0, Integer.MAX_VALUE);
            List<Integer> times = new ArrayList<>();

            times.add(cpuTime);

            for (int j = 0; j < ioPhases; j++) {
                int ioTimeInQuantums = getValidInput(
                        "\t\tIngrese el tiempo de E/S numero " + (j + 1) + " del proceso " + (i + 1) + " (quantums):", 1, Integer.MAX_VALUE);
                int ioTime = ioTimeInQuantums * quantum;
                times.add(ioTime);

                int cpuAfterIOInQuantums = getValidInput(
                        "\t\tIngrese el tiempo de CPU necesario después de la E/S numero " + (j + 1) + " del proceso " + (i + 1) + " (quantums):", 1, Integer.MAX_VALUE);
                int cpuAfterIO = cpuAfterIOInQuantums * quantum;
                times.add(cpuAfterIO);
            }

            processes.add(new Process(i, arrivalTime, times));
        }

        simularRoundRobin(processes, quantum, contextSwitchTime);
    }

    private static void simularRoundRobin(List<Process> processes, int quantum, int contextSwitch) {
        StringBuilder ganttChart = new StringBuilder("\n");
        Queue<Process> readyQueue = new LinkedList<>();
        Queue<Process> blockedQueue = new LinkedList<>();
        int currentTime = 0;
        int totalTurnaroundTime = 0, totalWaitingTime = 0;

        processes.sort(Comparator.comparingInt(p -> p.arrivalTime));
        List<Process> completedProcesses = new ArrayList<>();
        boolean firstTime = false;

        while (!processes.isEmpty() || !readyQueue.isEmpty() || !blockedQueue.isEmpty()) {

            if (firstTime) {
                displayReadyQueueWithGantt(readyQueue, ganttChart.toString());
            } else {
                firstTime = true;
            }

            Iterator<Process> blockedIterator = blockedQueue.iterator();
            while (blockedIterator.hasNext()) {
                Process process = blockedIterator.next();
                if (process.currentIoBlockTime <= currentTime) {
                    readyQueue.add(process);
                    blockedIterator.remove();
                }
            }

            while (!processes.isEmpty() && processes.get(0).arrivalTime <= currentTime) {
                readyQueue.add(processes.remove(0));
            }

            if (readyQueue.isEmpty() && processes.isEmpty() && blockedQueue.isEmpty()) {
                break;
            }

            if (!readyQueue.isEmpty()) {
                Process currentProcess = readyQueue.poll();

                if (currentTime == 0) {
                    if (currentProcess.firstExecution) {
                        currentProcess.waitingTime = 0;
                        currentProcess.firstExecution = false;
                    }

                } else {
                    if (currentProcess.firstExecution) {
                        currentProcess.waitingTime = currentTime - currentProcess.arrivalTime;
                        currentProcess.firstExecution = false;
                    }
                }

                ganttChart.append("[P").append(currentProcess.id).append("] ");

                int executedTime = quantum;
                if (currentProcess.currentPhase < currentProcess.times.size()) {
                    currentProcess.times.set(currentProcess.currentPhase, currentProcess.times.get(currentProcess.currentPhase) - executedTime);
                }

                currentTime += executedTime;
                currentTime += contextSwitch;

                if (currentProcess.times.get(currentProcess.currentPhase) == 0) {
                    currentProcess.currentPhase++;
                    if (currentProcess.currentPhase < currentProcess.times.size()) {
                        if (currentProcess.currentPhase % 2 == 0) {
                            readyQueue.add(currentProcess);
                        } else {
                            int blockingTime = currentProcess.times.get(currentProcess.currentPhase);
                            currentProcess.currentIoBlockTime = currentTime + blockingTime + contextSwitch;
                            currentProcess.currentPhase++;
                            blockedQueue.add(currentProcess);
                        }
                    } else {
                        // Process completed
                        currentProcess.totalIoTime = calculateIOTime(currentProcess.times);
                        currentProcess.turnaroundTime = currentTime - currentProcess.arrivalTime - currentProcess.totalIoTime - contextSwitch;
                        completedProcesses.add(currentProcess);
                        totalTurnaroundTime += currentProcess.turnaroundTime;
                        totalWaitingTime += currentProcess.waitingTime;
                    }
                } else {

                    while (!processes.isEmpty() && processes.get(0).arrivalTime <= currentTime) {
                        readyQueue.add(processes.remove(0));
                    }

                    if (currentProcess.times.get(currentProcess.currentPhase) > 0) {
                        boolean flag = true;
                        Iterator<Process> blockedIterator2 = blockedQueue.iterator();
                        Process unblockedProcess;
                        while (flag) {
                            try {
                                unblockedProcess = blockedIterator2.next();
                                if (unblockedProcess.currentIoBlockTime <= currentTime) {
                                    if (unblockedProcess.currentIoBlockTime < currentTime) {
                                        readyQueue.add(unblockedProcess);
                                        readyQueue.add(currentProcess);
                                        blockedIterator2.remove();
                                        flag = false;
                                    } else {
                                        if (!readyQueue.contains(currentProcess)) {
                                            readyQueue.add(currentProcess);
                                            flag = false;
                                        }
                                    }
                                }
                            } catch (Exception e) {
                                readyQueue.add(currentProcess);
                                flag = false;
                            }
                        }
                    }
                }
            }
        }

        displayResults(completedProcesses , totalTurnaroundTime, totalWaitingTime, ganttChart.toString());
    }

    private static void displayReadyQueueWithGantt(Queue<Process> readyQueue, String ganttChart) {
        if (readyQueue.isEmpty()) {
            System.err.println("\033[31mLa cola de listos está vacía.\033[0m");
            return;
        }

        StringBuilder message = new StringBuilder("Procesos en la cola de listos:\n\n");
        message.append(String.format("%-10s%-15s\n", "\033[1;34mProceso\033[0m", "\033[1;34mTiempo Restante\033[0m"));

        Queue<Process> queueCopy = new LinkedList<>(readyQueue);
        for (Process process : queueCopy) {
            int remainingTime = process.currentPhase < process.times.size()
                    ? process.times.get(process.currentPhase)
                    : 0;

            System.out.printf("%-10s%-15d\n", "P" + process.id, remainingTime);
        }

        System.out.println("\n\033[1;33mDiagrama de Gantt:\033[0m");

        StringBuilder coloredGantt = new StringBuilder();
        for (char ch : ganttChart.toCharArray()) {
            if (ch == '#') {
                // Fase de CPU (usamos verde)
                coloredGantt.append("\033[32m#\033[0m");
            } else if (ch == '.') {
                // Fase de E/S (usamos rojo)
                coloredGantt.append("\033[31m.\033[0m");
            } else {
                // Resto de los caracteres (sin color)
                coloredGantt.append(ch);
            }
        }

        // Imprimimos el diagrama de Gantt coloreado
        System.out.println(coloredGantt.toString());
    }

    private static int calculateIOTime(List<Integer> times) {
        int totalIOTime = 0;
        for (int i = 1; i < times.size(); i += 2) {
            totalIOTime += times.get(i);
        }
        return totalIOTime;
    }

    private static void displayResults(List<Process> processes, int totalTurnaroundTime, int totalWaitingTime, String ganttChart) {
        StringBuilder results = new StringBuilder();
        results.append("Resultados de la simulación:\n\n");
        results.append(ganttChart).append("\n\n");

        // Imprimimos el encabezado con más espacio entre las columnas
        System.out.printf("%-20s%-30s%-30s\n", "\033[1;34mProceso\033[0m", "\033[1;34mTiempo de Vuelta\033[0m", "\033[1;34mTiempo de Espera\033[0m");

        // Imprimimos los resultados de cada proceso
        for (Process p : processes) {
            System.out.printf("%-20s%-30d%-30d\n", "P" + p.id, p.turnaroundTime, p.waitingTime);
        }

        // Imprimimos los promedios de tiempos con color
        System.out.println("\n\033[1;32mPromedio Tiempo de Vuelta: \033[0m" + (double) totalTurnaroundTime / processes.size());
        System.out.println("\033[1;32mPromedio Tiempo de Espera: \033[0m" + (double) totalWaitingTime / processes.size());
    }

    private static int getValidInput(String message, int min, int max) {
        Scanner scanner = new Scanner(System.in); // Usamos Scanner para leer desde la consola
        while (true) {
            try {
                System.out.print(message); // Imprime el mensaje en consola
                String input = scanner.nextLine();

                // Si la entrada es nula o vacía (por alguna razón) se cierra el programa
                if (input == null || input.isEmpty()) {
                    System.out.println("Programa terminado.");
                    System.exit(0);
                }

                int value = Integer.parseInt(input); // Intentamos convertir la entrada a un número

                // Comprobamos si el valor está dentro del rango permitido
                if (value >= min && value <= max) {
                    return value; // Si es válido, lo retornamos
                } else {
                    // Error por estar fuera de rango
                    System.err.println("\033[31mPor favor, ingrese un número dentro del rango [" + min + ", " + max + "].\033[0m");
                }
            } catch (NumberFormatException e) {
                // Error por formato inválido (no es un número)
                System.err.println("\033[31mPor favor, ingrese un número válido.\033[0m");
            }
        }
    }


}