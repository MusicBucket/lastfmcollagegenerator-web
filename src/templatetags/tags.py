import os

from jinja2_simple_tags import StandaloneTag


class GATag(StandaloneTag):
    """
    Create a {% ga_tag %} tag.
    """
    tags = {"ga_tag"}

    def render(self):
        return os.getenv("GA_TAG")
