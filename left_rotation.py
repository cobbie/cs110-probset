import copy
class Queue():
    
    top = None
    last = None
    
    def __init__(self, arr):
        self.arr = arr
        self.top = self.arr[0]
        self.last = self.arr[len(self.arr)-1]
        
    def __str__(self):
        return str(self.arr)
        
    def enqueue(self, num):
        self.arr.append(num)
        self.last = num
        
    def special_dequeue(self):
        if(len(self.arr) >= 1):
            temp = copy.copy(self.top)
            del self.arr[0]
            self.top = self.arr[0]
            return temp

        
    def peek(self):
        if len(self.arr) >= 1:
             print('Current last item in queue: ' + str(self.last))
        else:
            print("No items in queue")
    
    def count(self):
        if len(self.arr) >= 1:
             print('Total values currently in queue: ' + str(len(self.arr)))
        else:
             print("No items in queue")
                
    def clear(self):
        del self.arr[:]
        print(f"Queue cleared\n{self.arr}")

if __name__ == '__main__':
    in_1 = input().split()
    in_2 = [int(i) for i in input().split()]
    arr = []

    for i in range(int(in_1[0])):
        arr.append(in_2[i])
    prob_queue =  Queue(arr)

    for i in range(0, int(in_1[1])):
        prob_queue.enqueue(prob_queue.special_dequeue())
    print(prob_queue)