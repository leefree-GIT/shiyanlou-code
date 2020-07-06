import requests

def download(url):
    '''
    从指定的URL中下载文件并存储到当前目录
    url:要下载页面内容的网址
    '''
    # 检查URL是否存在
    try:
        req = requests.get(url)
    except requests.exceptions.MissingSchema:
        print('Invalid URL "{}"'.format(url))
        return
    # 检查是否成功访问了该网站
    if req.status_code == 403:
        print('You do not have the authority to access this page.')
        return
    filename = url.split('/')[-1]
    with open(filename,'w') as fobj:
        fobj.write(req.content.decode('utf-8'))
    print("Download over.")


# 只要在当前模块名为__mian__时才会执行if块内的语句
# 作为模块导入其他文件时，则不执行if块内的语句
if __name__ == '__main__':
    url = input('Enter a URL:')
    download(url)
