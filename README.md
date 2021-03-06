## URL TO PDF
两个功能：
* 下载网页文件并存为pdf：url2pdf.py
* 将多个pdf文件合并成一个：mergePdf.py

### How to use
1. 配置环境
    * 开发环境为 Python 3.6.8
    * 安装 wkhtmltox，需要到网站下载对应版本，并放在自己知道的位置
    * pip 安装其他库
    ```
    pip install pdfkit
    pip install wkhtmltopdf
    ...
    ```
    **Tips：只用合并pdf功能，则只需要pip安装PyPDF2，且不用管配置文件**

2. 文件同路径下创建两个文件夹："pdfs", "merge"

3. 修改配置文件
    将各种文件路径填入 config.ini 中，详见下文说明
    另外需要预先准备一个文本文件，存放需要下载的 url，每行一个链接

4. 运行程序  
    * python url2pdf.py——下载网页文件
    * python mergePdf.py——将pdfs中的文件合并成一个pdf文件，并放在merge路径下

### 配置文件说明
分为 2 个 section
* download：下载 pdf 相关配置
  * wktool_path：wkhtmltox 的运行文件路径，一般是 `xxx\wkhtmltox\bin\wkhtmltopdf.exe`
  * url_file：指定的文本文件，会从里面读取需要下载的网页
  * out_path：pdf 输出的文件夹路径，可以使用相对路径，一定要有 `\` 结尾
* merge：将多个 pdf 文件合并的相关配置
  * input_path：存放多个 pdf 的文件夹的路径
  * output_path：输出 pdf 的路径

### 环境
关于这些包，可以直接搜索，中英文资料应该都很多，这里只是简单介绍

1. wkhtmltox
一个第三方库，是 pdf 操作的底层依赖，平台相关，下面这个网址找到合适的版本，并放到合适的位置
[官网](https://wkhtmltopdf.org/downloads.html)
[博文](https://www.cnblogs.com/xiaowenshu/p/9916719.html)

2. pdfkit
wkhtmltox 的封装包

3. configparser
读取配置文件的包
[博文](https://www.cnblogs.com/lhly/p/8066898.html)

4. PyPDF2
合并Pdf文件使用的包[博文](https://www.jianshu.com/p/82485e3e46e1)
