#!/bin/env python3

from psutil import disk_partitions
from psutil import disk_usage
from psutil._common import bytes2human

def format_output(mountpoint, used_space, total_space):
    return " " + mountpoint + " " + used_space + "/" + total_space

partitions = disk_partitions()
ext4_mountpoints = []
results = []

for partition in partitions:
    if partition.fstype == 'ext4':
        ext4_mountpoints.append(partition.mountpoint)

for mountpoint in ext4_mountpoints:
    total_space = bytes2human(disk_usage(mountpoint).total)
    used_space = bytes2human(disk_usage(mountpoint).used)

    results.append(format_output(mountpoint, used_space, total_space))

print(" ".join(results))

