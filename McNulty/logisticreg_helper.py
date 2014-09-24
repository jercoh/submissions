import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

def cartesian(arrays, out=None):
    """
    Generate a cartesian product of input arrays.

    Parameters
    ----------
    arrays : list of array-like
        1-D arrays to form the cartesian product of.
    out : ndarray
        Array to place the cartesian product in.

    Returns
    -------
    out : ndarray
        2-D array of shape (M, len(arrays)) containing cartesian products
        formed of input arrays.

    Examples
    --------
    >>> cartesian(([1, 2, 3], [4, 5], [6, 7]))
    array([[1, 4, 6],
           [1, 4, 7],
           [1, 5, 6],
           [1, 5, 7],
           [2, 4, 6],
           [2, 4, 7],
           [2, 5, 6],
           [2, 5, 7],
           [3, 4, 6],
           [3, 4, 7],
           [3, 5, 6],
           [3, 5, 7]])

    """

    arrays = [np.asarray(x) for x in arrays]
    dtype = arrays[0].dtype

    n = np.prod([x.size for x in arrays])
    if out is None:
        out = np.zeros([n, len(arrays)], dtype=dtype)

    m = n / arrays[0].size
    out[:,0] = np.repeat(arrays[0], m)
    if arrays[1:]:
        cartesian(arrays[1:], out=out[0:m,1:])
        for j in xrange(1, arrays[0].size):
            out[j*m:(j+1)*m,1:] = out[0:m,1:]
    return out

def isolate_and_plot(columns, data):
    i=0
    colors = 'rbgyrbgy'
    for column in columns:
        axes = plt.gca()
        axes.set_ylim([0,1])
        grouped = pd.pivot_table(data, values=['Won an Oscar'], rows=[column],
                                 aggfunc=np.mean)
        plt.plot(grouped.index.get_level_values(0), grouped['Won an Oscar'],
                    color=colors[int(i)])
        plt.xlabel(column)
        plt.ylabel("P(oscar=1)")
        plt.legend(column, loc='upper left', title='Variable')
        plt.title("Prob(oscar=1) isolating " + column)
        plt.show()
        i+=1

def train_logistic_regression(data, features, plot = False):
  train_cols = list(features)

  logit = sm.Logit(data['Won an Oscar'], data[features])

  # fit the model
  result = logit.fit()

  # instead of generating all possible values, we're going
  # to use an evenly spaced range of 10 values from the min to the max 
  new_values = []
  train_cols.pop()
  for feature in train_cols:
    values = np.linspace(data[feature].min(), data[feature].max(), 10)
    new_values.append(values)

  # enumerate all possibilities
  combos = pd.DataFrame(cartesian(new_values+[1.]))

  # recreate the columns
  combos.columns = features

  # make predictions on the enumerated dataset
  combos['Won an Oscar'] = result.predict(combos[features])

  # Plot
  if plot:
    isolate_and_plot(features, combos)

  return result

def calculate_precision(model, test_set, features):
  predictions = model.predict(test_set[features])
  result_df = pd.DataFrame()
  result_df['predictions'] = predictions
  result_df['observations'] = test_set['Won an Oscar'].values
  length = len(predictions)
  errors = 0.0
  for index, row in result_df.iterrows():
    if (row['observations'] == 1 and row['predictions'] >= 0.5) or (row['observations'] == 0 and row['predictions'] <= 0.5):
      pass
    else:
      errors += 1
    #print (row['observations'], row['predictions'])
  return 1-errors/length

class DataSet():
  def __init__(self, dataframe):
    rows = random.sample(dataframe.index, len(dataframe)*60/100)
    self.training_set = dataframe.ix[rows]
    cross_test_set = dataframe.drop(rows)
    cross_rows = random.sample(cross_test_set.index, len(cross_test_set)*50/100)
    self.cross_validation_set =cross_test_set.ix[cross_rows]
    self.test_set = cross_test_set.drop(rows)

    def train_regression(self, features):
      self.result = train_logistic_regression(self.training_set, features)

    def cross_validation(self):
      pass