"""execute notebooks in order and regenerate figures."""
import json, os, sys, traceback
import matplotlib
matplotlib.use('Agg')

BASE = os.path.dirname(os.path.abspath(__file__))

notebooks = [
    ('Analysis', 'pp_analysis_milan.ipynb'),
    ('Analysis', 'pp_analysis_turin.ipynb'),
    ('Regression', 'pp_regression.ipynb'),
]

for folder, nb_name in notebooks:
    nb_path = os.path.join(BASE, folder, nb_name)
    nb_dir  = os.path.join(BASE, folder)
    print(f'\n=== running {folder}/{nb_name} ===')

    with open(nb_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)

    # run cells in the notebook's own directory so relative paths resolve
    os.chdir(nb_dir)

    ns = {'__name__': '__main__'}

    for i, cell in enumerate(nb['cells']):
        if cell['cell_type'] != 'code':
            continue
        src = ''.join(cell['source'])
        if not src.strip():
            continue
        try:
            exec(compile(src, f'cell_{i}', 'exec'), ns)
        except Exception as e:
            print(f'  cell {i} ERROR: {e}')
            traceback.print_exc()

    print(f'  done')

print('\nall notebooks executed — figures updated')
