import os

import random


def get_gpu_memory():
    lines = os.popen('nvidia-smi -q -d Memory |grep -A5 GPU|grep Free').readlines()

    memory_available = [int(x.split()[2]) for x in lines]
    gpus = {index: mb for index, mb in enumerate(memory_available)}
    return gpus


def get_random_with_gpu_with_gb_free(gb):
    gpus = get_gpu_memory()
    filtered_keys = [key for key, value in gpus.items() if value // 1000 > gb]
    if filtered_keys:
        return random.choice(filtered_keys)
    else:
        return None