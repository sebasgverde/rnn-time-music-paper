# takes the folder with the dataset pickles and make a latex table

import os
import pickle
import argparse

import music_geometry_eval

from scipy import stats

parser = argparse.ArgumentParser(
                    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--pickles_dir', type=str, default='~/experiments/generated/song_sets',
                    help='data directory containing dataset pickles')
args = parser.parse_args()


def avg(song):
	return sum(song) / float(len(song))


result = []

conjunct_melodic_motion = []
limited_macroharmony = []
centricity = []

span_size_lm= 32
span_size_centr = 32
minimal_song_size = 12


base_name = 'train'

# songs_list = pickle.load(open(args.pickles_dir + base_name + '/' + base_name + '_song_list_cleaned.p', "rb"))
songs_list = pickle.load(open(args.pickles_dir + '/' + base_name + '_song_list_cleaned.p', "rb"))

for song in songs_list:
	if len(song) >= minimal_song_size:
		conjunct_melodic_motion.append(music_geometry_eval.calculate_time_supported_conjunct_melodic_motion(song))
		limited_macroharmony.append(music_geometry_eval.calculate_time_supported_limited_macroharmony(song, span_size_lm,slide_windowsize=4))
		centricity.append(music_geometry_eval.calculate_time_supported_centricity(song, span_size_centr,slide_windowsize=4))

print avg(conjunct_melodic_motion)
print avg(limited_macroharmony)
print avg(centricity)

print '---------------------------------------------------'
print 'stats scipy'
print 'cmm'
cmm_stats = stats.describe(conjunct_melodic_motion)
print cmm_stats
print 'lm'
lm_stats = stats.describe(limited_macroharmony)
print lm_stats
print 'centr'
centr_stats = stats.describe(centricity)
print centr_stats

conjunct_melodic_motion_dev_std = stats.tstd(conjunct_melodic_motion)
limited_macroharmony_dev_std = stats.tstd(limited_macroharmony)
centricity_dev_std = stats.tstd(centricity)

print '\nlatex table with variance:'
print('{0:.2f} {1:.2f} & {2:.2f} {3:.2f} & {4:.2f} {5:.2f} \\\\').format(cmm_stats.mean, cmm_stats.variance, lm_stats.mean, lm_stats.variance, centr_stats.mean, centr_stats.variance)

print '\nlatex table with dev std:'
print('{0:.2f} $\\pm$ {1:.2f} & {2:.2f} $\\pm$ {3:.2f} & {4:.2f} $\\pm$ {5:.2f} \\\\').format(cmm_stats.mean, conjunct_melodic_motion_dev_std, lm_stats.mean, limited_macroharmony_dev_std, centr_stats.mean, centricity_dev_std)
