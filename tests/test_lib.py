from Pipstoolbox.lib import get_model
# import keras
def test_model():
    model = get_model(5,5,5)
    layers = model.layers
    assert len(layers) == 3
    # assert type(model) == keras.engine.sequential.Sequential