---
icon: lucide/file-plus-corner
---

# Custom

## Reader

Custom reader needs to inherit from the `XGMMLReader` class and implement the `_networkx_to` method:

```python
class XGMMLReader(Generic[T], ABC):
    def __init__(self, **kwargs):
        pass

    @abstractmethod
    def _networkx_to(self, graph: nx.MultiGraph, **kwargs) -> T:
        raise NotImplementedError()
```

This method is used to convert the `nx.MultiGraph` object instance read from XGMML into a custom class instance. The `kwargs` in the `read` method are passed to the `_networkx_to` method.

## Writer

Custom writer needs to inherit from the `XGMMLWriter` class and implement the `_to_networkx` method:

```python
class XGMMLWriter(Generic[T], ABC):
    def __init__(self, **kwargs):
        self._uuid = str(uuid.uuid4())
        self._element_maker = ElementMaker(nsmap=NAMESPACES)

    @abstractmethod
    def _to_networkx(self, graph: T, **kwargs) -> nx.MultiGraph:
        raise NotImplementedError()
```

This method is used to convert a custom class instance into an instance of the `nx.MultiGraph` object which can be written to an XGMML file. The `kwargs` in the `write` method are passed to the `_to_networkx` method.
