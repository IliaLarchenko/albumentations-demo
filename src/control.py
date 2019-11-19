import streamlit as st


def select_int_interval(param_name, limits_list, defaults, **kwargs):
    st.sidebar.subheader(param_name)
    min_max_interval = st.sidebar.slider('', limits_list[0], limits_list[1], defaults, key = hash(param_name))
    return min_max_interval


def select_several_ints(param_name, subparam_names, limits_list, defaults_list, **kwargs):
    st.sidebar.subheader(param_name)
    result = []
    assert len(limits_list) == len(defaults_list)
    assert len(subparam_names) == len(defaults_list)
    
    for name, limits, defaults in zip(subparam_names, limits_list, defaults_list):
        result.append(st.sidebar.slider(name, limits[0], limits[1], defaults, key = hash(param_name + name)))
    return tuple(result)

def select_several_RGB(param_name, **kwargs):
    result = select_several_ints(param_name, 
                                 subparam_names = ["Red", "Green", "Blue"], 
                                 limits_list = [[0, 255],[0, 255],[0, 255]],
                                 defaults_list = [0, 0, 0])
    return tuple(result)


def select_radio(param_name, options_list, **kwargs):
    st.sidebar.subheader(param_name)
    result = st.sidebar.radio('', options_list)
    if isinstance(options_list[0],str):
        result = '"' + result + '"'
    return result


def select_checkbox(param_name, defaults, **kwargs):
    st.sidebar.subheader(param_name)
    result = st.sidebar.checkbox("True", defaults)
    return result



# dict from param name to function showing this param
param2func = {
    'int_interval': select_int_interval,
    'several_ints': select_several_ints,
    'radio': select_radio,
    'rgb': select_several_RGB,
    'checkbox': select_checkbox

}