import cv2
import os
import json

import streamlit as st


@st.cache
def load_image(image_name, path_to_folder="../images"):
    path_to_image = os.path.join(path_to_folder, image_name)
    image = cv2.imread(path_to_image)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image


@st.cache
def get_images_list(path_to_folder):
    image_names_list = [
        x for x in os.listdir(path_to_folder) if x[-3:] in ["jpg", "peg", "png"]
    ]
    return image_names_list


@st.cache
def load_augmentations_config(path_to_config: str = "configs/augmentations.json"):
    with open(path_to_config, "r") as config_file:
        augmentations = json.load(config_file)
    return augmentations


def generate_executable_string(transform_name, param_values):
    params_string = ", ".join(
        [k + "=" + str(param_values[k]) for k in param_values.keys()] + ["p=1.0"]
    )
    params_string = "(" + params_string + ")"
    return transform_name + params_string
