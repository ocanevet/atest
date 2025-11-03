# coding=utf-8

# SPDX-FileCopyrightText: Copyright 2025 Idiap Research Institute <contact@idiap.ch>
# SPDX-FileContributor: Olivier Canévet <olivier.canevet@idiap.ch>
# SPDX-License-Identifier: See LICENSE file

import argparse

from loguru import logger

import ztest


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", type=int, default=1, help="Variable a")
    parser.add_argument("-b", type=int, default=2, help="Variable b")
    args = parser.parse_args()

    op = ztest.Sum()
    s = op(args.a, args.b)
    logger.info(f"The sum is {s}")


if __name__ == "__main__":
    main()
