#!/bin/bash

SAMPLE_PYTHON=./rnnmusic/generate.py

EXPERIMENT_PATH=~/exampleresearch/models/selected
OUTPUT_PATH=~/exampleresearch/experiments/generated_songs

mkdir $OUTPUT_PATH

NOTES_NUMBER=30

NUMBER_SONGS=100


DATABASE=control

TYPE_NET=gru
NUMBER_LAYERS=1024
mkdir $OUTPUT_PATH/${DATABASE}_${TYPE_NET}_${NUMBER_LAYERS}_notes_${NOTES_NUMBER}
python $SAMPLE_PYTHON --db_type $DATABASE --rnn_type $TYPE_NET --rnn_units $NUMBER_LAYERS --num_notes $NOTES_NUMBER --num_songs $NUMBER_SONGS --checkpoints_folder $EXPERIMENT_PATH --output_uri "$OUTPUT_PATH/${DATABASE}_${TYPE_NET}_${NUMBER_LAYERS}_notes_${NOTES_NUMBER}/${DATABASE}_${TYPE_NET}_${NUMBER_LAYERS}_notes_${NOTES_NUMBER}"
TYPE_NET=lstm
NUMBER_LAYERS=2048
mkdir $OUTPUT_PATH/${DATABASE}_${TYPE_NET}_${NUMBER_LAYERS}_notes_${NOTES_NUMBER}
python $SAMPLE_PYTHON --db_type $DATABASE --rnn_type $TYPE_NET --rnn_units $NUMBER_LAYERS --num_notes $NOTES_NUMBER --num_songs $NUMBER_SONGS --checkpoints_folder $EXPERIMENT_PATH --output_uri "$OUTPUT_PATH/${DATABASE}_${TYPE_NET}_${NUMBER_LAYERS}_notes_${NOTES_NUMBER}/${DATABASE}_${TYPE_NET}_${NUMBER_LAYERS}_notes_${NOTES_NUMBER}"



DATABASE=interval

TYPE_NET=gru
NUMBER_LAYERS=1024
mkdir $OUTPUT_PATH/${DATABASE}_${TYPE_NET}_${NUMBER_LAYERS}_notes_${NOTES_NUMBER}
python $SAMPLE_PYTHON --db_type $DATABASE --rnn_type $TYPE_NET --rnn_units $NUMBER_LAYERS --num_notes $NOTES_NUMBER --num_songs $NUMBER_SONGS --checkpoints_folder $EXPERIMENT_PATH --output_uri "$OUTPUT_PATH/${DATABASE}_${TYPE_NET}_${NUMBER_LAYERS}_notes_${NOTES_NUMBER}/${DATABASE}_${TYPE_NET}_${NUMBER_LAYERS}_notes_${NOTES_NUMBER}"
TYPE_NET=lstm
NUMBER_LAYERS=2048
mkdir $OUTPUT_PATH/${DATABASE}_${TYPE_NET}_${NUMBER_LAYERS}_notes_${NOTES_NUMBER}
python $SAMPLE_PYTHON --db_type $DATABASE --rnn_type $TYPE_NET --rnn_units $NUMBER_LAYERS --num_notes $NOTES_NUMBER --num_songs $NUMBER_SONGS --checkpoints_folder $EXPERIMENT_PATH --output_uri "$OUTPUT_PATH/${DATABASE}_${TYPE_NET}_${NUMBER_LAYERS}_notes_${NOTES_NUMBER}/${DATABASE}_${TYPE_NET}_${NUMBER_LAYERS}_notes_${NOTES_NUMBER}"



DATABASE=db12

TYPE_NET=gru
NUMBER_LAYERS=512
mkdir $OUTPUT_PATH/${DATABASE}_${TYPE_NET}_${NUMBER_LAYERS}_notes_${NOTES_NUMBER}
python $SAMPLE_PYTHON --db_type $DATABASE --rnn_type $TYPE_NET --rnn_units $NUMBER_LAYERS --num_notes $NOTES_NUMBER --num_songs $NUMBER_SONGS --checkpoints_folder $EXPERIMENT_PATH --output_uri "$OUTPUT_PATH/${DATABASE}_${TYPE_NET}_${NUMBER_LAYERS}_notes_${NOTES_NUMBER}/${DATABASE}_${TYPE_NET}_${NUMBER_LAYERS}_notes_${NOTES_NUMBER}"
TYPE_NET=lstm
NUMBER_LAYERS=2048
mkdir $OUTPUT_PATH/${DATABASE}_${TYPE_NET}_${NUMBER_LAYERS}_notes_${NOTES_NUMBER}
python $SAMPLE_PYTHON --db_type $DATABASE --rnn_type $TYPE_NET --rnn_units $NUMBER_LAYERS --num_notes $NOTES_NUMBER --num_songs $NUMBER_SONGS --checkpoints_folder $EXPERIMENT_PATH --output_uri "$OUTPUT_PATH/${DATABASE}_${TYPE_NET}_${NUMBER_LAYERS}_notes_${NOTES_NUMBER}/${DATABASE}_${TYPE_NET}_${NUMBER_LAYERS}_notes_${NOTES_NUMBER}"
