quotes = [
    "Всё, к чему я прикасаюсь, всё, что меня окружает... всё это разрушается, калечится, гибнет. Разрушение — единственное, что у меня получается хорошо. Пусть будет так.",
    "пусть теперь все знают, крыс чревато злить, мор всё приближается, его не пережить",
    "Этой ночью Сергей Разумовский умер. теперь есть только Чумной Доктор",
    "Огонь все вылечит",
    "Нравственность и закон бессильны там, где правят деньги!"
]

# Создание HTML
html_content = f"""
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Цитаты Гражданина</title>
</head>
<body>
 <script>
        function getRandomQuote() {{
            var quotes = {quotes};
            var randomIndex = Math.floor(Math.random() * quotes.length);
            document.getElementById('quoteDisplay').innerText = quotes[randomIndex];
        }}
    </script>
    <h1>Цитаты Гражданина</h1>
    <p id="quoteDisplay">Нажмите на кнопку, чтобы увидеть случайную цитату.</p>
    <button onclick="getRandomQuote()">Показать цитату</button>
</body>
</html>
"""

# Запись в HTML-файл
with open("quotes.html", "w", encoding="utf-8") as file:
    file.write(html_content)