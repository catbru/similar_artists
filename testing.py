#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import sys
import spotipy

''' shows the albums and tracks for a given artist.
'''


def get_artist(name):
	results = sp.search(q='artist:' + name, type='artist')
	items = results['artists']['items']
	print items[0]['name']
	print items[0]['id']
	if len(items) > 0:
		return items[0]
	else:
		return None

def show_artists_related(id):
	i = 0
	relateds = sp.artist_related_artists(artist['id'])
	for artista in relateds['artists']:
		i = i + 1
		print str(i) + ' ' + artista['name'].encode('utf-8')


if __name__ == '__main__':
	sp = spotipy.Spotify()
	sp.trace = False

	#if len(sys.argv) < 2:
	#    print(('Usage: {0} artist name'.format(sys.argv[0])))
	#else:
	name = 'Joan Miquel Oliver'
	artist = get_artist(name)
	show_artists_related(artist)
	#show_artist(artist)