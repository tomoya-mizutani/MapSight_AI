python - << 'PY'
import json
import jsonschema
import time

SCHEMA_PATH = "schemas/player_position.schema.json"
DATA_PATH   = "data/positions/2025-09-18/Erangel1/positions.jsonl"

t0 = time.perf_counter()
print(f"[INFO] schema={SCHEMA_PATH}")
print(f"[INFO] data  ={DATA_PATH}")

with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
    schema = json.load(f)

ok = 0
bad = 0
PYint(f"[DONE] validated_ok={ok} bad={bad} elapsed={dt:.2f}s")
[INFO] schema=schemas/player_position.schema.json
[INFO] data  =data/positions/2025-09-18/Erangel1/positions.jsonl
Traceback (most recent call last):
  File "<stdin>", line 13, in <module>
  File "/usr/lib/python3.12/json/__init__.py", line 293, in load
    return loads(fp.read(),
           ^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/json/__init__.py", line 346, in loads
    return _default_decoder.decode(s)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/json/decoder.py", line 337, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/json/decoder.py", line 355, in raw_decode
    raise JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)