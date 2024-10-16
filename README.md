# WeChatMomentTextUnfold
自动帮你把粘贴的文本逐字录入微信朋友圈，解决朋友圈粘贴的文本被折叠的问题

## 使用方法

0. 将代码克隆到本地

1. 安装Python环境，Python 3.8 以上版本

2. 安装依赖库：
```sh
pip install pyautogui
pip install pyperclip
```

**注意**

* 在使用之前，你需要函数 open_wechat_moments 中的代码来定位微信打开朋友圈录入界面的位置，一共两个位置

```python
    time.sleep(5)
    print("current position1 ",pyautogui.position())
```
然后替换代码中的两个坐标。


3. 将代码中的录入文本替换为你要录入的文本

4. 运行main.py文件

```sh
python main.py
```

## 联系我

个人微信: somenzz-enjoy