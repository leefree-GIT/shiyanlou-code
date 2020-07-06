import requests

def download(url):
    req = requests.get(url)
    filename = url.split('/')[-1]
    with open(filename,'w') as fobj:
        fobj.write(req.content.decode('utf-8'))
    print("Download over.")


# 只要在当前模块名为__mian__时才会执行if块内的语句
# 作为模块导入其他文件时，则不执行if块内的语句
if __name__ == '__main__':
    url = input('Enter a URL:')
    download(url)
