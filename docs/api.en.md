# API

## Reader

### Object

Create an instance of the `XGMMLReader` object. Currently available:

- `NetworkxXGMMLReader`
- `IgraphXGMMLReader`

For example, using `NetworkxXGMMLReader`:

```python
import networkx as nx
from xgmml.reader.networkx_xgmml_reader import NetworkxXGMMLReader

reader = NetworkxXGMMLReader()
```

### Method

Read the XGMML file through the `read` method of the instance:

```python
def read(
    self,
    xgmml_path: str,
    **kwargs
) -> nx.MultiGraph
```

The result is an instance of the `nx.MultiGraph` object.

## Writer

### Object

Create an instance of the `XGMMLWriter` object. Currently available:

- `NetworkxXGMMLWriter`
- `IgraphXGMMLWriter`

For example, using `NetworkxXGMMLWriter`:

```python
import networkx as nx
from xgmml.writer.networkx_xgmml_writer import NetworkxXGMMLWriter

writer = NetworkxXGMMLWriter()
```

### Method

Write an XGMML file through the `write` method of the instance:

```python
def write(
    self,
    graph: nx.MultiGraph,
    xgmml_path: str,
    **kwargs
)
```