{
    'extra_keys': (),
    'file_ext': '.fits',
    'filetype': 'pixel-to-pixel flatfield image',
    'ld_tpn': 'stis_pfl_ld.tpn',
    'parkey': ('DETECTOR', 'OPT_ELEM', 'OBSTYPE', 'CENWAVE', 'APERTURE'),
    'parkey_relevance': {'aperture': '(OBSTYPE == "IMAGING")', 'cenwave': '(OBSTYPE == "SPECTROSCOPIC")'},
    'reffile_format': 'image',
    'reffile_required': 'none',
    'reffile_switch': 'none',
    'rmap_relevance': 'ALWAYS',
    'suffix': 'pfl',
    'text_descr': 'Pixel To Pixel Flat Field Image',
    'tpn': [("OBSTYPE == 'IMAGING'", 'stis_ipfl.tpn'), ("OBSTYPE == 'SPECTROSCOPIC'", 'stis_spfl.tpn')],
    'unique_rowkeys': None,
}