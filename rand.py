"""
rand.py description
"""

import subprocess


def random_array(arr):
    """ Shuffles an array randomly using its built in process """
    shuffled_num = None
    for i, value in enumerate(arr):
        shuffled_num = subprocess.run(
            ["shuf", "-i1-20", "-n1"], capture_output=True, check=False)
        value = int(shuffled_num.stdout)
    return arr

