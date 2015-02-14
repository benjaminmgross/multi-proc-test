#!/usr/bin/env python
# encoding: utf-8

import numpy
import pandas

def create_frame(n_rows, n_cols):
	df = pandas.DataFrame(numpy.random.randn(n_rows, n_cols))
	return df.to_json()