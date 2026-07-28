#!/usr/bin/env python
# -*- coding: utf-8 -*-
#=======================================================================
# Copyright (C) 2026, Chad L. File, Ph.D.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#=======================================================================
from __future__ import annotations

__author__ = "Chad L. File, Ph.D."
__author_email__ = "ChadFile@letu.edu"
__date__ = "11 March, 2026"
__url__ = "https://clfile-phd.my.canva.site/"

"""
randomizer.py - reusable CLI utilities and randomization helpers for
engineering/scientific problem generators.

Provides:
  - uniform_in(rng, ndp)
  - build_argparser()  -> base ArgumentParser with --seed
  - add_precision_arg(parser, name, default_ndp=1)
      Convenience to add a per-variable precision flag: --<name>-ndp
  - get_ndp(args, name, fallback=1)
      Convenience to retrieve the parsed per-variable precision

Design goals:
  - Domain agnostic (FE, thermo, fluids, dynamics, ...)
  - Plays nicely with problem-specific flags added by caller scripts
  - Predictable and reproducible randomization
  - OS cross-compatible range definitions
"""

import argparse
import random
from typing import Tuple

# ---------------------------------------------------------------------------
# Randomization utilities
# ---------------------------------------------------------------------------
def uniform_in(rng: Tuple[float, float], ndp: int = 1) -> float:
    """
    Draw a uniform random number from [a, b] and round to ndp decimals.

    Parameters
    ----------
    rng : (float, float)
        Bounds for randomization. Ordering does not matter.
    ndp : int
        Number of decimal places; must be non-negative.

    Returns
    -------
    float
        Rounded random value.
    """
    a, b = rng
    if a > b:
        a, b = b, a
    if ndp < 0:
        raise ValueError("ndp must be a non-negative integer.")
    return round(random.uniform(a, b), ndp)


# ---------------------------------------------------------------------------
# Base CLI parser
# ---------------------------------------------------------------------------
def build_argparser(description: str | None = None) -> argparse.ArgumentParser:
    """
    Create a *generic* argument parser for problem generators.
    This parser is intentionally minimal. Individual scripts
    should extend it with their domain-specific flags
    (e.g., --temp1, --pressure, --length-range, --voltage, etc.).

    Returns
    -------
    argparse.ArgumentParser
        A parser ready for extension before calling parse_args().
    """
    p = argparse.ArgumentParser(
        description=description or (
            "General-purpose randomization controls for problem generation."
        ),
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    # Reproducibility
    p.add_argument(
        "--seed",
        type=int,
        help="Random seed for reproducibility."
    )
    return p


# ---------------------------------------------------------------------------
# New helpers for per-variable precision (NDP)
# ---------------------------------------------------------------------------
def add_precision_arg(parser: argparse.ArgumentParser, name: str, default_ndp: int = 1) -> None:
    """
    Add a per-variable decimal precision argument to the parser:
        --<name>-ndp

    Example: add_precision_arg(parser, "pressure") adds:
        --pressure-ndp

    Parameters
    ----------
    parser : argparse.ArgumentParser
        Parser to extend.
    name : str
        Base flag name (without leading dashes).
    default_ndp : int
        Default decimal places for this variable.
    """
    parser.add_argument(f"--{name}-ndp", type=int, default=default_ndp,
                        help=f"Decimal places for '{name}'")


def get_ndp(args, name: str, fallback: int = 1) -> int:
    """
    Retrieve per-variable decimal places from parsed args.
    Looks for 'args.<name>_ndp' and falls back if missing.

    Example:
        ndp_p = get_ndp(args, "pressure", 2)

    Returns
    -------
    int
    """
    attr = f"{name}_ndp"
    return getattr(args, attr, fallback)


"""Option 1: Shuffle in place"""
# arr = ['a', 'b', 'c', 'd', 'e']
# random.shuffle(arr)
# print(arr)

"""Option 2: Return a new randomly ordered list (without modifying the original)"""
# arr = ['a', 'b', 'c', 'd', 'e']
# shuffled = random.sample(arr, k=len(arr))
# print(shuffled)

# No top-level execution block — this file is meant to be imported.