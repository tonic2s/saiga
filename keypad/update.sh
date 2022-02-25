#!/bin/bash

sudo mount -L CIRCUITPY /mnt
sudo rsync --recursive --human-readable --progress --update --checksum -v ./driver/* /mnt
sudo umount /mnt
