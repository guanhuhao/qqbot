from aiocache import cached

from .common import fetch_text


@cached(ttl=60) # 结果缓存 60 秒
async def get_current_weather_short(city: str) -> str:
    return (await fetch_text(f'https://wttr.in/{city}?format=1')).strip()

@cached(ttl=60)
async def get_current_weather_desc(city: str) -> str:
    _format = (
        '%l:\n'
        '+%c+%C:+%t\n'
        '+💦+湿度:+%h\n'
        '+💧+降水量:+%p\n'
        '+🍃+风力:+%w'
    )
    return await fetch_text(f'https://wttr.in/{city}?format={_format}')