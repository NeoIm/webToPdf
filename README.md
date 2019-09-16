## URL TO PDF
### How to use
1. 配置环境
    * 开发环境为 Python 3.6.8
    * 安装 wkhtmltox，需要到网站下载对应版本，并放在自己知道的位置
    * pip 安装其他库
```
pip install pdfkit
pip install wkhtmltopdf
pip install beautifulsoup4
```

2. 修改配置文件
    将各种文件路径填入 config.ini 中，详见下文说明
    另外需要预先准备一个文本文件，存放需要下载的 url，每行一个链接

3. 运行程序
    python url2pdf.py

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

3. requests
进行网络访问的包，常用于爬虫
get 方法，获取指定 URL 的 html 文本

3. BeautifulSoup
用于解析 html 的包，很强大，可以提取 html 文本中的指定内容
本项目用于获取指定网页的标题

4. lxml
搭配 BeautifulSoup 使用的 xml 解析

5. configparser
读取配置文件的 build-in 包
[博文](https://www.cnblogs.com/lhly/p/8066898.html)

