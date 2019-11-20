import streamlit as st

from control import param2func
from utils import get_images_list, load_image


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
