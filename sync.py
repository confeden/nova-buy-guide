import requests
from bs4 import BeautifulSoup

# Ссылка на твой Telegraph
url = 'https://telegra.ph/sposoby-priobreteniya-koda-03-09'

# Скачиваем страницу
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Вытаскиваем заголовок и само тело статьи
title_tag = soup.find('h1')
title = title_tag.text if title_tag else 'Способы приобретения Кода'
article = soup.find('article')

# Обновленный дизайн, копирующий стили Telegraph
html_content = f"""
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=PT+Serif:ital,wght@0,400;0,700;1,400;1,700&display=swap" rel="stylesheet">
    <style>
        body {{
            font-family: 'PT Serif', Georgia, serif;
            font-size: 18px;
            line-height: 1.58;
            color: #333;
            background: #fff;
            max-width: 732px;
            margin: 0 auto;
            padding: 20px;
        }}
        img {{ 
            max-width: 100%; 
            height: auto; 
            display: block; 
            margin: 0 auto; /* Центрирует картинку */
        }}
        figure {{ 
            margin: 30px 0; 
            text-align: center; 
        }}
        figcaption {{ 
            font-size: 15px; 
            color: #79828B; 
            margin-top: 10px; 
        }}
        a {{ color: #1a0dab; text-decoration: none; }}
        a:hover {{ text-decoration: underline; }}
        h1, h2, h3, h4 {{ 
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            color: #000;
        }}
        h1 {{ font-size: 32px; font-weight: 700; margin-bottom: 20px; }}
    </style>
</head>
<body>
    {article}
</body>
</html>
"""

# Сохраняем результат
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
