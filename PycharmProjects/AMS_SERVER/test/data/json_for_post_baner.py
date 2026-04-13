from random import randint

image_path = "/image_data/red_forest_16_9.jpg"
name = f"Название Банера № {randint(1, 1000)}"
json_for_post_baner = {
    "name": f"{name}",
    "aspect_ratio": "16:9",
    "banner_type_id": 1,
    "platform_ids": [
        7,
        8,
        9,
        11,
        12,
        10
    ],
    "show_duration": 3,
    "image_path": image_path,
}

