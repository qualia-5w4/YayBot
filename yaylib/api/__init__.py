"""

Yay! (nanameue, Inc.) API Client
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An API wrapper for Yay! (yay.space) written in Python.

:copyright: (c) 2023 ekkx
:license: MIT, see LICENSE for more details.

"""

from .auth import *
from .call import *
from .chat import *
from .group import *
from .misc import *
from .post import *

__all__ = [
    "auth",
    "call",
    "chat",
    "group",
    "misc",
    "post",
]
