# -*- coding: utf-8 -*-

import sqlalchemy
from sqlalchemy import MetaData, Table, Column
from sqlalchemy import String
import pandas as pd
from tabulate import tabulate


data_headers = ["id", "name"]
data_index = [0, 1, 2]
data_dct = dict(id=[1, 2, 3], name=["Alice", "Bob", "Cathy"])


tb = tabulate(
    data_dct,
    headers=data_headers,
    tablefmt="fancy_grid",
)
print(tb)