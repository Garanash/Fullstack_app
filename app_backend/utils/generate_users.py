from app_backend.utils.data_for_generation import *
import random


def generate_user(count):
    users = []
    for index in range(count):
        sex = random.randint(0, 1)
        name = random.choice(male_names) if sex == 1 else random.choice(female_names)
        character = random.choice(descriptions)
        icon = random.choice(svg_links)
        users.append(
            {
                'id': index,
                'name': name,
                "disc": character,
                "img": icon
            }
        )
    return users