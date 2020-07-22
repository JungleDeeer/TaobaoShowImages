import time
import datetime
import os
import aiohttp
import asyncio
import aiofiles
import imghdr


amount = 500
loopAmount = 1000
dirname ='MassiveSexyImages'
url = 'https://api.66mz8.com/api/rand.tbimg.php?format=images'
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    'Connection': 'keep-alive'
}

if not os.path.exists(dirname):
    os.mkdir(dirname)

async def content(session,url):
    for i in range(loopAmount):
        async with session.get(url,headers = headers) as response:
            img = await response.read()
            type = imghdr.what(None, img)
            if (type == None):
                continue
            async with aiofiles.open(dirname + str("/") + str(datetime.datetime.now().strftime('%Y%m%d%H%M%S')) + str(i) + '.' + type, mode = 'wb') as f:
                await f.write(img)
                await f.close()


async def download(url):
    async with aiohttp.ClientSession() as session:
        try:
            await content(session, url)
        except Exception as err:
            print(err)


startTime = time.time()
loop = asyncio.get_event_loop()
tasks = [asyncio.ensure_future(download(url))for i in range(amount)]
tasks = asyncio.gather(*tasks)
loop.run_until_complete(tasks)

finishTime = time.time()
print('cost time: %s'%(startTime - finishTime))
