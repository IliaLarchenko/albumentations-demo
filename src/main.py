import streamlit as st
import albumentations as A

from control import *
from utils import (
    load_augmentations_config,
    generate_executable_string,
)
from visuals import (
    show_transform_control,
    select_image,
    show_credentials,
    show_docstring,
)


# main
st.title("Demo of Albumentations transforms")
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
executable_string = generate_executable_string(transform_name, param_values)
st.text(executable_string)
exec("transform = A." + executable_string)
augmented_image = transform(image=image)["image"]

# show the images
st.text("Press R to update")
st.image(
    [image, augmented_image],
    caption=["Original image", "Transformed image"],
    width=320,
)

# print additional info
show_docstring(transform)
show_credentials()
