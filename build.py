"""
PyDetex
https://github.com/ppizarror/PyDetex

BUILD.
"""

import os
import shutil
import struct
import sys

assert len(sys.argv) == 2, 'Argument is required, usage: build.py pyinstaller/pipe/twine'
mode = sys.argv[1].strip()
sys_arch = struct.calcsize('P') * 8

if mode == 'pyinstaller':
    # Check upx
    upx = ''
    if sys.platform == 'win32' and sys_arch == 64:
        upx = '--upx-dir specs'
    pyinstaller = f'python -m PyInstaller' if sys.platform == 'win32' else 'pyinstaller'

    os.system(f'{pyinstaller} specs/PyDetex_Win_Single.spec --noconfirm {upx}')
    os.system(f'{pyinstaller} specs/PyDetex_macOS.spec --noconfirm')

elif mode == 'pipe':
    if os.path.isdir('dist/pipe'):
        for k in os.listdir('dist'):
            if '.egg' in k:
                os.remove(f'dist/{k}')
    if os.path.isdir('dist/pipe'):
        for k in os.listdir('dist/pipe'):
            if 'pydetex-' in k:
                os.remove(f'dist/pipe/{k}')
    if os.path.isdir('build'):
        for k in os.listdir('build'):
            if 'bdist.' in k or k == 'lib':
                shutil.rmtree(f'build/{k}')
    os.system(f'python setup.py sdist --dist-dir dist/pipe bdist_wheel --dist-dir dist/pipe')

elif mode == 'twine':
    if os.path.isdir('dist/pipe'):
        os.system(f'python -m twine upload dist/pipe/*')
    else:
        raise FileNotFoundError('Not distribution been found, execute build.py pipe')

else:
    raise ValueError(f'Unknown mode {mode}')
