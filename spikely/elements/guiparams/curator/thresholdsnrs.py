from spiketoolkit.validation.quality_metric_classes.parameter_dictionaries import (
    get_validation_params,
)
from spiketoolkit.curation import threshold_snrs
from spiketoolkit.validation.quality_metric_classes.snr import SNR
metric_default = SNR.params
spif_init_func = threshold_snrs
class_default = get_validation_params()

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
        "name": "snr_mode",
        "type": "str",
        "value": metric_default["snr_mode"],
        "default": metric_default["snr_mode"],
        "title": "Mode to compute noise SNR ('mad' | 'std' - default 'mad').",
    },
    {
        "name": "snr_noise_duration",
        "type": "float",
        "value": metric_default["snr_noise_duration"],
        "default": metric_default["snr_noise_duration"],
        "title": "Number of seconds to compute noise level from (default 10.0).",
    },
    {
        "name": "max_spikes_per_unit_for_snr",
        "type": "int",
        "value": metric_default["max_spikes_per_unit_for_snr"],
        "default": metric_default["max_spikes_per_unit_for_snr"],
        "title": "Maximum number of spikes to compute templates from (default 1000).",
    },
    {
        "name": "template_mode",
        "type": "str",
        "value": metric_default["template_mode"],
        "default": metric_default["template_mode"],
        "title": "Use 'mean' or 'median' to compute templates.",
    },
    {
        "name": "max_channel_peak",
        "type": "float",
        "value": metric_default["max_channel_peak"],
        "default": metric_default["max_channel_peak"],
        "title": " If maximum channel has to be found among negative peaks ('neg'), positive ('pos') or both ('both' - default).",
    },
    # kwargs
    {
        "name": "method",
        "type": "str",
        "value": class_default["method"],
        "default": class_default["method"],
        "title": "If 'absolute' (default), amplitudes are absolute amplitudes in uV are returned. \
                  If 'relative', amplitudes are returned as ratios between waveform amplitudes and template amplitudes.",
    },
    {
        "name": "peak",
        "type": "str",
        "value": class_default["peak"],
        "default": class_default["peak"],
        "title": "If maximum channel has to be found among negative peaks ('neg'), positive ('pos') or \
                  both ('both' - default).",
    },
    {
        "name": "frames_before",
        "type": "int",
        "value": class_default["frames_before"],
        "default": class_default["frames_before"],
        "title": "Frames before peak to compute amplitude.",
    },
    {
        "name": "frames_after",
        "type": "int",
        "value": class_default["frames_after"],
        "default": class_default["frames_after"],
        "title": "Frames after peak to compute amplitude.",
    },
    {
        "name": "apply_filter",
        "type": "bool",
        "value": class_default["apply_filter"],
        "default": class_default["apply_filter"],
        "title": "If True, recording is bandpass-filtered",
    },
    {
        "name": "freq_min",
        "type": "float",
        "value": class_default["freq_min"],
        "default": class_default["freq_min"],
        "title": "High-pass frequency for optional filter (default 300 Hz).",
    },
    {
        "name": "freq_max",
        "type": "float",
        "value": class_default["freq_max"],
        "default": class_default["freq_max"],
        "title": "Low-pass frequency for optional filter (default 6000 Hz).",
    },
    {
        "name": "grouping_property",
        "type": "str",
        "value": class_default["grouping_property"],
        "default": class_default["grouping_property"],
        "title": "Property to group channels. E.g. if the recording extractor has the 'group' property and \
                 'grouping_property' is 'group', then waveforms are computed group-wise.",
    },
    {
        "name": "ms_before",
        "type": "float",
        "value": class_default["ms_before"],
        "default": class_default["ms_before"],
        "title": "Time period in ms to cut waveforms before the spike events.",
    },
    {
        "name": "ms_after",
        "type": "float",
        "value": class_default["ms_after"],
        "default": class_default["ms_after"],
        "title": "Time period in ms to cut waveforms after the spike events.",
    },
    {
        "name": "dtype",
        "type": "dtype",
        "value": class_default["dtype"],
        "default": class_default["dtype"],
        "title": "The numpy dtype of the waveforms.",
    },
    {
        "name": "compute_property_from_recording",
        "type": "bool",
        "value": class_default["compute_property_from_recording"],
        "default": class_default["compute_property_from_recording"],
        "title": "If True and 'grouping_property' is given, the property of each unit is assigned as the corresponding \
                  property of the recording extractor channel on which the average waveform is the largest.",
    },
    {
        "name": "max_channels_per_waveforms",
        "type": "int",
        "value": class_default["max_channels_per_waveforms"],
        "default": class_default["max_channels_per_waveforms"],
        "title": " Maximum channels per waveforms to return. If None, all channels are returned.",
    },
    {
        "name": "n_jobs",
        "type": "int",
        "value": class_default["n_jobs"],
        "default": class_default["n_jobs"],
        "title": "Number of parallel jobs (default None).",
    },
    {
        "name": "memmap",
        "type": "bool",
        "value": class_default["memmap"],
        "default": class_default["memmap"],
        "title": "If True, waveforms are saved as memmap object (recommended for long recordings with many channels).",
    },
    {
        "name": "save_property_or_features",
        "type": "bool",
        "value": class_default["save_property_or_features"],
        "default": class_default["save_property_or_features"],
        "title": "If True, it will save features in the sorting extractor.",
    },
    {
        "name": "recompute_info",
        "type": "bool",
        "value": class_default["recompute_info"],
        "default": class_default["recompute_info"],
        "title": "If True, waveforms are recomputed.",
    },
    {
        "name": "max_spikes_per_unit",
        "type": "int",
        "value": class_default["max_spikes_per_unit"],
        "default": class_default["max_spikes_per_unit"],
        "title": "The maximum number of spikes to extract per unit.",
    },
    {
        "name": "seed",
        "type": "int",
        "value": class_default["seed"],
        "default": class_default["seed"],
        "title": "Random seed for reproducibility.",
    },
    {
        "name": "verbose",
        "type": "bool",
        "value": class_default["verbose"],
        "default": class_default["verbose"],
        "title": "If True, output from SpikeInterface element is verbose when run.",
    },
]
