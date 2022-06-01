
import sys
input = sys.stdin.readline
n = int(input())
heap = [0]

def addNode(data):
    heap.append(data)
    upHeapify()


def upHeapify():
    lastIndex = len(heap) - 1
    index = lastIndex
    parent = (lastIndex // 2)
    while parent >= 1:
        if heap[index] <= heap[parent]:
            heap[parent], heap[index] = heap[index], heap[parent]
            if index == 1:
                parent, index = 0, parent
            else:
                parent, index = (index // 2), parent
        else:
            return


def downHeapify(index):
    size = len(heap)-1
    left = index * 2
    while left <= size:
        right = left+1
        if right <= size:
            if heap[left] > heap[right]:
                left = right
        if heap[left] > heap[index]:
            return
        heap[index], heap[left] = heap[left], heap[index]
        index = left
        left = index * 2


def pop():
    root = heap[1] 
    heap[1] = heap[len(heap)-1]
    downHeapify(1)
    heap.pop(len(heap)-1)
    return root


for _ in range(n):
    x = int(input())
    if x == 0:
        if len(heap) == 1:
            print(0)
        else:
            print(pop())
    else:
        addNode(x)
