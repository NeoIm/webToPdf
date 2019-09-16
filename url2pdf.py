# import requests
import configparser
import re
import time

import pdfkit

# from bs4 import BeautifulSoup

class PdfDownloader:

    # 主要执行流程
    def main(self):
        self.read_config()
        urls = self.read_urls()
        count = 0
        for url in urls:
            count += 1
            print(count)
            print("downloading: ", url)
            # file_name = self.get_website_title(url)
            file_name = self.get_file_name(url)
            self.download_pdf(url, file_name)


    """
    读取配置文件
    复用的变量抽取到了配置文件中，并读取存在成员变量中，方便修改和使用
    """
    def read_config(self):
        conf = configparser.ConfigParser()
        conf.read("config.ini")
        print("read config.ini")
        self.url_file = conf.get("download", "url_file")
        print("url_file: ", self.url_file)
        self.out_path = conf.get("download", "out_path")
        print("out_path: ", self.out_path)
        self.wktool_path = conf.get("download", "wktool_path")
        print("wktool_path: ", self.wktool_path)

    def read_urls(self):
        urls = []
        with open(self.url_file) as f:
            for line in f.readlines():
                # print(line.strip())
                urls.append(line)
        return urls

    """
    下载网页并保存为 pdf
    """
    def download_pdf(self, url, file_name):
        # 指定 wkhtmltox 的路径
        config = pdfkit.configuration(wkhtmltopdf=self.wktool_path)
        # from_url这个函数是从url里面获取内容
        # 3个参数，第一个是url，第二个是文件名，第三个就是khtmltopdf的路径
        pdfkit.from_url(url, self.out_path+file_name+'.pdf', configuration=config)

    """
    获取网页标题
    因为是一个单独功能的函数，没有用到类的成员变量，所以定义成了静态方法
    """
    # @staticmethod
    # def get_website_title(url):
    #     headers = {
    #         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    #                       ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
    #     }
    #     response = requests.get(url=url, headers=headers)
    #     html = response.text
    #     # print(html)
    #     soup = BeautifulSoup(html, 'lxml')
    #     title_raw = soup.title
    #     # print(title_raw)
    #     title = title_raw.get_text()
    #     title.replace('\r', '').replace('\n', ' ')
    #     print("file name: ", title)
    #     return title

    """
    获取网页标题不稳定，故截取 url 的部分作为文件名
    """
    @staticmethod
    def get_file_name(url):
        pattern = re.compile("\w+.html$")
        name = pattern.search(url)
        if name is None:
            name = time.time()
        else:
            name = name.group()[:-5]
        return name


if __name__ == "__main__":
    pdf = PdfDownloader()
    # pdf.main()
    r = pdf.get_file_name("https://pnp.mathematik.uni-stuttgart.de/iadm/Weidl/analysis2/vorlesung-ana2/node4.html")
    print(r)
