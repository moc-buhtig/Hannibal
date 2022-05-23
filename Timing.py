import time


class Stopwatch:
    def __init__(self, name):
        self.name = name
        self.startTime = -1
        self.running = False
        self.runs = 0
        self.totalTime = 0

    def start(self):
        if not self.running:
            self.startTime = time.time()
            self.running = True

    def stop(self):
        if self.running:
            stop_time = time.time()
            elapsed_time = (stop_time - self.startTime) * 1000.0
            print('Timer {:s} stopped in {:3f} ms'.format(self.name, elapsed_time))

            self.startTime = -1
            self.running = False
            self.runs += 1
            self.totalTime += elapsed_time

    def average_time(self):
        if self.runs == 0:
            return 0
        else:
            return self.totalTime / float(self.runs)

    def __str__(self):
        return 'Stopwatch {:s}: {:n} runs, Total time - {:3f} ms, Average time - {:3f} ms'.format(
            self.name, self.runs, self.totalTime, self.average_time()
        )
