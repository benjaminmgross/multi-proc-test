#!/usr/bin/env python
# encoding: utf-8

import argparse
import pandas
from multiprocessing import Process


def get_max(series):
	return series.max()

if __name__ == '__main__':

 	usage = sys.argv[0] + "'json' string"
	description = "uses multi-threading to iterate over a DataFrame"
	parser = argparse.ArgumentParser(description = description, usage = usage)
	parser.add_argument('stream', nargs = 1, type = str, help = 'json stream')

	args = parser.parse_args()

	df = pandas.read_json(args[0], type = 'frame')
	for row in df.index:




