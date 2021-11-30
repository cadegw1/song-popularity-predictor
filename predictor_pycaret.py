# from predictor_class import SongPopularityPredictor
from pycaret.regression import *
import pandas as pd
from IPython.display import display
import matplotlib.pyplot as plt

SAMPLE_SIZE = 1000
TEST_SIZE = 50

df = pd.read_csv('SpotifyFeatures.csv')
data = df.iloc[0:SAMPLE_SIZE-1, :]
test_data = df.iloc[SAMPLE_SIZE:SAMPLE_SIZE+TEST_SIZE-1, :]
del df

regression = setup(data=data, target='popularity', session_id=100,
                   ignore_low_variance=True, use_gpu=True, test_data=test_data)
# display(compare_models(include=['lr', 'br', 'svm', 'ada', 'rf']))
model = create_model('lr')
predictions = predict_model(model)

print("Predictions\r\n")
display(predictions['popularity'])
print("Test Data\r\n")
display(test_data['popularity'])

# plot actual and target popularity scores
test_data['row_column'] = test_data.reset_index().index
ax = test_data.plot(x='row_column', y='popularity')
predictions.plot(ax=ax, y='popularity')
plt.show()

# interpret_model(model)

