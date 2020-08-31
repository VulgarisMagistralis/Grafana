#!/usr/bin/env python

from subprocess import Popen, PIPE

process = Popen(['cat',' out.json'], stdout=PIPE, stderr=PIPE)
stdout, stderr = process.communicate()
print stdout
