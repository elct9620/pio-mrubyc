Import('env')
from os.path import join, realpath, islink, abspath, isdir
from os import symlink, unlink

# Initialize
hal_symbol = abspath(join("mrubyc", "src", "hal"))
if islink(hal_symbol):
    unlink(hal_symbol)

mcu = env.get('BOARD_MCU')
hal_mcu_dir = realpath(join("mrubyc", "src", "hal_" + mcu))
if isdir(hal_mcu_dir):
    symlink(hal_mcu_dir, hal_symbol)
    env.Append(CPPDEFINES=[("HAL", mcu)])

# Default HAL=posix
if not islink(hal_symbol):
    src = realpath(join("mrubyc", "src", "hal_posix"))
    symlink(src, hal_symbol)
