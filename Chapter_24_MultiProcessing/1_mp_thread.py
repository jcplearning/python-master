from multiprocessing import Pool
import time
import logging


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    tasks = [1, 2, 3, 4, 5]

    for task in tasks:
        time.sleep(task)
        logging.info(f"Task {task} completed")

    with Pool(3) as pool:
        pool.map(time.sleep, tasks)
        logging.info("All tasks completed")





