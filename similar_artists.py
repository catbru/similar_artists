#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import io
import sys
import spotipy

''' script base per treure una xarxa de relacions entre artistes en base un a spotify
'''
#
#

def get_relateds(artista):
	""" torna dict {id:'name'} dels artistes relacionats amb artista """
	current_artistes = {}
	results = sp.search(q='artist:' + artista, type='artist')

	items = results['artists']['items']
	if len(items) > 0:
		relateds = sp.artist_related_artists(items[0]['id'])
		for item in relateds['artists']:
			current_artistes.update({item['id']:item['name']})
#	else:
#		raise ValueError('cerca artista sense cap resultat')
	return current_artistes


def merge_dict_uniques(desti, origen):
	""" fem merge dorigen a desti dels valors que no son a desti """
	desti_keys = desti.keys()
	for key in origen.keys():
		if key not in desti_keys:
			desti.update({key:origen[key]})
		else:
			continue
	return desti

def merge_array_uniques(desti, origen):
	""" fem merge dorigen a desti dels valors que no son a desti """
	for key in origen:
		if key not in desti:
			desti.append(key)
		else:
			continue
	return desti



def get_relations(artista, relacionats):
	""" recorre els relacionats i escriu la relacio artista(id) -> relacionat(id) a relacions """
	current_relations = []
	for relacionat in relacionats:
		current_relations.append({artista:relacionat})
	return current_relations


def get_artist(name):
	results = sp.search(q='artist:' + name, type='artist')
	items = results['artists']['items']
	if len(items) > 0:
		row = {items[0]['id']:items[0]['name']}
		return row
#	else:
#		raise ValueError('cerca artista sense cap resultat')

def dict_to_csv(name, dicc):
	csv = io.open(name, "a", encoding='utf8')
	for key in dicc.keys():
		csv.write(key + "," + dicc[key].encode('utf-8') +"\n")
	csv.close()

def array_to_csv(name, array):
	csv = io.open(name, "a", encoding='utf8')
	for key in array:
		csv.write(key.keys()[0]+ "," + key(key.keys()[0]).encode('utf-8') +"\n")
	csv.close()


if __name__ == '__main__':

	sp = spotipy.Spotify()
	sp.trace = False

	artistes = {}
	""" {id:'name'} """

	relacions = []
	""" {id:id} """

	#if len(sys.argv) < 2:
	#    print(('Usage: {0} artist name'.format(sys.argv[0])))
	#else:
	name = 'Joan Miquel Oliver'
	artistes.update(get_artist(name))	
	
	dones = []
	
	i = 0
	
	limit = 1000
	
	while len(dones) < limit:
		root_keys = artistes.keys()
		for key in list(root_keys):
		
			i = i + 1
		
			if key not in dones:	
		
				nous_artistes = get_relateds(artistes[key])
		
		
				noves_relacions = get_relations(key,nous_artistes.keys())
		
				relacions = merge_array_uniques(relacions,noves_relacions)
		
				dones.append(key)
			
				artistes = merge_dict_uniques(artistes,nous_artistes)
		
			if len(dones) > limit:
				break
	

	print('---NODES-----')
	for key in artistes.keys():
			print(key + "," + artistes[key])
	print('\n')
	print('\n')
	print('---EDGES-----')
	for key in relacions:
		for clau in key.keys():
			clau = clau
		for value in key.values():
			value = value
		print(clau+ "," + value)
