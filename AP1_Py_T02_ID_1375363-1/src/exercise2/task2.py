import asyncio
import aiohttp
import aiofiles
import os
from urllib.parse import urlparse


async def download_image(session, url, save_path, results):
    try:
        parsed = urlparse(url)
        if not parsed.scheme or not parsed.netloc:
            raise ValueError("Некорректный URL")
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
        
        async with session.get(url, timeout=10, headers=headers, ssl=False) as response:
            if response.status != 200:
                raise Exception(f"HTTP ошибка: {response.status}")

            data = await response.read()

            if not data or len(data) == 0:
                raise Exception("Получены пустые данные")
            
            filename = os.path.basename(parsed.path)
            if not filename:
                filename = "image.jpg"
            
            filepath = os.path.join(save_path, filename)

            if os.path.exists(filepath):
                os.remove(filepath)

            async with aiofiles.open(filepath, 'wb') as f:
                await f.write(data)
            
            results[url] = 'Успех'
            
    except Exception as e:
        results[url] = 'Ошибка'


async def input_loop(save_path, results, urls_order):
    
    connector = aiohttp.TCPConnector(ssl=False)
    async with aiohttp.ClientSession(connector=connector) as session:
        tasks = []
        
        while True:
            url = await asyncio.get_event_loop().run_in_executor(None, input)
            
            if not url.strip():
                break
            
            url = url.strip()
            urls_order.append(url)
            results[url] = 'В процессе'
            
            task = asyncio.create_task(
                download_image(session, url, save_path, results)
            )
            tasks.append(task)
        
        if tasks:
            await asyncio.gather(*tasks)


def validate_path(path):
    try:
        os.makedirs(path, exist_ok=True)
        
        test_file = os.path.join(path, '.test_write')
        with open(test_file, 'w') as f:
            f.write('test')
        os.remove(test_file)
        
        return True
    except (OSError, PermissionError):
        return False


def print_results(urls_order, results):
    
    if not urls_order:
        print("Нет данных для отображения.")
        return
    
    max_url_len = max((len(url) for url in urls_order), default=10)
    max_url_len = max(max_url_len, 10)
    
    print(f"+{'-' * (max_url_len + 2)}+{'-' * 8}+")
    print(f"| {'Ссылка':<{max_url_len}} | {'Статус':<6} |")
    print(f"+{'-' * (max_url_len + 2)}+{'-' * 8}+")
    
    for url in urls_order:
        status = results.get(url, 'Ошибка')
        print(f"| {url:<{max_url_len}} | {status:<6} |")
    
    print(f"+{'-' * (max_url_len + 2)}+{'-' * 8}+")


async def main():
    while True:
        save_path = input("Введите путь для сохранения изображений: ").strip()
        
        if validate_path(save_path):
            break
        else:
            print("Некорректный путь или нет доступа.")
    
    results = {}
    urls_order = []
    await input_loop(save_path, results, urls_order)
    
    print_results(urls_order, results)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nПрограмма прервана пользователем.")