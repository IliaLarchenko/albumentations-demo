import os
import streamlit as st
import albumentations as A

from utils import load_augmentations_config, get_arguments
from visuals import (
    show_transform_control,
    select_image,
    show_credentials,
    show_docstring,
)


def get_placeholder_params(image):
    return {
        "image_width": image.shape[1],
        "image_height": image.shape[0],
        "image_half_width": int(image.shape[1] / 2),
        "image_half_height": int(image.shape[0] / 2),
    }


def select_transformations(augmentations: dict, interface_type: str) -> list:
    # in the Simple mode you can choose only one transform
    if interface_type == "Simple":
        transform_names = [
            st.sidebar.selectbox(
                "Select a transformation:", sorted(list(augmentations.keys()))
            )
        ]
    # in the professional mode you can choose several transforms
    elif interface_type == "Professional":
        transform_names = [
            st.sidebar.selectbox(
                "Select transformation №1:", sorted(list(augmentations.keys()))
            )
        ]
        while transform_names[-1] != "None":
            transform_names.append(
                st.sidebar.selectbox(
                    f"Select transformation №{len(transform_names) + 1}:",
                    ["None"] + sorted(list(augmentations.keys())),
                )
            )
        transform_names = transform_names[:-1]
    return transform_names


def get_transormations_params(transform_names: list) -> list:
    transforms = []
    for i, transform_name in enumerate(transform_names):
        # select the params values
        st.sidebar.subheader("Params of the " + transform_name)
        param_values = show_transform_control(augmentations[transform_name], i)
        transforms.append(getattr(A, transform_name)(**param_values))
    return transforms


def show_random_params(data: dict, interface_type: str = "Professional"):
    """Shows random params used for transformation (from A.ReplayCompose)"""
    if interface_type == "Professional":
        st.subheader("Random params used")
        random_values = {}
        for applied_params in data["replay"]["transforms"]:
            random_values[
                applied_params["__class_fullname__"].split(".")[-1]
            ] = applied_params["params"]
        st.write(random_values)


# TODO: refactor all the new code

# get CLI params: the path to images and image width
path_to_images, width_original = get_arguments()

if not os.path.isdir(path_to_images):
    st.title("There is no directory: " + path_to_images)
else:
    # select interface type
    interface_type = st.sidebar.radio(
        "Select the interface mode", ["Simple", "Professional"]
    )

    # select image
    status, image = select_image(path_to_images, interface_type)
    if status == 1:
        st.title("Can't load image")
    if status == 2:
        st.title("Please, upload the image")
    else:
        # image was loaded successfully
        placeholder_params = get_placeholder_params(image)

        # load the config
        augmentations = load_augmentations_config(
            placeholder_params, "configs/augmentations.json"
        )

        # get list of transformations names
        transform_names = select_transformations(augmentations, interface_type)

        # get parameters for each transform
        transforms = get_transormations_params(transform_names)

        try:
            # apply the transformation to the image
            data = A.ReplayCompose(transforms)(image=image)
            error = 0
        except ValueError:
            error = 1
            st.title(
                "The error has occurred. Most probably you have passed wrong set of parameters. \
            Check transforms that change the shape of image."
            )

        # proced only if everything is ok
        if error == 0:
            augmented_image = data["image"]
            # show title
            st.title("Demo of Albumentations")

            # show the images
            width_transformed = int(
                width_original / image.shape[1] * augmented_image.shape[1]
            )

            st.image(image, caption="Original image", width=width_original)
            st.image(
                augmented_image, caption="Transformed image", width=width_transformed
            )

            # random values used to get transformations
            show_random_params(data, interface_type)

            # print additional info
            for transform in transforms:
                show_docstring(transform)
                st.code(str(transform))
            show_credentials()
