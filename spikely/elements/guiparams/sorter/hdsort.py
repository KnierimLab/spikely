from spikesorters.hdsort import HDSortSorter
class_default = HDSortSorter._default_params

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
    # hdsort specific parameters
    {
        "name": "detect_threshold",
        "type": "float",
        "value": class_default["detect_threshold"],
        "default": class_default["detect_threshold"],
        "title": "Relative detection threshold.",
    },
    {
        "name": "detect_sign",
        "type": "int",
        "value": class_default["detect_sign"],
        "default": class_default["detect_sign"],
        "title": "Use -1, or 1, depending on the sign of the spikes in the recording.",
    },
    {
        "name": "filter",
        "type": "bool",
        "value": class_default["filter"],
        "default": class_default["filter"],
        "title": "If True, the recordings are filtered.",
    },
    {
        "name": "parfor",
        "type": "bool",
        "value": class_default["parfor"],
        "default": class_default["parfor"],
        "title": "Use parallel processing.",
    },
    {
        "name": "hpf",
        "type": "float",
        "value": class_default["hpf"],
        "default": class_default["hpf"],
        "title": "high-pass cutoff frequency.",
    },
    {
        "name": "lpf",
        "type": "float",
        "value": class_default["lpf"],
        "default": class_default["lpf"],
        "title": "low-pass cutoff frequency.",
    },
    {
        "name": "max_el_per_group",
        "type": "int",
        "value": class_default["max_el_per_group"],
        "default": class_default["max_el_per_group"],
        "title": "Maximum number of electrodes per local electrode group.",
    },
    {
        "name": "min_el_per_group",
        "type": "int",
        "value": class_default["min_el_per_group"],
        "default": class_default["min_el_per_group"],
        "title": "Minimum number of electrodes per local electrode group.",
    },
    {
        "name": "add_if_nearer_than",
        "type": "float",
        "value": class_default["add_if_nearer_than"],
        "default": class_default["add_if_nearer_than"],
        "title": "Add to electrode group if distance is closer than this value.",
    },
    {
        "name": "max_distance_within_group",
        "type": "float",
        "value": class_default["max_distance_within_group"],
        "default": class_default["max_distance_within_group"],
        "title": "Maximum distance within group.",
    },
    {
        "name": "n_pc_dims",
        "type": "int",
        "value": class_default["n_pc_dims"],
        "default": class_default["n_pc_dims"],
        "title": "Number of pc dimensions.",
    },
    {
        "name": "chunk_size",
        "type": "int",
        "value": class_default["chunk_size"],
        "default": class_default["chunk_size"],
        "title": "Chunk size in number of samples.",
    },
    {
        "name": "loop_mode",
        "type": "str",
        "value": class_default["loop_mode"],
        "default": class_default["loop_mode"],
        "title": "Loop mode for sorting ('local_parfor', 'loop', 'grid').",
    },
]
