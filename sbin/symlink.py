#!/usr/bin/python3

import os
import sys


def sym_link(source, destination):
	os.symlink(source,destination)

if __name__ == "__main__":
	if len(sys.argv) == 3:
		sym_link(sys.argv[1], sys.argv[2])
	else:
		print(len(sys.argv))
		print("Need a source and a destination")
		exit()