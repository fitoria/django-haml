from django.core.management.base import BaseCommand, CommandError
#TODO:from hamlpy.hamlpy import Compiler
import os
import sys

def compile_haml():
    basedirs = []
    if os.environ.get('DJANGO_SETTINGS_MODULE'):
        from django.conf import settings
        basedirs.extend(settings.TEMPLATE_DIRS)
 
    basedirs = set(map(os.path.abspath, filter(os.path.isdir, basedirs)))

    if not basedirs:
        raise CommandError("This script should be run on your Django projecto or app tree")

    for basedir in basedirs:
        for dirpath, dirnames, filenames in os.walk(basedir):
            for f in filenames:
                if f.endswith('.hamlpy'):
                    sys.stderr.write('processing file %s in %s\n' % (f, dirpath))
                    pf = os.path.splitext(os.path.join(dirpath, f))[0]
    
                    cmd = 'hamlpy %s.hamlpy %s.html' % (pf, pf) 
                    os.system(cmd)

class Command(BaseCommand):
    '''This will compile all the haml templates into
    django templates'''

    help = 'Compiles all the haml templates into html'

    def handle(self, *args, **options):
        compile_haml()
