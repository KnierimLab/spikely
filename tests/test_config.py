"""Test functionality associated with config.py"""

import random
import sys

import pytest
from PyQt5 import QtWidgets
from spikely import config
from spikely.elements.extractor import Extractor
from spikely.spikely_main import SpikelyMainWindow


class TestCvt():

    # @pytest.mark.smoke
    def test_cvt_elem_raises(self):
        """cvt_elem_to_dict() shoule raise exception on invalid parameter"""
        with pytest.raises(TypeError):
            config.cvt_elem_to_dict('not a SpikeElement')

    def test_cvt_dict_raises(self):
        """cvt_dict_to_elem() shoule raise exception on invalid parameter"""
        with pytest.raises(TypeError):
            config.cvt_dict_to_elem('not a SpikeElement')

    # @pytest.mark.skip(reason='Need clarity from developer')
    def test_cvt_methods(self):
        """Test the methods used to enable JSON coding/decoding.

        Before JSON encoding, a SpikeElement is converted into a data-based
        dictionary representation using cvt_elem_to_dict().  After JSON
        decoding, the resultant dictionary is re-instantiated as a SpikeElement
        using cvt_dict_to_elem().

        This test runs through both conversions back-to-back and compares the
        resultant SpikeElement with the original SpikeElement to ensure
        identity.

        """
        cls_list = Extractor.get_installed_spif_cls_list()
        elem = Extractor(
            cls_list[random.randint(0, len(cls_list) - 1)]
        )
        elem_dict = config.cvt_elem_to_dict(elem)
        new_elem = config.cvt_dict_to_elem(elem_dict)

        print(f'SpikeElement tested: {elem.display_name}')

        assert elem.__class__.__name__ == new_elem.__class__.__name__
        assert elem.__module__ == new_elem.__module__
        assert elem.spif_class.__name__ == new_elem.spif_class.__name__
        assert elem.param_list == new_elem.param_list


# @pytest.mark.smoke
def test_get_main_window():
    """Tests function that finds reference to app's main window."""
    app = QtWidgets.QApplication(sys.argv)  # noqa: F841
    win = SpikelyMainWindow()
    found_win = config.get_main_window()

    assert win is found_win
