# from predictor_class import SongPopularityPredictor
from pycaret.regression import *
import pandas as pd
from IPython.display import display

data = pd.read_csv('SpotifyFeatures.csv')
data = data.sample(100)
regression = setup(data=data, target='popularity', session_id=100)
print(models())
display(compare_models(include=['lr', 'br', 'svm', 'ada', 'rf']))
model = create_model('lr')
predictions = predict_model(model)
display(predictions)
# interpret_model(model)

