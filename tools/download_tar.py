#!/usr/bin/env python
# This script downloads a tar file from the UMich robotics dataset
# Reference: http://blog.ppkt.eu/2014/06/python-urllib-and-tarfile/

import os
import urllib.request

os.chdir('..') # go up to project root directory
owd = os.getcwd() # original working directory
data_dir = None

# Make sure that there is a 'data' directory
def ensure_data_dir_exists():
    global owd, data_dir
    p = owd
    p = os.path.join(p, 'data')
    if not os.path.exists(p):
        os.mkdir(p)
    data_dir = p

# Download the tar file and put it in the data directory
def download_tar(base_name, date):
    global data_dir
    os.chdir(data_dir)
    tmp = '%s/sensor_data/' % base_name
    fname = '%s_sen.tar.gz' % date
    url = tmp + fname
    urllib.request.urlretrieve(url, os.path.join(data_dir, fname))


if __name__ == '__main__':
    base_name = 'http://robots.engin.umich.edu/nclt'
    date = '2013-01-10'
    ensure_data_dir_exists()
    download_tar(base_name, date)
