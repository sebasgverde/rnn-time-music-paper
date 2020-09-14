# takes the folder with the n generated songs as pickles and make a latex table

import os
import pickle
import argparse

import music_geometry_eval

from scipy import stats
from scipy.spatial import distance

parser = argparse.ArgumentParser(
                    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--generated_dir', type=str, default='~/experiments/generated/song_sets',
                    help='data directory containing generated songs')
args = parser.parse_args()
result = {}

m1 = 'm1'
m2 = 'm2'
m3 = 'm3'

# result = []

best_song_list = []
most_representative_song_list = []
span_size_lm= 32
span_size_centr = 32

sets_folder = args.generated_dir

# sets_folder = '~/experiments/generated/song_sets'
# sets_folder = '~/experiments/generated_2/20_notes'
# sets_folder = '~/experiments/generated_2/30_notes'

setslist=os.listdir(sets_folder)

for folder in setslist:
    songs_folder = sets_folder + '/' + folder

    conjunct_melodic_motion = []
    limited_macroharmony = []
    centricity = []
    general_tonality = []
    euclidean_distance = []

    filelist=os.listdir(songs_folder)
    i = 0

    model_table = []
    for song in filelist: # filelist[:] makes a copy of filelist.
        # import pdb; pdb.set_trace()
        if (song.endswith(".p")):
            song_array = pickle.load(open(songs_folder + '/' + song, "rb"))

            conjunct_melodic_motion.append(music_geometry_eval.calculate_time_supported_conjunct_melodic_motion(song_array))
            limited_macroharmony.append(music_geometry_eval.calculate_time_supported_limited_macroharmony(song_array, span_size_lm,slide_windowsize=4))
            centricity.append(music_geometry_eval.calculate_time_supported_centricity(song_array, span_size_centr,slide_windowsize=4))
            general_tonality.append(music_geometry_eval.calculate_general_tonality(conjunct_melodic_motion[i], limited_macroharmony[i], centricity[i]))

            # conjunct_melodic_motion.append(22)
            # limited_macroharmony.append(22)
            # centricity.append(22)
            # general_tonality.append(22)

            model_table.append({'string' :('{0} {1} {2:.2f} {3:.2f} {4:.2f}').format(i, song, conjunct_melodic_motion[i], limited_macroharmony[i], centricity[i])})
            model_table[i]['general_tonality'] = general_tonality[i]
            i+=1


	# for string in model_table:
	# 	print string


	# print '---------------------------------------------------'
	# print 'stats scipy'
	# print 'cmm'
    print folder
    cmm_stats = stats.describe(conjunct_melodic_motion)
    # cmm_stats['std_dev'] = stats.tstd(conjunct_melodic_motion)
    # print cmm_stats
    # print 'lm'
    lm_stats = stats.describe(limited_macroharmony)
    # print lm_stats
    # print 'centr'
    centr_stats = stats.describe(centricity)
    # print centr_stats

    elements = folder.split('_')
    database = elements[0]
    cell_type = elements[1]

    if not database in result:
    	result[database]={}
    if not cell_type in result[database]:
    	result[database][cell_type] = {}

	# print('{0} {1} Average note: {2}'.format(database, cell_type, music_geometry_eval.eval_song(song_array)))

	result[database][cell_type][m1] = {}
	result[database][cell_type][m2] = {}
	result[database][cell_type][m3] = {}

	result[database][cell_type][m1]['desc_stats'] = cmm_stats
	result[database][cell_type][m2]['desc_stats'] = lm_stats
	result[database][cell_type][m3]['desc_stats']= centr_stats
	result[database][cell_type][m1]['std_dev'] = stats.tstd(conjunct_melodic_motion)
	result[database][cell_type][m2]['std_dev'] = stats.tstd(limited_macroharmony)
	result[database][cell_type][m3]['std_dev']= stats.tstd(centricity)

	#
	# Find best song
	#
	# pos of the best song (minimal value in tonality)
	# it is actually difficult to define a best song, i take better the most representative
	# but keep this code if I find a way of best song in the future for optimization
	# for now this all is just descriptive
	#
	# import pdb
	# pdb.set_trace()
	val, best_song_pos = min((val, best_song_pos) for (best_song_pos, val) in enumerate(general_tonality))
	i= best_song_pos

	best_song_list.append(model_table[best_song_pos])

	result[database][cell_type]['best_song'] = {}
	result[database][cell_type]['best_song'][m1] = conjunct_melodic_motion[best_song_pos]
	result[database][cell_type]['best_song'][m2] = limited_macroharmony[best_song_pos]
	result[database][cell_type]['best_song'][m3] = centricity[best_song_pos]

	#
	# Find most representative song
	#

	mean_metrics_point = (cmm_stats.mean, lm_stats.mean, centr_stats.mean)
	for i in range(len(model_table)):
		current_metric_point = (conjunct_melodic_motion[i], limited_macroharmony[i], centricity[i])
		euclidean_distance.append(distance.euclidean(mean_metrics_point, current_metric_point))
		model_table[i]['euclidean_distance'] = euclidean_distance[i]


	val, most_representative_pos = min((val, most_representative_pos) for (most_representative_pos, val) in enumerate(euclidean_distance))
	i= most_representative_pos

	most_representative_song_list.append(model_table[most_representative_pos])

	result[database][cell_type]['most_rep_song'] = {}
	result[database][cell_type]['most_rep_song'][m1] = conjunct_melodic_motion[most_representative_pos]
	result[database][cell_type]['most_rep_song'][m2] = limited_macroharmony[most_representative_pos]
	result[database][cell_type]['most_rep_song'][m3] = centricity[most_representative_pos]


	# import pdb
	# pdb.set_trace()
	print('\n{0} table').format(folder)
	print('{0} {1} {2} {3} {4}').format('i', 'song name', 'CMM', 'LM', 'CENTR')
	order_model_table = model_table.sort(key=lambda x: x['euclidean_distance'])
	for table in model_table:
		print table


