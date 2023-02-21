try:
    from .production import *
except Exception as e:
    from .local import *
