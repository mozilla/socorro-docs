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
  '[[SocorroCollector]]': ':ref:`collector-chapter`',
  '[[SocorroProcessor]]': ':ref:`processor-chapter`',
  '[[Requirements]]': ':ref:`requirements-chapter`',
}

import re
wikilinks_maybe = re.compile(r'([^\[](Socorro[A-Z]\w+)[^\]])')
def wiki_replacer(s):
    whole, word = s.groups()
    return whole.replace(word, '[[%s]]' % word)

def replace(content, filename):

    content = wikilinks_maybe.sub(wiki_replacer, content)

    for key in REPLACEMENTS:
        if key in content:
            content = content.replace(key, REPLACEMENTS[key])
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
