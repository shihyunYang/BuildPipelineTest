#!/usr/bin/env python
import shutil

def greet():
    shutil.copy2('../Builds/BuildPlayer.apk', '/Users/yangsihyeon/Sites/build/BuildPlayer.apk')

if __name__ == "__main__":
    greet()