import itertools
import os

DOCS_PATH = os.path.dirname(os.path.abspath(__file__))

from init import db
from horizons.entities import Entities
from horizons.util.loaders.actionsetloader import ActionSetLoader

ActionSetLoader._find_action_sets('content/')

settler_names = dict(db('SELECT level, name FROM settler_level'))


header = """
Buildings Overview
==================

""".lstrip()


def get_image_url(building):
	gh = 'https://github.com/unknown-horizons/unknown-horizons/raw/master/'

	sets = ActionSetLoader.action_sets[building.action_sets.keys()[0]]
	path = sets.get('idle', sets.get('idle_full'))
	path = path[45].keys()[0]

	return gh + path
	

def sphinx_section(text, level):
	return '%s\n%s\n' % (text, level * len(text))


def generate_overview(buildings):
	buildings = sorted(buildings, key=lambda b: b.settler_level)

	with open(os.path.join(DOCS_PATH, 'docs/buildings.rst'), 'w') as f:
		f.write(header)
		for level, buildings in itertools.groupby(buildings, key=lambda b: b.settler_level):
			level_name = settler_names[level]
			f.write(sphinx_section(level_name, "'"))
			for b in buildings:
				f.write(sphinx_section(b.name, '`'))
				f.write('.. image:: %s\n' % get_image_url(b))


def main():
	data = []
	for b in Entities.buildings.itervalues():
		# skip paths (they have multiple images)
		if b.id in (15, 43):
			continue
		data.append(b)

	generate_overview(data)

    
if __name__ == '__main__':
	main()
