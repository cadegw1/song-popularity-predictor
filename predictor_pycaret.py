# from predictor_class import SongPopularityPredictor
from pycaret.regression import *
import pandas as pd
from IPython.display import display
import matplotlib.pyplot as plt

SAMPLE_SIZE = 1000

data = pd.read_csv('SpotifyFeatures.csv')
data = data.sample(SAMPLE_SIZE)
data['row_column'] = data.reset_index().index
ax = data.plot(x='row_column', y='popularity')

regression = setup(data=data, target='popularity', session_id=100, ignore_low_variance=True)
# display(compare_models(include=['lr', 'br', 'svm', 'ada', 'rf']))
model = create_model('rf')
predictions = predict_model(model)

predictions.plot(ax=ax, y='popularity')
plt.show()

# display(predictions)
# interpret_model(model)

