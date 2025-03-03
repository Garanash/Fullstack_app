male_names = [
    "Александр",
    "Дмитрий",
    "Иван",
    "Сергей",
    "Андрей",
    "Михаил",
    "Николай",
    "Алексей",
    "Владимир",
    "Евгений",
    "Павел",
    "Артем",
    "Виктор",
    "Константин",
    "Роман",
    "Олег",
    "Юрий",
    "Григорий",
    "Тимофей",
    "Василий"
]
female_names = [
    "Анна",
    "Мария",
    "Елена",
    "Ольга",
    "Татьяна",
    "Наталья",
    "Екатерина",
    "Ирина",
    "Светлана",
    "Виктория",
    "Александра",
    "Дарья",
    "Юлия",
    "Ксения",
    "Анастасия",
    "Людмила",
    "Валентина",
    "Маргарита",
    "Евгения",
    "Полина"
]
descriptions = [
    "творческий и вдохновляющий человек, всегда готовый к новым идеям",
    "внимательный и заботливый, всегда поддерживает окружающих",
    "целеустремленный и трудолюбивый, достигает поставленных целей",
    "любознательный и открытый к новым знаниям, постоянно развивается",
    "добрый и отзывчивый, всегда готов помочь другим",
    "спокойный и уравновешенный, умеет находить решения в сложных ситуациях",
    "энергичный и активный, заряжает окружающих своим энтузиазмом",
    "надежный и ответственный, на такого человека всегда можно положиться",
    "оптимистичный и жизнерадостный, смотрит на мир с улыбкой",
    "тактичный и дипломатичный, умеет находить общий язык с любым человеком",
    "креативный и нестандартно мыслящий, предлагает уникальные решения",
    "скромный и искренний, ценит простые радости жизни",
    "амбициозный и уверенный в себе, стремится к большим высотам",
    "чуткий и понимающий, умеет слушать и поддерживать",
    "организованный и дисциплинированный, всегда следует плану",
    "романтичный и мечтательный, видит красоту в мелочах",
    "практичный и рациональный, принимает взвешенные решения",
    "общительный и дружелюбный, легко находит новых друзей",
    "мудрый и рассудительный, дает ценные советы",
    "смелый и решительный, не боится трудностей"
]
svg_links = [
    "https://upload.wikimedia.org/wikipedia/commons/0/02/SVG_logo.svg",  # Логотип SVG
    "https://simpleicons.org/icons/github.svg",  # Иконка GitHub
    "https://simpleicons.org/icons/apple.svg",  # Иконка Apple
    "https://simpleicons.org/icons/google.svg",  # Иконка Google
    "https://simpleicons.org/icons/instagram.svg",  # Иконка Instagram
    "https://simpleicons.org/icons/youtube.svg",  # Иконка YouTube
    "https://simpleicons.org/icons/wikipedia.svg",  # Иконка Wikipedia
    "https://simpleicons.org/icons/reddit.svg",  # Иконка Reddit
    "https://simpleicons.org/icons/amazon.svg",  # Иконка Amazon
    "https://simpleicons.org/icons/netflix.svg",  # Иконка Netflix
    "https://simpleicons.org/icons/spotify.svg",  # Иконка Spotify
    "https://simpleicons.org/icons/discord.svg",  # Иконка Discord
    "https://simpleicons.org/icons/slack.svg",  # Иконка Slack
    "https://simpleicons.org/icons/twitch.svg",  # Иконка Twitch
    "https://simpleicons.org/icons/wordpress.svg",  # Иконка WordPress
    "https://simpleicons.org/icons/linux.svg",  # Иконка Linux
]



import random

def generate_user(count):
    users = []
    for index in range(count):
        sex = random.randint(0,1)
        name = random.choice(male_names) if sex == 1 else random.choice(female_names)
        character = random.choice(descriptions)
        icon = random.choice(svg_links)
        users.append(
            {
                'id':index,
                'name':name,
                "disc":character,
                "img":icon
            }
        )
    return users