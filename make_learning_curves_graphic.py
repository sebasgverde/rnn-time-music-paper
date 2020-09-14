import pickle

# db_type = "control"
db_type = "interval"
# db_type = "db12"

rnn_type = "lstm"
# rnn_type = "gru"

checkpoint_dir = ["./models/training_checkpoints_","_" + rnn_type + "_units_"]
history_1 = pickle.load(open(checkpoint_dir[0] +db_type + checkpoint_dir[1]+ "128/learning_curve_info.p"))
history_2 = pickle.load(open(checkpoint_dir[0] +db_type + checkpoint_dir[1]+ "256/learning_curve_info.p"))
history_3 = pickle.load(open(checkpoint_dir[0] +db_type + checkpoint_dir[1]+ "512/learning_curve_info.p"))
history_4 = pickle.load(open(checkpoint_dir[0] +db_type + checkpoint_dir[1]+ "1024/learning_curve_info.p"))
history_5 = pickle.load(open(checkpoint_dir[0] +db_type + checkpoint_dir[1]+ "2048/learning_curve_info.p"))

import matplotlib.pyplot as plt
# plt.title(r'loss')
plt.xlabel('Epochs')
plt.ylabel('Loss (Cross Entropy)')

# plt.plot(history_1["epochs"][0:200], history_1["training_loss"][0:200], linewidth=2.0, label="128")
# plt.plot(history_2["epochs"][0:200], history_2["training_loss"][0:200], linewidth=2.0, label="256")
# plt.plot(history_3["epochs"][0:200], history_3["training_loss"][0:200], linewidth=2.0, label="512")
# plt.plot(history_4["epochs"][0:200], history_4["training_loss"][0:200], linewidth=2.0, label="1024")
# plt.plot(history_5["epochs"][0:200], history_5["training_loss"][0:200], linewidth=2.0, label="2048")

plt.plot(history_1["epochs"][0:200], history_1["validation_loss"][0:200], linewidth=2.0, label="128")
plt.plot(history_2["epochs"][0:200], history_2["validation_loss"][0:200], linewidth=2.0, label="256")
plt.plot(history_3["epochs"][0:200], history_3["validation_loss"][0:200], linewidth=2.0, label="512")
plt.plot(history_4["epochs"][0:200], history_4["validation_loss"][0:200], linewidth=2.0, label="1024")
plt.plot(history_5["epochs"][0:200], history_5["validation_loss"][0:200], linewidth=2.0, label="2048")

plt.legend()

# plt.show()
plt.savefig('learnig_curve_{}_{}.png'.format(db_type, rnn_type))
