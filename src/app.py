import streamlit as st
import albumentations as A

from utils import (
    load_augmentations_config,
    get_params_string
)
from visuals import (
    show_transform_control,
    select_image,
    show_credentials,
    show_docstring,
)


# show title
st.title("Demo of Albumentations transforms")

# select image
image = select_image(path_to_images="images")

# load the config
augmentations = load_augmentations_config("configs/augmentations.json")

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
st.text("Params passed:" + get_params_string(param_values))
st.text("Press R to update")

# show the images
st.image(
    [image, augmented_image],
    caption=["Original image", "Transformed image"],
    width=320,
)

# print additional info
show_docstring(transform)
show_credentials()
