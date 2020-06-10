# jeb_fast_api 为后台项目

## dev
### 运行环境
- Python 3.7.5
### 程序依赖
- 生成`pip3 freeze -> requirements.txt`
- 安装`pip3 install -r requirements.txt` or `pip3 install -i https://mirrors.aliyun.com/pypi/simple/ -r requirements.txt`\
### dev run
`uvicorn app.main:app --reload --host=0.0.0.0 --port 8011`

## docker
### build
`docker build -f ./Dockerfile -t jeb_fast_api . --no-cache --rm`
### run
`docker run -d --name jeb_fast_api -p 8080:80 jeb_fast_api`
