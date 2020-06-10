import hashlib

from app.config.settings import DOMAIN, REDIS_SHORT_URL_DB
from app.db.base import RedisConn

# redis 存放短链接映射
shortUrlRedisConn = RedisConn(db=REDIS_SHORT_URL_DB)


def _md5(field):
    md5 = hashlib.md5()
    md5.update(field.encode(encoding='utf-8'))
    return md5.hexdigest()


# 根据长链接生成唯一hash key
def GetHashKey(long_url, number=3):
    code_map = (
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
        'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
        'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
        'y', 'z', '0', '1', '2', '3', '4', '5',
        '6', '7', '8', '9', 'A', 'B', 'C', 'D',
        'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
        'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
        'U', 'V', 'W', 'X', 'Y', 'Z'
    )
    hex = _md5(long_url)
    i = 0
    n = int(hex[i * 8:(i + 1) * 8], 16)
    v = []
    e = 0
    for j in range(0, number):
        x = 0x0000003D & n
        e |= ((0x00000002 & n) >> 1) << j
        v.insert(0, code_map[x])
        n = n >> 6
    e |= n << 5
    v.insert(0, code_map[e & 0x0000003D])
    return ''.join(v)


def GetShortUrl(originalUrl):
    hashKey = GetHashKey(originalUrl)
    shortUrlRedisConn.set(hashKey, originalUrl)
    shortUrl = "{}/{}".format(DOMAIN, hashKey)
    return shortUrl


def GetOriginalUrl(hashKey: str):
    bString = shortUrlRedisConn.get(hashKey)
    if bString:
        return bString.decode("utf-8")
    return ""


if __name__ == '__main__':
    print(GetHashKey('http://www.weii.ink'))
