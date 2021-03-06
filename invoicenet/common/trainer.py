import time
from invoicenet.common.model import Model
import numpy as np


def train(model: Model):
    n_updates = 50000
    print_interval = 20
    best = float("inf")

    start = time.time()
    for i in range(n_updates):
        train_loss = model.train_batch()
        if not np.isfinite(train_loss):
            raise ValueError("NaN loss")

        if i % print_interval == 0:
            took = time.time() - start
            val_loss = model.val_batch()
            print("%05d/%05d %f batches/s train loss: %f val loss: %f" % (i, n_updates, (i + 1) / took, train_loss, val_loss))
            if not np.isfinite(val_loss):
                raise ValueError("NaN loss")
            if val_loss < best:
                model.save("best")

    return model
