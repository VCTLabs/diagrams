"""
Embedded provides a set of simple embedded device and network nodes.
"""

from diagrams import Node


class _Embedded(Node):
    _provider = "embedded"
    _icon_dir = "resources/embedded"

    fontcolor = "#ffffff"
