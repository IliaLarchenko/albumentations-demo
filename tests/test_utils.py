# test

from src.utils import get_images_list


def test_get_images_list():
    images_list = get_images_list("images")
    assert isinstance(images_list, list)
    assert len(images_list) > 0
    assert isinstance(images_list[0], str)
