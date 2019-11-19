import streamlit as st


def select_int_interval(param_name, limits_list, defaults_list, **kwargs):
    st.sidebar.subheader(param_name)
    min_max_interval = st.sidebar.slider('', limits_list[0], limits_list[1], defaults_list)
    return min_max_interval

def select_several_ints(param_name, subparam_names, limits_list, defaults_list, **kwargs):
    st.sidebar.subheader(param_name)
    result = []
    assert len(limits_list) == len(defaults_list)
    assert len(subparam_names) == len(defaults_list)
    
    for name, limits, defaults in zip(subparam_names, limits_list, defaults_list):
        result.append(st.sidebar.slider(name, limits[0], limits[1], defaults))
    return tuple(result)


# dict from param name to function showing this param
param2func = {
    'int_interval': select_int_interval,
    'several_ints': select_several_ints,
    
}