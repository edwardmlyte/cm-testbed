# cm-testbed
A playground for testing out chartmuseum index generation

`gen-charts.py <dir>` will quickly generate a load (2000) of helm charts for you, requires an existing chart directory on which to generate from

`dockerrun.sh` runs the docker image of chartmuseum with the `charts` directory as it's chart storage location

Typical use:
```bash
helm create badger
python3 gen-charts.py badger
dockerrun.sh
```

Addition of `run-gen.sh` as a lazy way to quickly create moar charts. Warning, your CPU will be busy af whilst this runs.

Note: there has been almost zero testing of this.
