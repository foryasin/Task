from rq import Queue
from worker import conn
import utils

q = Queue(connection=conn)


if __name__ == "__main__":
    q.enqueue(utils.count_total)
    q.enqueue(utils.count_each_word, "security")

