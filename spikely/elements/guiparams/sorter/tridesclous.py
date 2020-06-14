from spikesorters.tridesclous import TridesclousSorter
class_default = TridesclousSorter._default_params

gui_params = [
    {
        "name": "output_folder",
        "type": "folder",
        "value": None,
        "default": None,
        "title": "Sorting output folder path.",
        "base_param": True,
    },
    {
        "name": "verbose",
        "type": "bool",
        "value": False,
        "default": False,
        "title": "If True, output from SpikeInterface element is verbose when run.",
        "base_param": True,
    },
    {
        "name": "grouping_property",
        "type": "str",
        "value": None,
        "default": None,
        "title": "Property name to be used for sorter output grouping.",
        "base_param": True,
    },
    {
        "name": "parallel",
        "type": "bool",
        "value": False,
        "default": False,
        "title": "If grouping property specifed, sort property groups in parallel if True.",
        "base_param": True,
    },
    {
        "name": "delete_output_folder",
        "type": "bool",
        "value": False,
        "default": False,
        "title": "Delete specified or default output folder on completion if True.",
        "base_param": True,
    },
    # Tridesclous specific parameters
    {
        "name": "highpass_freq",
        "type": "float",
        "value": class_default["highpass_freq"],
        "default": class_default["highpass_freq"],
        "title": "High-pass frequency",
    },
    {
        "name": "lowpass_freq",
        "type": "float",
        "value": class_default["lowpass_freq"],
        "default": class_default["lowpass_freq"],
        "title": "Low-pass frequency",
    },
    {
        "name": "peak_sign",
        "type": "str",
        "value": class_default["peak_sign"],
        "default": class_default["peak_sign"],
        "title": "Negative or positive peak sign",
    },
    {
        "name": "relative_threshold",
        "type": "float",
        "value": class_default["relative_threshold"],
        "default": class_default["relative_threshold"],
        "title": "Relative threshold for detection",
    },
    {
        "name": "peak_span_ms",
        "type": "float",
        "value": class_default["peak_span_ms"],
        "default": class_default["peak_span_ms"],
        "title": "Time span of peaks for detected events (ms)",
    },
    {
        "name": "wf_left_ms",
        "type": "float",
        "value": class_default["wf_left_ms"],
        "default": class_default["wf_left_ms"],
        "title": "Waveform length before peak (ms)",
    },
    {
        "name": "wf_right_ms",
        "type": "float",
        "value": class_default["wf_right_ms"],
        "default": class_default["wf_right_ms"],
        "title": "Waveform length after peak (ms)",
    },
    {
        "name": "feature_method",
        "type": "str",
        "value": class_default["feature_method"],
        "default": class_default["feature_method"],
        "title": "Feature Extraction Method",
    },
    {
        "name": "cluster_method",
        "type": "str",
        "value": class_default["cluster_method"],
        "default": class_default["cluster_method"],
        "title": "Clustering Method",
    },
    {
        "name": "clean_catalogue_gui",
        "type": "bool",
        "value": class_default["clean_catalogue_gui"],
        "default": class_default["clean_catalogue_gui"],
        "title": "Clean catalogue with an interactive window",
    },
]