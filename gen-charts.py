#!/usr/bin/env python
import os, re, sys

name = sys.argv[1]

for i in range(1, 2000):
    with open(f"{name}/Chart.yaml") as f:
        data = f.read()
        data = re.sub(r"version:.*$", f"version: 0.0.{i}\n", data, flags=re.M)
    with open(f"{name}/Chart.yaml", "w") as f:
        f.write(data)
    
    os.system(f"helm package {name}")
    os.system(f"mv {name}*.tgz ~/workspace/ccycloud_ghorg/chartmuseum-testing/charts")

    
