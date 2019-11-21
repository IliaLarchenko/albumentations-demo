import streamlit as st
import albumentations as A

from utils import load_augmentations_config
from visuals import (
    show_transform_control,
    select_image,
    show_credentials,
    show_docstring,
)


# show title
st.title("Demo of Albumentations")

# select image
image = select_image(path_to_images="images")
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
augmented_image = transform(image=image)["image"]

# show the params passed
# st.text("Params passed: ")
# st.code(get_params_string(param_values))
# st.text("Press R to update")

# show the images
width_original = 400
width_transformed = int(width_original / image.shape[1] * augmented_image.shape[1])

st.image(
    image, caption="Original image", width=width_original,
)
st.image(
    augmented_image, caption="Transformed image", width=width_transformed,
)

# print additional info
st.code(str(transform))
show_docstring(transform)
show_credentials()
