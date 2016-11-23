import cclib.parser
import sys

nwlog = cclib.parser.NWChem(sys.argv[1])
data = nwlog.parse()
