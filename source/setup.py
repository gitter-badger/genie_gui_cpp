from distutils.core import setup
import py2exe

setup(
    windows = [{
        "script": "geniegui.pyw",
	}],
    data_files = ["icon.png"],
	options = {
    	"py2exe": {
    		'includes': ["sip"],
    		'bundle_files': 3,
    		'compressed': True
    	}
	},
	zipfile = None
)
