#!/usr/bin/env python
# -*- coding: utf-8 -*-
#=======================================================================
#  Copyright (C) 2026, Chad L. File, Ph.D.
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#=======================================================================
from __future__ import annotations
__author__ = "Chad L. File, Ph.D."
__author_email__ = "ChadFile@letu.edu"
__date__ = "10 March, 2026"
__url__ = "https://clfile-phd.my.canva.site/"

"""
randomizer.py - reusable CLI utilities and randomization helpers for
engineering/scientific problem generators.

Provides:
  - uniform_in(rng, ndp)
  - build_argparser() returns a base ArgumentParser with
        --seed      (reproducibility)
        --ndp       (decimal places for randomized values)
    Scripts importing this module may extend the parser with
    any domain-specific arguments (temperature, pressure, forces, etc.).

Design goals:
  - Domain agnostic (usable for FE, thermo, fluids, dynamics, ...)
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


# No top-level execution block — this file is meant to be imported.