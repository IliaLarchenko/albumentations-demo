import streamlit as st
import albumentations as A

from control import *
from utils import (
    load_image,
    get_images_list,
    load_augmentations_config,
    generate_executable_string,
)


def select_image(path_to_images: str = "images"):
    image_names_list = get_images_list(path_to_images)
    image_name = st.sidebar.selectbox("Select an image:", image_names_list)
    image = load_image(image_name, path_to_images)
    return image


def show_transform_control(transform_params: dict):
    param_values = {}
    if len(transform_params) == 0:
        st.sidebar.text(transform_name + " transform has no parameters")
    else:
        for param in transform_params:
            param_values[param["param_name"]] = param2func[param["type"]](**param)
    return param_values


def show_credentials():
    st.text("")
    st.text("")
    st.subheader("Credentials:")
    st.text("Source: https://github.com/IliaLarchenko/albumentations-demo")
    st.text(
        "Albumentations library: https://github.com/albumentations-team/albumentations"
    )
    st.text("Image Source: https://www.pexels.com/royalty-free-images/")


def show_docstring(object):
    st.subheader("Docstring:")
    st.text(str(object.__doc__))


# main
st.title("Demo of Albumentations transforms")

# selecting an image
image = select_image(path_to_images="images")

# load the config
augmentations = load_augmentations_config("configs/augmentations.json")
transform_name = st.sidebar.selectbox(
    "Select a transformation:", sorted(list(augmentations.keys()))
)

# select the params values
param_values = show_transform_control(augmentations[transform_name])
executable_string = generate_executable_string(transform_name, param_values)

st.text(executable_string)
st.text("Press R to update")
exec("transform = A." + executable_string)
augmented_image = transform(image=image)["image"]

st.image(
    [image, augmented_image],
    caption=["Original image", "Transformed image"],
    width=320,
)

show_docstring(transform)
show_credentials()
