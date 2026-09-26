from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path

PLUGIN = Path(__file__).with_name('connected_spectrum.py')

def load_plugin():
    spec = importlib.util.spec_from_file_location('connected_spectrum', PLUGIN)
    if spec is None or spec.loader is None:
        raise RuntimeError('cannot load connected_spectrum.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--X', type=int, default=100000)
    parser.add_argument('--Q', type=int, default=199)
    parser.add_argument('--kmax', type=int, default=8)
    parser.add_argument('--precision', type=int, default=70)
    parser.add_argument('--output', default='primary_result.json')
    args = parser.parse_args()

    module = load_plugin()
    cfg = {'X':args.X,'Q':args.Q,'kmax':args.kmax,'precision':args.precision}
    result = module.primary_compute(cfg)
    Path(args.output).write_text(json.dumps(result,indent=2,sort_keys=True),encoding='utf-8')
    print(json.dumps({'status':result['status'],'candidate_count':result['candidate_count'],'D':result['D']}))

if __name__ == '__main__':
    main()
