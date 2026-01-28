import requests
import json
import webbrowser

VERSION_URL = "https://gitee.com/your_repo/raw/master/version.json"

def check_update(current_version):
    try:
        # 获取远程版本信息
        response = requests.get(VERSION_URL, timeout=5)
        data = response.json()
        latest_version = data["version"]
        download_url = data["url"]

        # 比对版本号
        if latest_version != current_version:
            print(f"发现新版本 {latest_version}，当前版本 {current_version}")
            # 这里可以选择自动下载或提示用户
            webbrowser.open(download_url)  # 打开浏览器下载
        else:
            print("当前已是最新版本。")

    except Exception as e:
        print("检查更新失败：", e)
