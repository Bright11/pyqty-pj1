# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['login.py'],
    pathex=[],
    binaries=[],
    datas=[('Textslider.py', '.'), ('login.py', '.'), ('registeration.py', '.'), ('sales.py', '.'), ('workers.py', '.'), ('customers.py', '.'), ('expenses.py', '.'), ('riders.py', '.'), ('calculator.py', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='login',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='login',
)
