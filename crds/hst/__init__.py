from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

"""
>>> TYPES.get_row_keys_by_instrument("wfpc2")
['detchip', 'detector', 'direction', 'filter', 'filter1', 'filter2', 'obsdate', 'theta']

>>> TYPES.suffix_to_filekind("acs","drk")
'darkfile'

>>> TYPES.filetype_to_filekind("stis", "dark image")
'darkfile'

>>> TYPES.get_filekinds("wfpc2")
['atodfile', 'biasfile', 'darkfile', 'dgeofile', 'flatfile', 'idctab', 'maskfile', 'offtab', 'shadfile', 'wf4tfile']

>>> TYPES.mapping_validator_key("hst_acs_darkfile.rmap")
('acs_drk_ld.tpn', "hst_acs_darkfile.rmap")

>>> from crds import config

Originally the CDBS .tpn files for STIS LFL and PFL varied by OBSMODE.  This design quirk
was later simplified by the addition of "presence expressions" which activate or deactivate
individual .tpn constraints based on the reference file header.

>>> TYPES.reference_name_to_ld_tpn_key(config.locate_file("pcc2026io_lfl.fits", "hst"))
('stis_lfl_ld.tpn',)

>>> TYPES.reference_name_to_ld_tpn_key(config.locate_file("iaf1723io_lfl.fits", "hst"))
('stis_lfl_ld.tpn',)

>>> TYPES.reference_name_to_validator_key(config.locate_file("pcc2026io_lfl.fits", "hst"))
('stis_lfl.tpn',)

>>> TYPES.reference_name_to_validator_key(config.locate_file("iaf1723io_lfl.fits", "hst"))
('stis_lfl.tpn',)

"""

import os.path

from crds.core import reftypes

TYPES = reftypes.from_package_file("hst", __file__)

OBSERVATORY = TYPES.observatory
INSTRUMENTS = TYPES.instruments
EXTENSIONS = TYPES.extensions
TEXT_DESCR = TYPES.text_descr
FILEKINDS = TYPES.filekinds

HERE  = os.path.dirname(__file__) or "."

UNDEFINED_PARKEY_SUBST_VALUE = "UNDEFINED"

INSTRUMENT_FIXERS = {
    "wfii": "wfpc2",
}

TYPE_FIXERS = {
    ("wfpc2","dark") : "drk", 
}

PROVENANCE_KEYWORDS = ("DESCRIP", "COMMENT", "PEDIGREE", "USEAFTER","HISTORY",)

USEAFTER_KEYWORDS = ("DATE-OBS", "TIME-OBS")  # Dataset keywords matching in UseAfter selectors

DEFAULT_SELECTORS = ("Match", "UseAfter")   # Normal selector hierarchy in rmap

def test():
    """Run hst package doctests."""
    from crds import hst
    import doctest
    return doctest.testmod(hst)
