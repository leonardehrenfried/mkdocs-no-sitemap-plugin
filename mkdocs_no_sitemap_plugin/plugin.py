"""Mkdocs plugin for disabling the sitemap"""
import logging
from mkdocs.plugins import BasePlugin


LOGGER = logging.getLogger(__name__)


class NoSitemapPlugin(BasePlugin):
    def __init__(self):
        pass

    def on_post_template(self,output_content,template_name,config):
        if template_name == "sitemap.xml":
            return ""
