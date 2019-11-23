# test

import numpy as np
import albumentations as A

from src.utils import get_images_list, load_image, load_augmentations_config


def test_get_images_list():
    images_list = get_images_list("images")
    assert isinstance(images_list, list)
    assert len(images_list) > 0
    assert isinstance(images_list[0], str)


def test_load_image():
    images_list = get_images_list("images")
    for image_name in images_list:
        image = load_image(image_name, path_to_folder="images", bgr2rgb=True)
        assert len(image.shape) == 3, f"error in {image_name}"
        assert image.shape[2] == 3, f"error in {image_name}"
        assert image.max() <= 255, f"error in {image_name}"
        assert image.min() >= 0, f"error in {image_name}"


def test_load_augmentations_config():
    image = np.random.randint(0, 255, (100, 100, 3)).astype(np.uint8)
    placeholder_params = {
        "image_width": image.shape[1],
        "image_height": image.shape[0],
        "image_half_width": int(image.shape[1] / 2),
        "image_half_height": int(image.shape[0] / 2),
    }
    augmentations = load_augmentations_config(
        placeholder_params, path_to_config="configs/augmentations.json"
    )

    for transform_name in augmentations.keys():
        if transform_name in [
            "CenterCrop",
            "RandomCrop",
            "RandomResizedCrop",
            "Resize",
        ]:
            param_values = {"p": 1.0, "height": 10, "width": 10}
        elif transform_name in ["RandomSizedCrop"]:
            param_values = {
                "p": 1.0,
                "height": 10,
                "width": 10,
                "min_max_height": (50, 50),
            }
        elif transform_name in ["Crop"]:
            param_values = {"p": 1.0, "x_max": 10, "y_max": 10}
        else:
            param_values = {"p": 1.0}
        transform = getattr(A, transform_name)(**param_values)
        transformed_image = transform(image=image)["image"]
        assert len(transformed_image.shape) == 3, f"error in {str(transform)}"
        assert transformed_image.shape[2] == 3, f"error in {str(transform)}"
        assert transformed_image.max() <= 255, f"error in {str(transform)}"
        assert transformed_image.min() >= 0, f"error in {str(transform)}"
