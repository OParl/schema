from pyld import jsonld
import json
import sys

sep = "============================================================="

try:
	CONTEXT_PATH = sys.argv[1]
	JSON_PATH = sys.argv[2]
except:
	print("Usage: python test.py <context_path> <doc_path>")
	sys.exit(1)

context = json.load(open(CONTEXT_PATH, "rb"))
doc = json.load(open(JSON_PATH, "rb"))
compacted = jsonld.compact(doc, context)
expanded = jsonld.expand(compacted)
flattened = jsonld.flatten(doc)

print(sep)
print("Testing context '%s' with document '%s'" % (CONTEXT_PATH, JSON_PATH))

print(sep)
print("Compacted:")
print(json.dumps(compacted, indent=4))

print(sep)
print("Expanded:")
print(json.dumps(expanded, indent=4))

print(sep)
print("Flattened:")
print(json.dumps(flattened, indent=4))
