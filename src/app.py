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

# get CLI params: the path to images and image width
path_to_images, width_original = get_arguments()
if not os.path.isdir(path_to_images):
    st.title("There is no directory: " + path_to_images)
else:
    # select image
    status, image = select_image(path_to_images)
    if status == 0:
        st.title("Can't load image from: " + path_to_images)
    else:
        # show title
        st.title("Demo of Albumentations")

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
        transform_name = st.sidebar.selectbox(
            "Select a transformation:", sorted(list(augmentations.keys()))
        )

        # select the params values
        param_values = show_transform_control(augmentations[transform_name])

        # apply the transformation to the image
        transform = getattr(A, transform_name)(**param_values)
        data = A.ReplayCompose([transform])(image=image)
        augmented_image = data["image"]

        # TODO add convinient replay compose
        # applied_params = data["replay"]["transforms"][0]['params']
        # for k,v in applied_params.items():
        #     applied_params[k] = str(v)
        # st.write(applied_params)
        # st.write(data["replay"])

        # show the images
        width_transformed = int(
            width_original / image.shape[1] * augmented_image.shape[1]
        )

        st.image(image, caption="Original image", width=width_original)
        st.image(augmented_image, caption="Transformed image", width=width_transformed)

        # print additional info
        st.code(str(transform))
        show_docstring(transform)
        show_credentials()
