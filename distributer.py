#!/usr/bin/env python
import shutil
import datetime as dt
import os



def webpageCreate(strname):
    #if os.path.isfile('/Users/yangsihyeon/Sites/index.html')
    os.remove('/Users/yangsihyeon/Sites/index.html')
    
    file = open('/Users/yangsihyeon/Sites/index.html','w')
    
    webpage = """<html>
            <body>
                <h1>Android</h1>
                <p><a href="build/{0}">install {0} dev-aos</a></p>
            </body>
        </html>
        """
    webpage.format(strname)
    
    
    file.write(webpage)
    file.close();


def greet():
    x = dt.datetime.now()
    test = '/Users/yangsihyeon/Sites/build/BuildPlayer{0}_{1}_{2}_{3}_{4}_{5}_[6].apk'
    test.format(x.year, x.month, x.day, x.hour, x.minute, x.second)
    shutil.copy2('/Users/yangsihyeon/Desktop/BuildPipelineTest/Builds/BuildPlayer.apk', test)
    
    filename = 'BuildPlayer{0}_{1}_{2}_{3}_{4}_{5}_[6].apk'
    filename.format(x.year, x.month, x.day, x.hour, x.minute, x.second)
    webpageCreate(filename)
    

if __name__ == "__main__":
    greet()
