# <center>Sequence Generation using Deep Recurrent Networks: A study case in music.</center>

# Printed anonymous version of the supplementary web page.

<center>Songs, code and datasets to replicate the research and the specific results of the paper</center>



[<center>Paper</center>]() [<center>Github</center>](https://github.com/sebasgverde/rnn-time-music-paper)

![](https://sebasgverde.github.io/rnn-time-music-paper/images/RNNtraining.jpg)
![](https://sebasgverde.github.io/rnn-time-music-paper/images/RNNsample.jpg)
## Abstract
Automatic generation of sequences has been a highly explored field in the last years. In particular, natural language processing and automatic music composition have gained importance due to the recent advances in machine learning and Neural Networks with intrinsic memory mechanisms such as Recurrent Neural Networks. This paper evaluates different types of memory mechanisms (memory cells) and analyses their performance in the field of music composition. The proposed approach considers music theory concepts such as transposition, and uses data transformations (embeddings) to introduce semantic meaning. The performance of the proposed architecture is automatically evaluated using quantitative metrics based in geometry to measure the tonality of a musical composition.


## Datasets, Model Weights and more

- [Datasets](https://www.dropbox.com/s/x0delcrq2jmo79i/data.zip?dl=0)
- [Network Weigths](https://www.dropbox.com/s/1gofckoiqrymsyh/selected_models.zip?dl=0)
- [Midi songs final models](https://www.dropbox.com/s/n2i1wgvm2bqky5p/generated_songs.zip?dl=0)

## Code
- [Paper scripts](https://github.com/sebasgverde/rnn-time-music-paper)
- [RNN time model 1.0](https://github.com/sebasgverde/rnnmusic/tree/nnmusic_model)
- [Library for midi manipulation 1.0](https://github.com/sebasgverde/music-geometry-eval)
- [Library for music evaluation 2.0](https://github.com/sebasgverde/music-geometry-eval)

## Demos
Click the images to see a youtube video

#### Final models representative songs
[![](https://sebasgverde.github.io/rnn-time-music-paper/images/generated_songs_demo_1.png)](https://youtu.be/FGUIEshh6WU)
[![](https://sebasgverde.github.io/rnn-time-music-paper/images/generated_songs_demo_2.png)](https://youtu.be/FGUIEshh6WU)
[![](https://sebasgverde.github.io/rnn-time-music-paper/images/generated_songs_demo_3.png)](https://youtu.be/FGUIEshh6WU)

## Research Replication
Note: All is done assuming you are in your home directory

#### Set the environment
Create a root folder and clone the scripts and model repositories:
```
mkdir exampleresearch
cd exampleresearch
git clone https://github.com/sebasgverde/rnnmusic/tree/nnmusic_model/
git clone -b 1.0 --single-branch https://github.com/sebasgverde/rnnmusic/tree/nnmusic_model/rnnmusic
```

create a virtual env using the requirements in rnnMusicSeqGenerator
```
mkvirtualenv exampleresearchmusic
pip install -r ~/exampleresearch/rnnMusicSeqGenerator/requirements.txt
```

For this two special libraries which were developed by me, you have two options, I recommend to install them also in the virtual env
```
pip install music-geometry-eval==2.0
pip install xxxx.xxxx==1.0
```

but you can also clone the repositories and use them as normal packages
```
git clone -b 2.0 --single-branch https://github.com/sebasgverde/music-geometry-eval.git
git clone -b 1.0 --single-branch https://xxxx.xxxx.git
```

#### Datasets
The mono-midi-transposition-dataset is the result of series of transformations over the mono-MusicXML-dataset
![](https://sebasgverde.github.io/rnn-time-music-paper/images/datasetflow.png)
Download the datasets:
```
mkdir data
wget -N https://www.dropbox.com/s/x0delcrq2jmo79i/data.zip?dl=1 -O data.zip
unzip data.zip -d data/
rm data.zip
```

<!-- You can also make some unit test to the pickles
```
python rnn-time-music-paper/paper_scripts/unittestdatacreation.py -v
``` -->

---

**Special Note**: If instead of replicating the research you want to specifically reproduce the paper results, you can just [skip](https://sebasgverde.github.io/rnn-time-music-paper/#models-metric-evaluation) the next two sections and download the network weights and the 600 generated songs.

```
mkdir models/
wget -N https://www.dropbox.com/s/1gofckoiqrymsyh/selected_models.zip?dl=1 -O model_weights.zip
unzip model_weights.zip -d ~/exampleresearch/models/selected
rm model_weights.zip
```

```
mkdir ~/exampleresearch/experiments/
wget -N https://www.dropbox.com/s/n2i1wgvm2bqky5p/generated_songs.zip?dl=1 -O generated_songs.zip
unzip generated_songs.zip -d ~/exampleresearch/experiments/
rm generated_songs.zip
```
---

#### Optimal number of units

Run the script which does 30 experiments (the 3 dataset variations, with the 2 cell types and 5 number of units), time will depend on the GPU hardware.
```
./rnn-time-music-paper/train.sh
```
This will create the folder models, with all the models separated in folders by dataset and cell type, inside the respective folders there will be the weights and a pickle with the model hyperparameters that are necesary to use the models at sampling, also pickles with information about the training history and learning curves graphs.

You can also create the learning curves with next script template using the learning_curve_info pickles
```
python rnn-time-music-paper/make_learning_curves_graphic.py
```
You will see a graph like this:

![](https://sebasgverde.github.io/rnn-time-music-paper/images/learnig_curve_control_lstm.png)

#### Generating songs


Now that we have reduced the problem to 6 models (best learning curve for each pair dataset-cell), we will generate 100 songs with each model, always using the same seed and size (just modify the generatesongs script with the appropriate units number)
```
mkdir ~/exampleresearch/experiments/
mkdir ~/exampleresearch/experiments/generated_songs
./rnn-time-music-paper/generatesongs.sh
```
This will create 6 folders, each with 200 files, the 100 songs as midi and as pickle file with the song as a list.
![](https://sebasgverde.github.io/rnn-time-music-paper/images/song_generated_files.png)

#### Models metric evaluation
The next step is to use the music_geometry_eval library to test the tonality of the models. This script will apply 3 quantitative metrics (Conjunct Melody Motion, Limited Macroharmony and Centricity) to each set of 100 songs. The output file will have 6 tables with all the songs, different latex tables with summary information, the list of the most representative song of each model (the song whose metrics have the lower euclidean distance to the mean of the 100) and finally, a latex table with the mean and standard deviation for each metric in each model for each 100 song set.
```
python rnn-time-music-paper/eval_n_songs.py --generated_dir ~/exampleresearch/experiments/generated_songs > ~/exampleresearch/experiments/metrics_eval_100_songs.txt
```
After that, create a folder and move each of the most representative songs there, this script will generate the latex code for the table with those metrics
```
python rnn-time-music-paper/eval_most_rep_songs.py --songs_folder ~/exampleresearch/experiments/rep_songs > ~/exampleresearch/experiments/metrics_eval_most_repres_songs.txt
```

#### Analysing tonality of the models quantitatively

In order to analyze it, it is necessary to have a baseline applying the metrics to the dataset:
```
python rnn-time-music-paper/dataset_metric_eval.py --pickles_dir ~/exampleresearch/data > ~/exampleresearch/experiments/metrics_eval_dataset.txt
```
Once you compile the latex tables, they will look like this:

#### Dataset
![](https://sebasgverde.github.io/rnn-time-music-paper/images/metric_table_dataset.png)

#### Models
![](https://sebasgverde.github.io/rnn-time-music-paper/images/metric_table_models.png)

#### Most Representative Songs
![](https://sebasgverde.github.io/rnn-time-music-paper/images/metric_table_most_rep_songs.png)

Now, you can use the scripts in template_scripts, to transform the midi files in mp3, wav and jpg, however, the images aren't very flexible from console, seem there's no way to export to png from console indicating the dimensions, so I recommend:

- you can use mid_2_wav and mid_2_mp3 to get the audios
- open the midis in musescore, change the dimension in design->page settings
- save as .mscz
- export as png (even so the console doesn't work, export each png manually)

<!-- ### Other scripts
The scripts in scripts_for_supercomputing are modified versions of the training script for 6 of the experiments which I trained in a cluster environment in HPC centre [Apolo](http://www.eafit.edu.co/centros/apolo/Paginas/technical-specification.aspx). It works with slurm as cluster management and job scheduling system, so also the slurm scripts are provided. -->
