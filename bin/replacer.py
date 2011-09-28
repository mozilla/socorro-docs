#!/usr/bin/env python
"""
Makes sure all docs/*.rst files are properly right-stripped of whitespace

By: peterbe
"""

import os
from glob import glob
DIR = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'docs'))
assert glob(os.path.join(DIR, '*.rst'))

REPLACEMENTS = {
#  '[[SocorroCollector]]': ':ref:`collector-chapter`',
#  '[[SocorroMonitor]]': ':ref:`collector-chapter`',
#  '[[SocorroProcessor]]': ':ref:`processor-chapter`',
  '[[Requirements]]': ':ref:`requirements-chapter`',
  '[[DeferredJobStorage]]': ':ref:`deferredjobstorage-chapter`',
  '[[JsonDumpStorage]]': ':ref:`jsondumpstorage-chapter`',
  '[[ProcessedDumpStorage]]': ':ref:`processeddumpstorage-chapter`',
  '[[StandardJobStorage]]': ':ref:`standardjobstorage-chapter`',
  '[[ReportDatabaseDesign]]': ':ref:`reportdatabasedesign-chapter`',
  '[[TopCrashersBySignature]]': ':ref:`topcrashersbysignature-chapter`',
  '[[TopCrashersByUrl]]': ':ref:`topcrashersbyurl-chapter`',
  '[[SignatureGeneration]]': ':ref:`signaturegeneration-chapter`',
}
_SOCORRO_REPLACEMENTS = (
  'Collector', 'Monitor', 'Processor', 'Reporter', 'CommonConfig',
  'DatabaseSetup', 'DeferredCleanup', 'FileSystem', 'UI',
  'CrashMover', 'Server',
)
for each in _SOCORRO_REPLACEMENTS:
    REPLACEMENTS['[[Socorro%s]]' % each] = ':ref:`%s-chapter`' % each.lower()

import re
#wikilinks_maybe = re.compile(r'([^\[](Socorro[A-Z]\w+)\s[^\]])')
#wikilinks_maybe = re.compile(r'([^\[](Socorro[A-Z]\w+)[^\]])')
wikilinks_maybe = re.compile(r'([^\[](Socorro[A-Z]\w+)\.?\s[^\]])')
def wiki_replacer(s):
    whole, word = s.groups()
    return whole.replace(word, '[[%s]]' % word)

# E.g. `foo bar` but not not ``bar foo``
#singleticks = re.compile('[^`:]`[^`]+`[^`]')
singleticks = re.compile('\s`[^`_]+`\s')

def replace(content, filename):

    content = wikilinks_maybe.sub(wiki_replacer, content)
    content = singleticks.sub(lambda s: s.group().replace('`', '``'), content)

    for key in REPLACEMENTS:
        if key in content:
            content = content.replace(key, REPLACEMENTS[key])
        #else:
        #    _plain = key.replace('[[', '').replace(']]', '')
        #    if _plain in content:
        #        print "SUSPICIOUS", repr(_plain), "in", filename

    return content

def main(*args):
    for f in glob(os.path.join(DIR, '*.rst')):
        content = open(f).read()
        new_content = replace(content, f)
        if new_content is not None and content != new_content:
            print f
            open(f, 'w').write(new_content)

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(*sys.argv[:1]))
