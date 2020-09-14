DB_TYPE=control
RNN_TYPE=lstm
EPOCHS=200
python rnnmusic/main.py --db_type $DB_TYPE --rnn_type $RNN_TYPE --rnn_units 128 --epochs $EPOCHS
python rnnmusic/main.py --db_type $DB_TYPE --rnn_type $RNN_TYPE --rnn_units 256 --epochs $EPOCHS
python rnnmusic/main.py --db_type $DB_TYPE --rnn_type $RNN_TYPE --rnn_units 512 --epochs $EPOCHS
python rnnmusic/main.py --db_type $DB_TYPE --rnn_type $RNN_TYPE --rnn_units 1024 --epochs $EPOCHS
python rnnmusic/main.py --db_type $DB_TYPE --rnn_type $RNN_TYPE --rnn_units 2048 --epochs $EPOCHS

RNN_TYPE=gru
python rnnmusic/main.py --db_type $DB_TYPE --rnn_type $RNN_TYPE --rnn_units 128 --epochs $EPOCHS
python rnnmusic/main.py --db_type $DB_TYPE --rnn_type $RNN_TYPE --rnn_units 256 --epochs $EPOCHS
python rnnmusic/main.py --db_type $DB_TYPE --rnn_type $RNN_TYPE --rnn_units 512 --epochs $EPOCHS
python rnnmusic/main.py --db_type $DB_TYPE --rnn_type $RNN_TYPE --rnn_units 1024 --epochs $EPOCHS
python rnnmusic/main.py --db_type $DB_TYPE --rnn_type $RNN_TYPE --rnn_units 2048 --epochs $EPOCHS

DB_TYPE=interval
RNN_TYPE=lstm
EPOCHS=200
python rnnmusic/main.py --db_type $DB_TYPE --rnn_type $RNN_TYPE --rnn_units 128 --epochs $EPOCHS
python rnnmusic/main.py --db_type $DB_TYPE --rnn_type $RNN_TYPE --rnn_units 256 --epochs $EPOCHS
python rnnmusic/main.py --db_type $DB_TYPE --rnn_type $RNN_TYPE --rnn_units 512 --epochs $EPOCHS
python rnnmusic/main.py --db_type $DB_TYPE --rnn_type $RNN_TYPE --rnn_units 1024 --epochs $EPOCHS
python rnnmusic/main.py --db_type $DB_TYPE --rnn_type $RNN_TYPE --rnn_units 2048 --epochs $EPOCHS

RNN_TYPE=gru
python rnnmusic/main.py --db_type $DB_TYPE --rnn_type $RNN_TYPE --rnn_units 128 --epochs $EPOCHS
python rnnmusic/main.py --db_type $DB_TYPE --rnn_type $RNN_TYPE --rnn_units 256 --epochs $EPOCHS
python rnnmusic/main.py --db_type $DB_TYPE --rnn_type $RNN_TYPE --rnn_units 512 --epochs $EPOCHS
python rnnmusic/main.py --db_type $DB_TYPE --rnn_type $RNN_TYPE --rnn_units 1024 --epochs $EPOCHS
python rnnmusic/main.py --db_type $DB_TYPE --rnn_type $RNN_TYPE --rnn_units 2048 --epochs $EPOCHS
#
DB_TYPE=db12
RNN_TYPE=lstm
EPOCHS=90
python rnnmusic/main.py --db_type $DB_TYPE --rnn_type $RNN_TYPE --rnn_units 128 --epochs $EPOCHS
python rnnmusic/main.py --db_type $DB_TYPE --rnn_type $RNN_TYPE --rnn_units 256 --epochs $EPOCHS
python rnnmusic/main.py --db_type $DB_TYPE --rnn_type $RNN_TYPE --rnn_units 512 --epochs $EPOCHS
python rnnmusic/main.py --db_type $DB_TYPE --rnn_type $RNN_TYPE --rnn_units 1024 --epochs $EPOCHS
python rnnmusic/main.py --db_type $DB_TYPE --rnn_type $RNN_TYPE --rnn_units 2048 --epochs $EPOCHS

RNN_TYPE=gru
python rnnmusic/main.py --db_type $DB_TYPE --rnn_type $RNN_TYPE --rnn_units 128 --epochs $EPOCHS
python rnnmusic/main.py --db_type $DB_TYPE --rnn_type $RNN_TYPE --rnn_units 256 --epochs $EPOCHS
python rnnmusic/main.py --db_type $DB_TYPE --rnn_type $RNN_TYPE --rnn_units 512 --epochs $EPOCHS
python rnnmusic/main.py --db_type $DB_TYPE --rnn_type $RNN_TYPE --rnn_units 1024 --epochs $EPOCHS
python rnnmusic/main.py --db_type $DB_TYPE --rnn_type $RNN_TYPE --rnn_units 2048 --epochs $EPOCHS
