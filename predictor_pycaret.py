# from predictor_class import SongPopularityPredictor
from pycaret.regression import *
import pandas as pd
import matplotlib.pyplot as plt
import shap

SAMPLE_SIZE = 1000
TEST_SIZE = 50
# IGNORE_FEATURES_LIST = ["track_id","artist_name","track_name"]
#


# segmenting dataset
def segment_dataset(data, random=False):
    if random is False:
        sample = data.iloc[0:SAMPLE_SIZE, :]
        test = data.iloc[SAMPLE_SIZE:SAMPLE_SIZE + TEST_SIZE, :]
    else:
        sample = data.sample(n=SAMPLE_SIZE)
        test = data.sample(n=TEST_SIZE)
    return sample, test

# create, train, and test network
def network(train_data, target, regression_alg):
    setup(data=train_data, target=target, session_id=100, ignore_low_variance=True)
    model = create_model(regression_alg)  # bayesian ridge is most optimal according to compare_models()
    return model

# plot actual and target popularity scores
def plot_accuracy(predictions, print_predictions=True):
    predictions['row_column'] = predictions.reset_index().index
    if print_predictions:
        print(predictions[['popularity', 'Label', 'row_column']].head(TEST_SIZE))
    predictions.plot(x='row_column', y=['popularity', 'Label'])    # Label represents predicted values
    plt.xlabel("# of samples")
    plt.ylabel("popularity")
    plt.legend(['actual', 'predicted'])
    plt.show()


if __name__ == '__main__':
    df = pd.read_csv('SpotifyFeatures.csv')
    target = 'popularity' #Target Feature
    regression_alg = 'dt'
    interpret = True

    train_data, test_data = segment_dataset(df, random=True)
    network = network(train_data, target, regression_alg) #If using python kernel/jupyter -> Must Run 'def network' block to reset model.
    predictions = predict_model(estimator=network, data=test_data)

    plot_accuracy(predictions)
    if interpret is True:
        interpret_model(network)