print '\nlatex table mean:'
partial_result = result['control']
print('control & {0:.2f} {1:.2f} {2:.2f} & {3:.2f} {4:.2f} {5:.2f} \\\\').format(partial_result['lstm'][m1]['desc_stats'].mean, partial_result['lstm'][m2]['desc_stats'].mean,partial_result['lstm'][m3]['desc_stats'].mean, partial_result['gru'][m1]['desc_stats'].mean,partial_result['gru'][m2]['desc_stats'].mean, partial_result['gru'][m3]['desc_stats'].mean)


partial_result = result['interval']
print('interval  & {0:.2f} {1:.2f} {2:.2f} & {3:.2f} {4:.2f} {5:.2f} \\\\').format(partial_result['lstm'][m1]['desc_stats'].mean, partial_result['lstm'][m2]['desc_stats'].mean, partial_result['lstm'][m3]['desc_stats'].mean, partial_result['gru'][m1]['desc_stats'].mean, partial_result['gru'][m2]['desc_stats'].mean, partial_result['gru'][m3]['desc_stats'].mean)
partial_result = result['db12']
print('db12  & {0:.2f} {1:.2f} {2:.2f} & {3:.2f} {4:.2f} {5:.2f} \\\\').format(partial_result['lstm'][m1]['desc_stats'].mean, partial_result['lstm'][m2]['desc_stats'].mean, partial_result['lstm'][m3]['desc_stats'].mean, partial_result['gru'][m1]['desc_stats'].mean, partial_result['gru'][m2]['desc_stats'].mean, partial_result['gru'][m3]['desc_stats'].mean)

print '\nlatex table variance:'
partial_result = result['control']
print('control & {0:.2f} {1:.2f} {2:.2f} & {3:.2f} {4:.2f} {5:.2f} \\\\').format(partial_result['lstm'][m1]['desc_stats'].variance, partial_result['lstm'][m2]['desc_stats'].variance, partial_result['lstm'][m3]['desc_stats'].variance, partial_result['gru'][m1]['desc_stats'].variance, partial_result['gru'][m2]['desc_stats'].variance, partial_result['gru'][m3]['desc_stats'].variance)
partial_result = result['interval']
print('interval  & {0:.2f} {1:.2f} {2:.2f} & {3:.2f} {4:.2f} {5:.2f} \\\\').format(partial_result['lstm'][m1]['desc_stats'].variance, partial_result['lstm'][m2]['desc_stats'].variance, partial_result['lstm'][m3]['desc_stats'].variance, partial_result['gru'][m1]['desc_stats'].variance, partial_result['gru'][m2]['desc_stats'].variance, partial_result['gru'][m3]['desc_stats'].variance)
partial_result = result['db12']
print('db12  & {0:.2f} {1:.2f} {2:.2f} & {3:.2f} {4:.2f} {5:.2f} \\\\').format(partial_result['lstm'][m1]['desc_stats'].variance, partial_result['lstm'][m2]['desc_stats'].variance, partial_result['lstm'][m3]['desc_stats'].variance, partial_result['gru'][m1]['desc_stats'].variance, partial_result['gru'][m2]['desc_stats'].variance, partial_result['gru'][m3]['desc_stats'].variance)

