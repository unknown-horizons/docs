import inspect
import os
import re

DOCS_PATH = os.path.dirname(os.path.abspath(__file__))

import init
from horizons.scenario.actions import ACTIONS
from horizons.scenario.conditions import CONDITIONS


def sphinx_section(text, level):
	return '%s\n%s\n' % (text, level * len(text))


def fix_doc(doc):
	indent = '   '
	if not doc:
		return ''

	doc = re.sub(r'^\s*@.*$', '', doc, flags=re.MULTILINE)
	doc = re.sub(r'#.*$', '', doc, flags=re.MULTILINE)

	return indent + doc.replace('\t', indent)


def get_args(func):
	args, varargs, _, _  = inspect.getargspec(func)

	result = ', '.join(args[1:])
	if varargs:
		if result:
			result += ', \*%s ' % varargs
		else:
			result = '\*%s' % varargs

	return result


def generate():
	with open(os.path.join(DOCS_PATH, 'docs/scenario.rst'), 'w') as f:
		f.write(sphinx_section('Scenario', '='))

		f.write(sphinx_section('Actions', '-'))
		for name, func in sorted(ACTIONS.registry.items()):
			f.write('.. function:: %s(%s)\n\n' % (name, get_args(func)))
			f.write('%s\n\n' % fix_doc(func.__doc__))

		f.write(sphinx_section('Conditions', '-'))
		for name, func in sorted(CONDITIONS.registry.items()):
			f.write('.. function:: %s(%s)\n\n' % (name, get_args(func)))
			f.write('%s\n\n' % fix_doc(func.__doc__))


if __name__ == '__main__':
	generate()
