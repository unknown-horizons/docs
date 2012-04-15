import itertools
import os
import sys

DOCS_PATH = os.path.dirname(os.path.abspath(__file__))

from init import db
from horizons.entities import Entities
from horizons.util.loaders.actionsetloader import ActionSetLoader

ActionSetLoader._find_action_sets('content/')

settler_names = dict(db('SELECT level, name FROM settler_level'))

global gh, used_res_ids
gh = 'https://github.com/unknown-horizons/unknown-horizons/raw/master/'
#gh = 'file://localhost/{path}/'.format(path=os.path.abspath(sys.argv[1]))
used_res_ids = set()

header = """
Buildings Overview
==================

""".lstrip()


def get_image_url(building):
	sets = ActionSetLoader.action_sets[building.action_sets.keys()[0]]
	path = sets.get('idle', sets.get('idle_full'))
	path = path[45].keys()[0]

	return gh + path
	

def sphinx_section(text, level):
	return '%s\n%s\n' % (text, level * len(text))

def get_res_icon_path(res_id):
	return gh + 'content/gui/icons/resources/32/{id:03d}.png'.format(id=res_id)

def get_building_cost_list(building):
	for r in building.costs.iterkeys():
		used_res_ids.add(r)
	building.costs[-99] = building.running_costs or 0
	building.costs[-98] = building.running_costs_inactive or 0
	building.costs[980] = building.size[0]
	building.costs[981] = building.size[1]
	sep  = '+' + '+'.join('--------' for (_, _) in building.costs.iteritems()) + '+\n'
	ret  = sep
	ret += '| ' + ' | '.join('|r%03d|' % r for (r, _) in sorted(building.costs.items())) + ' |\n'
	ret += sep
	ret += '| ' + ' | '.join( '%6d'  % a for (_, a) in sorted(building.costs.items())) + ' |\n'
	ret += sep
	return ret + '\n'

def generate_overview(buildings):
	buildings = sorted(buildings, key=lambda b: b.settler_level)

	with open(os.path.join(DOCS_PATH, 'docs/buildings.rst'), 'w') as f:
		f.write(header)
		for level, buildings in itertools.groupby(buildings, key=lambda b: b.settler_level):
			level_name = settler_names[level]
			f.write(sphinx_section(level_name, "'"))
			for b in buildings:
				f.write(sphinx_section(b.name, '`'))
				f.write('%s\n\n' % b.tooltip_text)
				if hasattr(b, 'component_templates'):
					produced_res = set()
					for component in b.component_templates:
						for k, v in component.iteritems():
							if 'ProducerComponent' in k:
								for _, line in component[k]['productionlines'].iteritems():
									output = line.get('produces')
									if output:
										produced_res.add(output[0][0])
										used_res_ids.add(output[0][0])
								if produced_res:
									f.write('Produces:\n')
									for id in produced_res:
										f.write('|r{id:03d}|\n'.format(id=id))
									f.write('\n')
				f.write(get_building_cost_list(b))
				f.write('.. image:: %s\n\n' % get_image_url(b))
		f.write('\n' * 3)

		# create replace rules for all required resource icons
		for id in used_res_ids:
			f.write('.. |r{id:03d}| image:: {path}\n'.format(id=id, path=get_res_icon_path(id)))
		f.write('.. |r-99| image:: {path}\n'.format(path=gh+'content/gui/icons/resources/negative32.png'))
		f.write('.. |r-98| image:: {path}\n'.format(path=gh+'content/gui/icons/resources/zzz32.png'))
		f.write('.. |r980| replace:: x\n')
		f.write('.. |r981| replace:: y\n')


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
