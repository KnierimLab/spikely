gui_params = [
    {
        "name": "threshold",
        "type": "float",
        "title": "The threshold for the given metric.",
    },
    {
        "name": "threshold_sign",
        "type": "str",
        "title": "If 'less', will threshold any metric less than the given threshold. \
                  If 'less_or_equal', will threshold any metric less than or equal to the given threshold. \
                  If 'greater', will threshold any metric greater than the given threshold. \
                  If 'greater_or_equal', will threshold any metric greater than or equal to the given threshold.",
    },
    {
        "name": "sampling_frequency",
        "type": "float",
        "value": None,
        "default": None,
        "title": "The sampling frequency of the result. If None, will check to see if sampling frequency is in sorting extractor.",
    },
    #kwargs
    {
        "name": "save_property_or_features",
        "type": "bool",
        "value": True,
        "default": True,
        "title": "If True, it will save features in the sorting extractor.",
    },
    {
        "name": "verbose",
        "type": "bool",
        "value": False,
        "default": False,
        "title": "If True, output from SpikeInterface element is verbose when run.",
    },
]