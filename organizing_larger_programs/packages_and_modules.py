import urllib
print(type(urllib))

# urllib.request (module) is nested inside urllib (package)
import urllib.request
print(type(urllib.request))

# Even when imported this way, the sub-module knows its own hierarchical module name
from urllib import request
print(request)

# The urllib package has a __path__ member that urllib.request does not have
# The __path__ attribute is a list of system paths indicating where urllib searches to find nested modules
# Note that packages are generally directories, while modules are generally files
print(urllib.__path__)
