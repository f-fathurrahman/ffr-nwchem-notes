## Using OpenBabel's `babel` to read geometry from NWChem log file

Code:
```
babel LOG.nwo LOG.xyz
```

OpenBabel recognize NWChem log file with extension `.nwo`. It seems that OpenBabel
only able to read one geometry only.


## Testing `cclib` for parsing NWChem log file

Code:
```python
import cclib.parser
nwlog = cclib.parser.NWChem("LOG.nwo")
data = nwlog.parse()
```

I got the following errors:
```
/home/efefer/mysoftwares/lib/python2.7/site-packages/cclib/parser/nwchemparser.pyc in extract(self, inputfile, line)
    110                 line = next(inputfile)
    111
--> 112             self.set_attribute('geotargets', [gmax, grms, xmax, xrms])
    113
    114         # NWChem does not normally print the basis set for each atom, but rather

UnboundLocalError: local variable 'gmax' referenced before assignment
```

and the following warning:
```
[NWChem LOG.nwo WARNING] In nwchemparser.py, line 99, line not blank as expected: maximum gradient threshold         (gmax) =   0.000450
```
