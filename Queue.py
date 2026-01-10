class Queue:
    def __init__(self):
        self.queue = []
    def add(self, num: int):
        self.queue.append(num)

    def remove(self):
        if self.queue:  # check if not empty
            return self.queue.pop(0)
        else:
            return None

    def get_queue(self):
        return self.queue


queue_var = Queue()
queue_var.add(1)
queue_var.add(3)
queue_var.remove()
print(queue_var.get_queue())
