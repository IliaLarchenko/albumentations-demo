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

# TODO: refactor all the new code of professional mode

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
    if status == 0:
        st.title("Can't load image")
    if status == 2:
        st.title("Please, upload the image")
    else:
        placeholder_params = {
            "image_width": image.shape[1],
            "image_height": image.shape[0],
            "image_half_width": int(image.shape[1] / 2),
            "image_half_height": int(image.shape[0] / 2),
        }

        # load the config
        augmentations = load_augmentations_config(
            placeholder_params, "configs/augmentations.json"
        )

        # select a transformation
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

        transforms = []
        for i, transform_name in enumerate(transform_names):
            # select the params values
            st.sidebar.subheader("Params of the " + transform_name)
            param_values = show_transform_control(augmentations[transform_name], i)
            transforms.append(getattr(A, transform_name)(**param_values))

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
            if interface_type == "Professional":
                st.subheader("Random params used")
                random_values = {}
                for applied_params in data["replay"]["transforms"]:
                    random_values[
                        applied_params["__class_fullname__"].split(".")[-1]
                    ] = applied_params["params"]
                st.write(random_values)

            # print additional info
            for transform in transforms:
                show_docstring(transform)
                st.code(str(transform))
            show_credentials()
