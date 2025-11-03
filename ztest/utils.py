# coding=utf-8

# SPDX-FileCopyrightText: Copyright 2025 Idiap Research Institute <contact@idiap.ch>
# SPDX-FileContributor: Olivier Canévet <olivier.canevet@idiap.ch>
# SPDX-License-Identifier: See LICENSE file

from loguru import logger

class Sum:
    def __init__(self):
        pass

    def __call__(self, a, b):
        logger.info(f"Adding {a} and {b}")
        return a + b
