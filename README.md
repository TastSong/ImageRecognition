ImageRecognition
====================

总述
--------------------

* 本程序是用来识别图片中的文字
* 主要使用腾讯的OCR AI接口实现的

环境
---------------------

* python3
* PyCharm 2017.1 x64
* Anaconda3

使用
---------------------

* 首先到[腾讯AI开放平台](https://ai.qq.com/)  开通相应的应用，得到APPID和KEY
* 将要识别的图片放入根目录下的img文件夹
* 根据识别的循序，将图片从`0.jpg` ~ `n.jpg`进行命名
* 识别的文字会根据识别的顺序，存放到根目录下的`date.txt`文件里
