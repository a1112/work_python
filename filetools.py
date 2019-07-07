import shutil
import logging

def copytree(src, dst, symlinks=False, ignore=None, copy_function=shutil.copy2,
             ignore_dangling_symlinks=False):

    return shutil.copytree(src, dst, symlinks, ignore, copy_function,ignore_dangling_symlinks)
    '''
    from shutil import copytree, ignore_patterns

copytree(source, destination, ignore=ignore_patterns('*.pyc', 'tmp*'))
    '''