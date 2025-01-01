# ZJU-BS-SYSTEM-PROJECT: Budget Bee

浙江大学2024秋冬B/S体系软件设计项目：商品比价网站

## User

首先构建环境，然后运行主程序

```Shell
pip install . [--no-deps] # 下载依赖包
python main.py            # 运行主程序
```

## Structure

```Shell
.
├── README.md                         # 自述文档
├── clean.sh                          # 清除构建产物脚本
├── docs                              # 文档
│   ├── Assignment.pdf                # 项目要求
│   ├── CHANGELOG.md                  # 变更日志
│   ├── Design.md                     # 设计报告
│   ├── Design.pdf
│   ├── Develop.md                    # 开发报告与测试报告
│   ├── Develop.pdf
│   ├── TODO.md                       # 待办事项
│   └── assets
│       └── ...
├── pyproject.toml                    # 项目依赖
└── src                               # 源代码
    ├── app                           # 应用包
    │   ├── App.py                    # 顶层应用类
    │   ├── Configs.py                # 配置文件读取类
    │   ├── __init__.py
    │   ├── database                  # 数据库模块
    │   │   ├── DatabaseConnector.py
    │   │   ├── DatabaseInitializer.py
    │   │   └── __init__.py
    │   ├── models                    # 数据模型
    │   │   ├── Price.py
    │   │   ├── Product.py
    │   │   ├── Subscription.py
    │   │   ├── User.py
    │   │   └── __init__.py
    │   ├── services                  # 爬虫服务模块
    │   │   ├── Dangdang.py
    │   │   ├── Spider.py
    │   │   ├── Suning.py
    │   │   └── __init__.py
    │   ├── static                    # 前端样式
    │   │   ├── css
    │   │   │   └── ...
    │   │   ├── img
    │   │   │   └── ...
    │   │   └── js
    │   │       └── ...
    │   ├── templates                  # 页面模板
    │   │   ├── authentication
    │   │   │   ├── login.html
    │   │   │   └── register.html
    │   │   ├── base.html
    │   │   ├── home
    │   │   │   ├── details.html
    │   │   │   ├── home.html
    │   │   │   └── search.html
    │   │   └── index.html
    │   ├── utils                      # 项目工具
    │   │   ├── EmailManager.py
    │   │   ├── Platforms.py
    │   │   ├── WebDriver.py
    │   │   └── __init__.py
    │   └── views                      # 视图模块
    │       ├── __init__.py
    │       ├── authentication.py
    │       ├── home.py
    │       └── index.py
    ├── configs                        # 配置信息
    │   ├── Application.yml
    │   └── DBInitializer.sql
    ├── main.py                        # 主程序
    ├── resources                      # 第三方资源
    │   ├── LICENSE.chromedriver
    │   ├── THIRD_PARTY_NOTICES.chromedriver
    │   └── chromedriver
    └── tests                          # 测试文件夹
        ├── DatabaseTests.py
        └── EmailTests.py
```
