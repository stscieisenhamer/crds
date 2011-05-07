import os.path
import crds.log as log

def create_path(path):
    """Recursively traverses directory path creating directories as
    needed so that the entire path exists.
    """
    if path.startswith("./"):
        path = path[2:]
    if os.path.exists(path):
        return
    current = []
    for c in path.split("/"):
        if not c:
            current.append("/")
            continue
        current.append(str(c))
        # log.write("Creating", current)
        d = os.path.join(*current)
        d.replace("//","/")
        if not os.path.exists(d):
            os.mkdir(d)

def ensure_dir_exists(fullpath):
    """Creates dirs from `fullpath` if they don't already exist.
    """
    create_path(os.path.dirname(fullpath))


# ===================================================================

def context_to_observatory(context_file):
    """
    >>> context_to_observatory('hst_acs_biasfile.rmap')
    'hst'
    """
    return os.path.basename(context_file).split("_")[0].split(".")[0]

def context_to_instrument(context_file):
    """
    >>> context_to_instrument('hst_acs_biasfile.rmap')
    'acs'
    """
    return os.path.basename(context_file).split("_")[1].split(".")[0]

def context_to_reftype(context_file):
    """
    >>> context_to_reftype('hst_acs_biasfile.rmap')
    'biasfile'
    """
    return os.path.basename(context_file).split("_")[2].split(".")[0]

# ===================================================================

def get_object(dotted_name):
    """Import the given `dotted_name` and return the object."""
    parts = dotted_name.split(".")
    pkgpath = ".".join(parts[:-1])
    cls = parts[-1]
    namespace = {}
    exec "from " + pkgpath + " import " + cls in namespace, namespace
    return namespace[cls]

# ===================================================================

def get_header_union(fname):
    """Get the union of keywords from all header extensions of `fname`.  In
    the case of collisions,  keep the first value found as extensions are loaded
    in numerical order.
    """
    import pyfits
    union = {}
    for hdu in pyfits.open(fname):
        for key in hdu.header:
            newval = hdu.header[key]
            if key not in union:
                union[key] = newval
            elif union[key] != newval:
                log.verbose("*** WARNING: Header union collision on", repr(key), repr(union[key]), repr(hdu.header[key]))
    return union
