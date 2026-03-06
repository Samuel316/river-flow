#!/usr/bin/env python3
# coding=utf-8
"""
Copyright Samuel Lloyd
6/3/2026
"""

import importlib
import logging


# --- Set up logging ---


log_format = logging.Formatter(
    "%(asctime)s,%(msecs)03d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s"
)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Add a console handler

handler = logging.StreamHandler()
handler.setFormatter(log_format)
logger.addHandler(handler)

# Add a file handler

file_handler = logging.FileHandler("template.log")
file_handler.setFormatter(log_format)
logger.addHandler(file_handler)

# --- import data for pip install ---

with importlib.resources.open_text("data", "template_data.csv") as file:
    data = file.read()

