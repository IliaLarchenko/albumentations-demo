import os
import streamlit as st
import albumentations as A

from utils import (
    load_augmentations_config,
    get_arguments,
    get_placeholder_params,
    select_transformations,
    show_random_params,
)
from visuals import (
    select_image,
    show_credentials,
    show_docstring,
    get_transormations_params,
)


def main():
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

            # get the list of transformations names
            transform_names = select_transformations(augmentations, interface_type)

            # get parameters for each transform
            transforms = get_transormations_params(transform_names, augmentations)

            try:
                # apply the transformation to the image
                data = A.ReplayCompose(transforms)(image=image)
                error = 0
            except ValueError:
                error = 1
                st.title(
                    "The error has occurred. \
                Most probably you have passed wrong set of parameters. \
                Check transforms that change the shape of image."
                )

            # proceed only if everything is ok
            if error == 0:
                augmented_image = data["image"]
                # show title
                st.title("Demo of Albumentations")

                st.write("I have deployed this service as a Hugging Face Space: https://huggingface.co/spaces/ilarchenko/albumentations-demo please, check it out!")
                st.write("The version deployed here on Heroku will be deprecated soon.")

                # show the images
                width_transformed = int(
                    width_original / image.shape[1] * augmented_image.shape[1]
                )

                st.image(image, caption="Original image", width=width_original)
                st.image(
                    augmented_image,
                    caption="Transformed image",
                    width=width_transformed,
                )

                # comment about refreshing
                st.write("*Press 'R' to refresh*")

                # random values used to get transformations
                show_random_params(data, interface_type)

                # print additional info
                for transform in transforms:
                    show_docstring(transform)
                    st.code(str(transform))
                show_credentials()

                # adding generic privacy policy
                if "GA" in os.environ:
                    st.markdown(
                        (
                            "[Privacy policy]"
                            + (
                                "(https://htmlpreview.github.io/?"
                                + "https://github.com/IliaLarchenko/"
                                + "albumentations-demo/blob/deploy/docs/privacy.html)"
                            )
                        )
                    )


if __name__ == "__main__":
    main()
