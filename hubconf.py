dependencies = ['torch']
from timm054.models import registry

globals().update(registry._model_entrypoints)
