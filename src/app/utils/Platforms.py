"""
This module defines the supported platforms.
"""

from enum import Enum, unique


@unique
class Platform(Enum):
    """
    Supported platforms.
    """

    SUNING = "https://www.suning.com/"
    DANGDANG = "https://www.dangdang.com/"
