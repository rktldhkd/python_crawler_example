# -*- mode: python -*-

block_cipher = None


a = Analysis(['naver_login_auto.py'],
             pathex=['C:\\dev\\git\\python\\python_crawler_example\\crawling\\celenium_sample'],
             binaries=[('C:\\dev\\git\\python\\python_crawler_example\\webDriver\\chromedriver.exe', '.')],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='naver_login_auto',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