print '\nlatex table standard deviation:'
partial_result = result['control']
print('control & {0:.2f} {1:.2f} {2:.2f} & {3:.2f} {4:.2f} {5:.2f} \\\\').format(partial_result['lstm'][m1]['std_dev'], partial_result['lstm'][m2]['std_dev'], partial_result['lstm'][m3]['std_dev'], partial_result['gru'][m1]['std_dev'], partial_result['gru'][m2]['std_dev'], partial_result['gru'][m3]['std_dev'])
partial_result = result['interval']
print('interval  & {0:.2f} {1:.2f} {2:.2f} & {3:.2f} {4:.2f} {5:.2f} \\\\').format(partial_result['lstm'][m1]['std_dev'], partial_result['lstm'][m2]['std_dev'], partial_result['lstm'][m3]['std_dev'], partial_result['gru'][m1]['std_dev'], partial_result['gru'][m2]['std_dev'], partial_result['gru'][m3]['std_dev'])
partial_result = result['db12']
print('db12  & {0:.2f} {1:.2f} {2:.2f} & {3:.2f} {4:.2f} {5:.2f} \\\\').format(partial_result['lstm'][m1]['std_dev'], partial_result['lstm'][m2]['std_dev'], partial_result['lstm'][m3]['std_dev'], partial_result['gru'][m1]['std_dev'], partial_result['gru'][m2]['std_dev'], partial_result['gru'][m3]['std_dev'])


print '\nlatex table best songs:'
partial_result = result['control']
print('control & {0:.2f} {1:.2f} {2:.2f} & {3:.2f} {4:.2f} {5:.2f} \\\\').format(partial_result['lstm']['best_song'][m1], partial_result['lstm']['best_song'][m2], partial_result['lstm']['best_song'][m3], partial_result['gru']['best_song'][m1], partial_result['gru']['best_song'][m2], partial_result['gru']['best_song'][m3])
partial_result = result['interval']
print('interval  & {0:.2f} {1:.2f} {2:.2f} & {3:.2f} {4:.2f} {5:.2f} \\\\').format(partial_result['lstm']['best_song'][m1], partial_result['lstm']['best_song'][m2], partial_result['lstm']['best_song'][m3], partial_result['gru']['best_song'][m1], partial_result['gru']['best_song'][m2], partial_result['gru']['best_song'][m3])
partial_result = result['db12']
print('db12  & {0:.2f} {1:.2f} {2:.2f} & {3:.2f} {4:.2f} {5:.2f} \\\\').format(partial_result['lstm']['best_song'][m1], partial_result['lstm']['best_song'][m2], partial_result['lstm']['best_song'][m3], partial_result['gru']['best_song'][m1], partial_result['gru']['best_song'][m2], partial_result['gru']['best_song'][m3])

print '\nlatex table most representative songs:'
partial_result = result['control']
print('control & {0:.2f} {1:.2f} {2:.2f} & {3:.2f} {4:.2f} {5:.2f} \\\\').format(partial_result['lstm']['most_rep_song'][m1], partial_result['lstm']['most_rep_song'][m2], partial_result['lstm']['most_rep_song'][m3], partial_result['gru']['most_rep_song'][m1], partial_result['gru']['most_rep_song'][m2], partial_result['gru']['most_rep_song'][m3])
partial_result = result['interval']
print('interval  & {0:.2f} {1:.2f} {2:.2f} & {3:.2f} {4:.2f} {5:.2f} \\\\').format(partial_result['lstm']['most_rep_song'][m1], partial_result['lstm']['most_rep_song'][m2], partial_result['lstm']['most_rep_song'][m3], partial_result['gru']['most_rep_song'][m1], partial_result['gru']['most_rep_song'][m2], partial_result['gru']['most_rep_song'][m3])
partial_result = result['db12']
print('db12  & {0:.2f} {1:.2f} {2:.2f} & {3:.2f} {4:.2f} {5:.2f} \\\\').format(partial_result['lstm']['most_rep_song'][m1], partial_result['lstm']['most_rep_song'][m2], partial_result['lstm']['most_rep_song'][m3], partial_result['gru']['most_rep_song'][m1], partial_result['gru']['most_rep_song'][m2], partial_result['gru']['most_rep_song'][m3])

