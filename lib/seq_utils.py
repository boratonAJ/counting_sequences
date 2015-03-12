#!/usr/bin/env python
import os
import sys



def count_seqs(input_file):
    count = 0
    for line in input_file:
        line = line.lstrip() # strip leading spaces, if any
        if line.startswith('>'):
            count += 1
    return count


