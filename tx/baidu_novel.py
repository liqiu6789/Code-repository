import requests
from bs4 import BeautifulSoup

# 目标URL列表
urls = [
    "https://top.baidu.com/board?tab=novel",
    "https://top.baidu.com/board?tab=realtime",
    "https://top.baidu.com/board?tab=homepage",
    "https://top.baidu.com/board?tab=movie",
    "https://top.baidu.com/board?tab=teleplay",
    "https://top.baidu.com/board?tab=car",
    "https://top.baidu.com/board?tab=game"
]

# 抓取和解析数据的函数
def fetch_and_parse(url):
    try:
        # 发送HTTP GET请求
        response = requests.get(url)
        response.raise_for_status()  # 检查HTTP错误

        # 解析HTML内容
        soup = BeautifulSoup(response.text, 'html.parser')

        # 查找包含标题的 <a> 标签
        title_links = soup.find_all('a', class_='title_dIF3B')

        # 提取标题
        titles = []
        for link in title_links:
            title_div = link.find('div', class_='c-single-text-ellipsis')
            if title_div:
                title = title_div.text.strip()
                titles.append(title)

        return titles

    except requests.exceptions.RequestException as e:
        print(f"请求失败: {url}, 错误: {e}")
        return []
    except Exception as e:
        print(f"解析失败: {url}, 错误: {e}")
        return []

# 遍历URL列表并抓取数据
for url in urls:
    print(f"正在抓取: {url}")
    titles = fetch_and_parse(url)
    if titles:
        print(f"抓取到的标题:")
        for index, title in enumerate(titles, start=1):
            print(f"{index}. {title}")
    else:
        print("未抓取到数据")
    print("-" * 50)  # 分隔线