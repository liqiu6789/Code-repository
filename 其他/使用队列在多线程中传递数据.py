import threading
import queue
import time

# 创建队列
data_queue = queue.Queue()

# 生产者线程函数
def producer(queue):
    for i in range(4):
        item = f"Item {i}"
        queue.put(item)
        print(f"Produced {item}")
        time.sleep(1)  # 模拟生产数据的延迟
    queue.put(None)  # 生产完毕的标志

# 消费者线程函数
def consumer(queue):
    while True:
        item = queue.get()
        if item is None:
            break  # 结束循环的条件
        print(f"Consumed {item}")
        time.sleep(2)  # 模拟处理数据的延迟

# 创建生产者和消费者线程
producer_thread = threading.Thread(target=producer, args=(data_queue,))
consumer_thread = threading.Thread(target=consumer, args=(data_queue,))

# 启动线程
producer_thread.start()
consumer_thread.start()

# 等待线程完成
producer_thread.join()
consumer_thread.join()

print("All tasks are completed.")
