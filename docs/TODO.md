# TODOLISTS

- [x] 所有的配置全部放到`src/config/Application.yml`中，然后使用文件读取，把所有的配置信息读取后分为不同的类存放在`Configs.py`中调用
- [x] 添加数据库执行和提交的封装
- [ ] 爬虫能不能优化
- [x] 不采用Flask的`current_app`和`g`等设计，而是独立封装为类，保持向下兼容
- [x] 更改`requirements.txt`为`pyproject.toml`
- [x] 更改包的名字为`app`
- [ ] 删除没有用到的静态文件
- [ ] 日志系统
- [ ] 由`argparse`模块引入是否需要初始化数据库