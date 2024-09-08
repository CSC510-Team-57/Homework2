"""
This component contains a randomizer helper function for the main hw2 file which randomly sorts
a given array for testing
"""

import subprocess

def random_array(arr):
    """ Shuffles an array randomly using its built in process """
    shuffled_num = None
    for i in enumerate(arr):
        shuffled_num = subprocess.run(
            ["shuf", "-i1-20", "-n1"], capture_output=True, check=False)
        i[1] = int(shuffled_num.stdout)
    return arr
    