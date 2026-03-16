import requests
from bs4 import BeautifulSoup

# Ссылка на твой Telegraph
url = 'https://telegra.ph/sposoby-priobreteniya-koda-03-09'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

title = 'Способы приобретения кода'
article = soup.find('article')

# Идеальная копия стилей Telegraph
html_content = f"""
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link rel="icon" type="image/x-icon" href="icon.ico">
    <style>
        /* Основной текст как в Telegraph */
        body {{
            font-family: Georgia, Cambria, "Times New Roman", serif;
            font-size: 18px;
            line-height: 1.58;
            color: rgba(0, 0, 0, 0.8);
            background: #fff;
            max-width: 732px;
            margin: 0 auto;
            padding: 20px 20px 40px;
        }}
        /* Заголовки (sans-serif) */
        h1, h2, h3, h4, address {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            color: #000;
            font-style: normal;
        }}
        h1 {{
            font-size: 32px;
            font-weight: 700;
            margin-bottom: 20px;
        }}
        /* Выравнивание QR-кода строго по центру */
        figure {{
            margin: 30px 0;
            padding: 0;
            display: flex;
            flex-direction: column;
            align-items: center; /* Центрируем содержимое */
            text-align: center;
        }}
        img {{
            max-width: 100%;
            height: auto;
            display: block;
        }}
        figcaption {{
            margin-top: 10px;
            color: #79828B;
            font-size: 15px;
        }}
        /* Ссылки и абзацы */
        a {{
            color: #1a0dab;
            text-decoration: none;
        }}
        a:hover {{
            text-decoration: underline;
        }}
        p {{
            margin-top: 0;
            margin-bottom: 1em;
        }}
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