print '\nbest songs:'
for string in best_song_list:
	print string

print '\nmost rep songs:'
for string in most_representative_song_list:
	print string

print '\nlatex table mean and std dev:'
print '\\multirow{ 2}{*}{CMM} &  '
partial_result = result['control']
print('control & {0:.2f} $\\pm$ {1:.2f} & {2:.2f} $\\pm$ {3:.2f} \\\\').format(partial_result['lstm'][m1]['desc_stats'].mean, partial_result['lstm'][m1]['std_dev'], partial_result['gru'][m1]['desc_stats'].mean, partial_result['gru'][m1]['std_dev'])
partial_result = result['interval']
print('&interval  & {0:.2f} $\\pm$ {1:.2f} & {2:.2f} $\\pm$ {3:.2f} \\\\').format(partial_result['lstm'][m1]['desc_stats'].mean, partial_result['lstm'][m1]['std_dev'], partial_result['gru'][m1]['desc_stats'].mean, partial_result['gru'][m1]['std_dev'])
partial_result = result['db12']
print('&db12  & {0:.2f} $\\pm$ {1:.2f} & {2:.2f} $\\pm$ {3:.2f} \\\\').format(partial_result['lstm'][m1]['desc_stats'].mean, partial_result['lstm'][m1]['std_dev'], partial_result['gru'][m1]['desc_stats'].mean, partial_result['gru'][m1]['std_dev'])
print '\\hline'
print '\\multirow{ 3}{*}{LM} &  '
partial_result = result['control']
print('control & {0:.2f} $\\pm$ {1:.2f} & {2:.2f} $\\pm$ {3:.2f} \\\\').format(partial_result['lstm'][m2]['desc_stats'].mean, partial_result['lstm'][m2]['std_dev'], partial_result['gru'][m2]['desc_stats'].mean, partial_result['gru'][m2]['std_dev'])
partial_result = result['interval']
print('&interval  & {0:.2f} $\\pm$ {1:.2f} & {2:.2f} $\\pm$ {3:.2f} \\\\').format(partial_result['lstm'][m2]['desc_stats'].mean, partial_result['lstm'][m2]['std_dev'], partial_result['gru'][m2]['desc_stats'].mean, partial_result['gru'][m2]['std_dev'])
partial_result = result['db12']
print('&db12  & {0:.2f} $\\pm$ {1:.2f} & {2:.2f} $\\pm$ {3:.2f} \\\\').format(partial_result['lstm'][m2]['desc_stats'].mean, partial_result['lstm'][m2]['std_dev'], partial_result['gru'][m2]['desc_stats'].mean, partial_result['gru'][m2]['std_dev'])
print '\\hline'
print '\\multirow{ 3}{*}{CENTR} &  '
partial_result = result['control']
print('control & {0:.2f} $\\pm$ {1:.2f} & {2:.2f} $\\pm$ {3:.2f} \\\\').format(partial_result['lstm'][m3]['desc_stats'].mean, partial_result['lstm'][m3]['std_dev'], partial_result['gru'][m3]['desc_stats'].mean, partial_result['gru'][m3]['std_dev'])
partial_result = result['interval']
print('&interval  & {0:.2f} $\\pm$ {1:.2f} & {2:.2f} $\\pm$ {3:.2f} \\\\').format(partial_result['lstm'][m3]['desc_stats'].mean, partial_result['lstm'][m3]['std_dev'], partial_result['gru'][m3]['desc_stats'].mean, partial_result['gru'][m3]['std_dev'])
partial_result = result['db12']
print('&db12  & {0:.2f} $\\pm$ {1:.2f} & {2:.2f} $\\pm$ {3:.2f} \\\\').format(partial_result['lstm'][m3]['desc_stats'].mean, partial_result['lstm'][m3]['std_dev'], partial_result['gru'][m3]['desc_stats'].mean, partial_result['gru'][m3]['std_dev'])
print '\\hline'
