# -*- encoding: utf-8 -*-
"""
Пути к файлам и каталогам
"""
import os.path

for path in [ '/one/two/three', '/one/two/three/', '/', '.', '']:
    print '"%s" : "%s"' % (path, os.path.split(path))

print '"%s" : "%s"' % (path, os.path.basename(path))

print '"%s" : "%s"' % (path, os.path.dirname(path))

paths = ['/one/two/three/four',
         '/one/two/threefold',
         '/one/two/three/']

print paths
print os.path.commonprefix(paths)

for parts in [ ('one', 'two', 'three'),
               ('/', 'one', 'two', 'three'),
               ('/one', '/two', '/three') ]:
    print parts, ':', os.path.join(*parts)

for path in [ 'one//two//three', 
              'one/./two/./three', 
              'one/../one/two/three ]:
    print path, ':', os.path.normpath(path)

for path in [ '.', '..', './one/two/three', '../one/two/three']:
    print '"%s" : "%s"' % (path, os.path.abspath(path))

for file in [ __file__, os.path.dirname(__file__), '/', './broken_link']:
    print 'File        :', file
    print 'Absolute    :', os.path.isabs(file)
    print 'Is File?    :', os.path.isfile(file)
    print 'Is Dir?     :', os.path.isdir(file)
    print 'Is Link?    :', os.path.islink(file)
    print 'Mountpoint? :', os.path.ismount(file)
    print 'Exists?     :', os.path.exists(file)
    print 'Link Exists?:', os.path.lexists(file)
    print

import os
os.getcwd()
os.path.abspath('')
os.path.abspath('.ssh')
os.path.abspath('/home/you/.ssh')
os.path.abspath('.ssh/../foo/')