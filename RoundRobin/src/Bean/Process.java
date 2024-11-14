package Bean;

import java.util.List;

public class Process {
    int id;
    int arrivalTime;
    List<Integer> times; // Contains CPU and I/O times
    int currentPhase;
    int waitingTime;
    int turnaroundTime;
    int totalIOTime; // Total I/O time
    int currentBlockTime;
    boolean firstExecution;

    Process(int id, int arrivalTime, List<Integer> times) {
        this.id = id;
        this.arrivalTime = arrivalTime;
        this.times = times;
        this.currentPhase = 0;
        this.waitingTime = 0;
        this.turnaroundTime = 0;
        this.totalIOTime = 0;
        this.firstExecution = true;
    }
}

