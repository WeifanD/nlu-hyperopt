from hyperopt import hp

# Default search space: Try different numbers of training epochs.
search_space = {"epochs": hp.qloguniform("epochs", 0, 4.7, 2)
    }
