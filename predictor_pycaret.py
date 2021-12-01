# from predictor_class import SongPopularityPredictor
from pycaret.regression import *
import pandas as pd
import matplotlib.pyplot as plt

SAMPLE_SIZE = 1000
TEST_SIZE = 50

# segmenting dataset
df = pd.read_csv('SpotifyFeatures.csv')
data = df.iloc[0:SAMPLE_SIZE, :]
test_data = df.iloc[SAMPLE_SIZE:SAMPLE_SIZE+TEST_SIZE, :]
del df

# create, train, and test network
regression = setup(data=data, target='popularity', session_id=100)
# compare_models()
model = create_model('br')  # bayesian ridge is most optimal according to compare_models()
predictions = predict_model(estimator=model, data=test_data)

# plot actual and target popularity scores
predictions['row_column'] = predictions.reset_index().index
ax = predictions.plot(x='row_column', y=['popularity', 'Label'])    # Label represents predicted values
plt.show()
print(predictions[['popularity', 'Label', 'row_column']].head(TEST_SIZE))

# interpret_model(model)

