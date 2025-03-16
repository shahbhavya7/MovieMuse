import pickle
import bz2



# Save compressed similarity.pkl
with bz2.BZ2File("similarity.pkl.bz2", "wb") as f:
    pickle.dump(similarityyy, f)

print("Pickle files compressed successfully!")
