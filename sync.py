import requests
from bs4 import BeautifulSoup

# Ссылка на твой Telegraph
url = 'https://telegra.ph/sposoby-priobreteniya-koda-03-09'

# Скачиваем страницу (сервера GitHub сделают это без проблем)
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Вытаскиваем заголовок и само тело статьи
title_tag = soup.find('h1')
title = title_tag.text if title_tag else 'Способы приобретения Nova'
article = soup.find('article')

# Базовый минималистичный дизайн для зеркала
html_content = f"""
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            line-height: 1.6; color: #333; background: #fff; max-width: 800px; margin: 0 auto; padding: 20px;
        }}
        img {{ max-width: 100%; height: auto; border-radius: 8px; margin: 15px 0; }}
        a {{ color: #0066cc; text-decoration: none; }}
        a:hover {{ text-decoration: underline; }}
        h1 {{ color: #000; }}
        figure {{ margin: 0; padding: 0; }}
        figcaption {{ font-size: 0.9em; color: #666; text-align: center; }}
    </style>
</head>
<body>
    {article}
</body>
</html>
"""

# Сохраняем результат в index.html
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
