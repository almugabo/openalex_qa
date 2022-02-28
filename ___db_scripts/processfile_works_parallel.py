#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 18:18:25 2022

@author: mike
"""

import sys
from sqlalchemy import create_engine
import yaml
import time 
import os



import open_alex as oa

import glob

from multiprocessing import Pool


SNAPSHOT_DIR = '/media/mike/x_ssd/___DATA_STAGING/openalex/'

CSV_DIR = '/media/mike/SSD4T/__staging/openalex_v20220224/works'

jsonl_file_list = glob.glob(os.path.join(SNAPSHOT_DIR, 'data', 'works', '*', '*.gz')) # -- fo  testing[54:60]



def xfile_process(xfile):
    oa.process_file_work(jsonl_file_name = xfile, CSV_DIR = CSV_DIR )
    print('processing:', xfile.split('=')[1], '----', time.asctime(), flush=True)


def main():
    #arguments for the parallelism 
    num_processors = 20 #Create a pool of processors

    p=Pool(processes = num_processors)#get them to work in parallel
    #p.map(func = xfile_process, iterable = jsonl_file_list_1)
    p.map(func = xfile_process, iterable = jsonl_file_list)    
    
if __name__ == '__main__':
    print(time.asctime(), 'START')    
    #pass
    print('processing files: ', len(jsonl_file_list))    
    main()
    print(time.asctime(), 'END')
    
