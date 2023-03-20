#!/usr/bin/env python
import shutil

def greet():
    shutil.copy2('/Users/yangsihyeon/Desktop/BuildPipelineTest/Builds/BuildPlayer.apk', '/Users/yangsihyeon/Sites/build/BuildPlayer.apk')

if __name__ == "__main__":
    greet()
