#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
from ctypes import ArgumentError
import os
import sys
import platform


def run_command(command: str):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)

    for stdout_line in iter(process.stdout.readline, ""):    
        if not stdout_line:
            break;

        print(stdout_line.decode('utf-8').strip())
    
    process.stdout.close()
    return process.wait()
    
def main():
    unity_path = '"C:/Program Files/Unity/Hub/Editor/2021.3.6f1/Editor/Unity.exe" -quit -accept-apiupdate -nographics -batchmode -logFile "BuildAndroid.log" -buildTarget Android -projectPath F:/WorkSpace/buildPipelineTest -executeMethod BuildPlayer.BuildAndroid'

/Applications/Unity/Hub/Editor/2021.3.6f1

    exit(run_command(unity_path))
    
    
    
if __name__ == "__main__":
    main()