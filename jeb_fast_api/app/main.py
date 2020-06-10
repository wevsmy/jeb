# @Version: V1.0
# @Author: wevsmy
# @License: Apache Licence
# @Contact: wevsmy@gmail.com
# @Site: https://blog.weii.ink
# @Software: PyCharm
# @File: main.py
# @Time: 2020/6/10 下午4:31
import time
from os.path import join

from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
from fastapi.responses import Response, HTMLResponse, RedirectResponse
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.staticfiles import StaticFiles

from app.apis.api import api_router
from app.config.log_config import GetLogger
from app.config.settings import PROJECT_NAME, PROJECT_DESCRIPTION, PROJECT_PATH, PROJECT_STATIC_PATH, DEBUG, DOMAIN
from app.core.shortUrl import GetOriginalUrl
from app.flask.main import flask_app

logger = GetLogger(__name__)  # 生成一个log实例

app = FastAPI(
    title=PROJECT_NAME,
    description=PROJECT_DESCRIPTION,
    version="0.0.0",
    debug=DEBUG,
    openapi_url="/openapi.json" if DEBUG else None,
    docs_url="/docs" if DEBUG else None,
    redoc_url="/redoc" if DEBUG else None,
)


@app.on_event("startup")
async def startup_event():
    logger.info("App startup")


# 允许跨域请求的域名列表(不一致的端口也会被视为不同的域名)
origins = ["*"]

# 跨域中间件 通配符匹配，允许域名和方法
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# 自定义中间件
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


# 根路由
# 默认跳转H5前端页面
@app.get("/")
async def read_root():
    return RedirectResponse(DOMAIN + '/h5#/', status_code=302)


# 返回图标
@app.get("/favicon.ico")
async def favicon():
    with open(join(PROJECT_STATIC_PATH, "img", "favicon.ico"), mode="rb") as f:
        content = f.read()
        return Response(content=content, status_code=200)


# H5前端页面路由
@app.get("/h5")
async def h5_index():
    with open(join(PROJECT_PATH, "app", "h5", "index.html"), mode="rb") as f:
        html_content = f.read()
        return HTMLResponse(content=html_content, status_code=200)


# ex http://host:port/static/xxxx  xxx对应的为static文件夹下的路径
app.mount("/static", StaticFiles(directory=PROJECT_STATIC_PATH), name="static")

# ex http://host:port/h5/static/xxxx  xxx对应的为app/h5/static文件夹下的路径,h5文件夹为前端页面文件
app.mount("/h5/static", StaticFiles(directory=join(PROJECT_PATH, "app", "h5", "static")), name="/h5/static")

# 引入flask路由
# 为微信公众号预留的
app.mount("/wx", WSGIMiddleware(flask_app))

# 引入API路由
app.include_router(api_router, prefix="/api", tags=["api"])


# 短链接302跳转
# 匹配不到默认跳转前端H5页面
@app.get("/{id}")
async def shortUrl(id: str):
    originalUrl = GetOriginalUrl(id)
    if originalUrl:
        return RedirectResponse(originalUrl, status_code=302)
    return RedirectResponse(DOMAIN + '/h5#/', status_code=302)


@app.on_event("shutdown")
def shutdown_event():
    logger.info("App shutdown")


if __name__ == '__main__':
    pass
