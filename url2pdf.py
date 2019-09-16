import requests
import lxml
import configparser

import pdfkit

from bs4 import BeautifulSoup

class PdfDownloader:

    # 主要执行流程
    def main(self):
        self.read_config()
        urls = self.read_urls()
        for url in urls:
            print("downloading: ", url)
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
    @staticmethod
    def get_file_name(url):
        response = requests.get(url=url)
        html = response.text
        # print(html)
        soup = BeautifulSoup(html, 'lxml')
        title_raw = soup.title
        title = title_raw.get_text()
        title.replace('\t', '').replace('\n', ' ')
        print("file name: ", title)
        return title


if __name__ == "__main__":
    pdf = PdfDownloader()
    pdf.main()
    # pdf.read_config()
    # pdf.download_pdf("https://pnp.mathematik.uni-stuttgart.de/iadm/Weidl/analysis2/vorlesung-ana2/node4.html", "test.pdf")

