import streamlit as st

# TODO: rename and refactor everything


def select_num_interval(
    param_name: str, limits_list: list, defaults, n_for_hash, **kwargs
):
    st.sidebar.subheader(param_name)
    min_max_interval = st.sidebar.slider(
        "",
        limits_list[0],
        limits_list[1],
        defaults,
        key=hash(param_name + str(n_for_hash)),
    )
    return min_max_interval


def select_several_nums(
    param_name, subparam_names, limits_list, defaults_list, n_for_hash, **kwargs
):
    st.sidebar.subheader(param_name)
    result = []
    assert len(limits_list) == len(defaults_list)
    assert len(subparam_names) == len(defaults_list)

    for name, limits, defaults in zip(subparam_names, limits_list, defaults_list):
        result.append(
            st.sidebar.slider(
                name,
                limits[0],
                limits[1],
                defaults,
                key=hash(param_name + name + str(n_for_hash)),
            )
        )
    return tuple(result)


def select_min_max(
    param_name, limits_list, defaults_list, n_for_hash, min_diff=0, **kwargs
):
    assert len(param_name) == 2
    result = list(
        select_num_interval(
            " & ".join(param_name), limits_list, defaults_list, n_for_hash
        )
    )
    if result[1] - result[0] < min_diff:
        diff = min_diff - result[1] + result[0]
        if result[1] + diff <= limits_list[1]:
            result[1] = result[1] + diff
        elif result[0] - diff >= limits_list[0]:
            result[0] = result[0] - diff
        else:
            result = limits_list
    return tuple(result)


def select_RGB(param_name, n_for_hash, **kwargs):
    result = select_several_nums(
        param_name,
        subparam_names=["Red", "Green", "Blue"],
        limits_list=[[0, 255], [0, 255], [0, 255]],
        defaults_list=[0, 0, 0],
        n_for_hash=n_for_hash,
    )
    return tuple(result)


def replace_none(string):
    if string == "None":
        return None
    else:
        return string


def select_radio(param_name, options_list, n_for_hash, **kwargs):
    st.sidebar.subheader(param_name)
    result = st.sidebar.radio("", options_list, key=hash(param_name + str(n_for_hash)))
    return replace_none(result)


def select_checkbox(param_name, defaults, n_for_hash, **kwargs):
    st.sidebar.subheader(param_name)
    result = st.sidebar.checkbox(
        "True", defaults, key=hash(param_name + str(n_for_hash))
    )
    return result


# dict from param name to function showing this param
param2func = {
    "num_interval": select_num_interval,
    "several_nums": select_several_nums,
    "radio": select_radio,
    "rgb": select_RGB,
    "checkbox": select_checkbox,
    "min_max": select_min_max,
}
