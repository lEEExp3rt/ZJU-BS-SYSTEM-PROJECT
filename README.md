# ZJU-BS-SYSTEM-PROJECT: Budget Bee

浙江大学2024秋冬B/S体系软件设计项目：商品比价网站

## Structure

```Shell
.
├── CHANGELOG.md
├── README.md
├── TODO.md
├── clean.sh
├── docs
│   ├── Assignment.pdf
│   └── Design.md
└── src
    ├── backend
    │   ├── App.py
    │   ├── Configs.py
    │   ├── __init__.py
    │   ├── database
    │   │   ├── DatabaseConnector.py
    │   │   ├── DatabaseInitializer.py
    │   │   └── __init__.py
    │   ├── models
    │   │   ├── Price.py
    │   │   ├── Product.py
    │   │   ├── Subscription.py
    │   │   ├── User.py
    │   │   └── __init__.py
    │   ├── services
    │   │   ├── Dangdang.py
    │   │   ├── Spider.py
    │   │   ├── Suning.py
    │   │   └── __init__.py
    │   ├── static
    │   │   ├── css
    │   │   │   ├── bootstrap-grid.css
    │   │   │   ├── bootstrap-grid.css.map
    │   │   │   ├── bootstrap-grid.min.css
    │   │   │   ├── bootstrap-grid.min.css.map
    │   │   │   ├── bootstrap-grid.rtl.css
    │   │   │   ├── bootstrap-grid.rtl.css.map
    │   │   │   ├── bootstrap-grid.rtl.min.css
    │   │   │   ├── bootstrap-grid.rtl.min.css.map
    │   │   │   ├── bootstrap-reboot.css
    │   │   │   ├── bootstrap-reboot.css.map
    │   │   │   ├── bootstrap-reboot.min.css
    │   │   │   ├── bootstrap-reboot.min.css.map
    │   │   │   ├── bootstrap-reboot.rtl.css
    │   │   │   ├── bootstrap-reboot.rtl.css.map
    │   │   │   ├── bootstrap-reboot.rtl.min.css
    │   │   │   ├── bootstrap-reboot.rtl.min.css.map
    │   │   │   ├── bootstrap-utilities.css
    │   │   │   ├── bootstrap-utilities.css.map
    │   │   │   ├── bootstrap-utilities.min.css
    │   │   │   ├── bootstrap-utilities.min.css.map
    │   │   │   ├── bootstrap-utilities.rtl.css
    │   │   │   ├── bootstrap-utilities.rtl.css.map
    │   │   │   ├── bootstrap-utilities.rtl.min.css
    │   │   │   ├── bootstrap-utilities.rtl.min.css.map
    │   │   │   ├── bootstrap.css
    │   │   │   ├── bootstrap.css.map
    │   │   │   ├── bootstrap.min.css
    │   │   │   ├── bootstrap.min.css.map
    │   │   │   ├── bootstrap.rtl.css
    │   │   │   ├── bootstrap.rtl.css.map
    │   │   │   ├── bootstrap.rtl.min.css
    │   │   │   ├── bootstrap.rtl.min.css.map
    │   │   │   └── style.css
    │   │   ├── img
    │   │   │   └── logo.svg
    │   │   └── js
    │   │       ├── bootstrap.bundle.js
    │   │       ├── bootstrap.bundle.js.map
    │   │       ├── bootstrap.bundle.min.js
    │   │       ├── bootstrap.bundle.min.js.map
    │   │       ├── bootstrap.esm.js
    │   │       ├── bootstrap.esm.js.map
    │   │       ├── bootstrap.esm.min.js
    │   │       ├── bootstrap.esm.min.js.map
    │   │       ├── bootstrap.js
    │   │       ├── bootstrap.js.map
    │   │       ├── bootstrap.min.js
    │   │       └── bootstrap.min.js.map
    │   ├── templates
    │   │   ├── authentication
    │   │   │   ├── login.html
    │   │   │   └── register.html
    │   │   ├── base.html
    │   │   ├── home
    │   │   │   ├── home.html
    │   │   │   └── search.html
    │   │   └── index.html
    │   ├── utils
    │   │   ├── EmailManager.py
    │   │   ├── Platforms.py
    │   │   ├── WebDriver.py
    │   │   └── __init__.py
    │   └── views
    │       ├── __init__.py
    │       ├── authentication.py
    │       ├── home.py
    │       └── index.py
    ├── configs
    │   ├── Application.yml
    │   └── DBInitializer.sql
    ├── main.py
    ├── pyproject.toml
    ├── resources
    │   ├── LICENSE.chromedriver
    │   ├── THIRD_PARTY_NOTICES.chromedriver
    │   └── chromedriver
    └── tests
        ├── DatabaseTests.py
        └── EmailTests.py
```
