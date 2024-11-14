import java.util.List;

public class Process {
    int id;
    int arrivalTime;
    List<Integer> times; // Contiene tiempos de CPU y E/S
    int currentPhase;
    int waitingTime;
    int turnaroundTime;
    int totalIoTime; // Tiempo total de E/S
    int currentIoBlockTime;
    boolean firstExecution;

    Process(int id, int arrivalTime, List<Integer> times) {
        this.id = id;
        this.arrivalTime = arrivalTime;
        this.times = times;
        this.currentPhase = 0;
        this.waitingTime = 0;
        this.turnaroundTime = 0;
        this.totalIoTime = 0;
        this.firstExecution = true;
    }
}