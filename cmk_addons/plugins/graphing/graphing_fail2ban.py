#!/usr/bin/env python3
#
# target directory: ~/local/lib/python3/cmk_addons/plugins/fail2ban/graphing/

"""Configuration of metrics"""

from cmk.graphing.v1 import Title
from cmk.graphing.v1.metrics import Color, DecimalNotation, Metric, Unit

metric_current_failed = Metric(
    name = "current_failed",
    title = Title("Current failed"),
    unit = Unit(DecimalNotation("")),
    color = Color.ORANGE,
)

metric_current_banned = Metric(
    name = "current_banned",
    title = Title("Current banned"),
    unit = Unit(DecimalNotation("")),
    color = Color.PINK,
)

metric_total_failed = Metric(
    name = "total_failed",
    title = Title("Total failed"),
    unit = Unit(DecimalNotation("")),
    color = Color.ORANGE,
)

metric_total_banned = Metric(
    name = "total_banned",
    title = Title("Total banned"),
    unit = Unit(DecimalNotation("")),
    color = Color.PINK,
)
