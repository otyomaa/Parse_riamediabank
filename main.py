import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

from auth_temp import user_agent


def parse():
    headers = {"User-Agent": user_agent}

    # URL сайта
    base_url = "https://riamediabank.ru"
    story_url = "/search/?selection=story"

    save_folder = "downloaded_images"

    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    num_images_to_download = int(input("Введите количество изображений для скачивания: "))

    soup = BeautifulSoup(requests.get(urljoin(base_url, story_url), headers=headers).text, "html.parser")

    a_tags = soup.find_all("a", class_="list-item__link")

    downloaded_count = 0

    for a_tag in a_tags:
        if downloaded_count >= num_images_to_download:
            break

        a_page_soup = BeautifulSoup(requests.get(urljoin(base_url, a_tag.get("href")), headers=headers).text,
                                    "html.parser")

        a_tags_page = a_page_soup.find_all("a", class_="list-item__link")

        for a_tag_page in a_tags_page:
            if downloaded_count >= num_images_to_download:
                break

            pic_soup = BeautifulSoup(requests.get(urljoin(base_url, story_url, a_tag_page.get("href")), headers=headers).text,
                                     "html.parser")

            img_src = pic_soup.find("figure", class_="media__figure").find("img").get("src")

            h3_tag = pic_soup.find("div", class_="media__col_l").find("h3", class_="media__description")

            img_name = f"{'_'.join(h3_tag.string.split()[:30])}.jpg"

            img_response = requests.get(img_src, headers=headers)
            if img_response.status_code == 200:
                img_path = os.path.join(save_folder, img_name)
                with open(img_path, "wb") as img_file:
                    img_file.write(img_response.content)
                    downloaded_count += 1
                    print(f"Скачено изображений: {downloaded_count}/{num_images_to_download}", img_name, sep='\n')

    print("Загрузка завершена.")


if __name__ == "__main__":
    parse()
