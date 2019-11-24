import cv2
import streamlit as st

from control import param2func
from utils import get_images_list, load_image


def show_logo():
    st.image(load_image("logo.png", "../images"), format="PNG")


def select_image(path_to_images: str):
    image_names_list = get_images_list(path_to_images)
    if len(image_names_list) < 1:
        return 0, 0
    else:
        try:
            image_name = st.sidebar.selectbox("Select an image:", image_names_list)
            image = load_image(image_name, path_to_images)
            return 1, image
        except cv2.error:
            return 0, 0


def show_transform_control(transform_params: dict) -> dict:
    param_values = {"p": 1.0}
    if len(transform_params) == 0:
        st.sidebar.text("Transform has no parameters")
    else:
        for param in transform_params:
            control_function = param2func[param["type"]]
            if isinstance(param["param_name"], list):
                returned_values = control_function(**param)
                for name, value in zip(param["param_name"], returned_values):
                    param_values[name] = value
            else:
                param_values[param["param_name"]] = control_function(**param)
    return param_values


def show_credentials():
    st.markdown("* * *")
    st.subheader("Credentials:")
    st.markdown(
        (
            "Source: [github.com/IliaLarchenko/albumentations-demo]"
            "(https://github.com/IliaLarchenko/albumentations-demo)"
        )
    )
    st.markdown(
        (
            "Albumentations library: [github.com/albumentations-team/albumentations]"
            "(https://github.com/albumentations-team/albumentations)"
        )
    )
    st.markdown(
        (
            "Image Source: [pexels.com/royalty-free-images]"
            "(https://pexels.com/royalty-free-images/)"
        )
    )


def show_docstring(obj_with_ds):
    st.markdown("* * *")
    st.subheader("Docstring:")
    st.text(obj_with_ds.__doc__)
