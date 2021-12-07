from pycaret.regression import *
import pandas as pd
import matplotlib.pyplot as plt

SAMPLE_SIZE = 2000
TEST_SIZE = 25


# Return list of track features from artist name and track name
def get_song_features(self, artist, track):
    track = self.client.search(q='artist:' + artist + ' track:' + track, type='track')
    track_id = track['tracks']['items'][0]['id']
    return self.get_track_features(track_id)


# Segmenting dataset
def segment_dataset(data, random=False):
    if random is False:
        sample = data.iloc[0:SAMPLE_SIZE, :]
        test = data.iloc[SAMPLE_SIZE:SAMPLE_SIZE + TEST_SIZE, :]
    else:
        sample = data.sample(n=SAMPLE_SIZE)
        test = data.sample(n=TEST_SIZE)
    return sample, test


# Create, train, and test network
def network(train_data, target, regression_alg):
    setup(data=train_data, target=target, session_id=100, ignore_low_variance=True)
    model = create_model(regression_alg)  # bayesian ridge is most optimal according to compare_models()
    return model


# Plot actual and target popularity scores
def plot_accuracy(predictions, labels, print_predictions=True, grid=False):
    plot_data = pd.DataFrame({'row_column': [*range(0, TEST_SIZE)]})
    plot_data['popularity'] = predictions[0]['popularity'].values
    for i in range(len(predictions)):
        plot_data[labels[i]] = predictions[i]['Label'].values
        if print_predictions:
            print(predictions[i][['popularity', 'Label']].head(TEST_SIZE))
    ax = plot_data.plot(x='row_column', y='popularity', linewidth=2)
    plot_data.plot(ax=ax, y=labels, linewidth=0.5)
    plt.xlabel("# of samples")
    plt.ylabel("popularity")
    plt.legend(['actual'] + labels)
    if grid:
        ax.set_xticks(*[range(0, TEST_SIZE)])
        plt.grid(visible=True)
    plt.show()


if __name__ == '__main__':
    df = pd.read_csv('SpotifyFeatures.csv')
    target = 'popularity'   # Target Feature
    regression_alg = ['br', 'rf', 'knn', 'dt']  # Must be a list of at least one element
    interpret = False

    predictions = []
    train_data, test_data = segment_dataset(df, random=True)
    for alg in regression_alg:
        net = network(train_data, target, alg)
        predictions.append(predict_model(estimator=net, data=test_data))

    plot_accuracy(predictions, regression_alg, print_predictions=False, grid=True)
    if interpret is True:
        interpret_model(network)

