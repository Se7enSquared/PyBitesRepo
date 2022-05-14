from collections import deque


def my_queue(n=5):
    return deque(maxlen=n)


if __name__ == '__main__':
    mq = my_queue()
    for i in range(10):
        mq.append(i)
        print((i, list(mq)))
