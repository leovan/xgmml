# API

## 读取器

### 对象

创建 `XGMMLReader` 对象实例，当前有：

- `NetworkxXGMMLReader`
- `IgraphXGMMLReader`

以 `NetworkxXGMMLReader` 为例：

```python
from xgmml.reader.networkx_xgmml_reader import NetworkxXGMMLReader

reader = NetworkxXGMMLReader()
```

### 方法

通过实例的 `read` 方法读取 XGMML 文件：

```python
def read(
    self,
    xgmml_path: str,
    **kwargs
) -> nx.MultiGraph
```

结果为 `nx.MultiGraph` 对象实例。

## 写入器

### 对象

创建 `XGMMLWriter` 对象实例，当前有：

- `NetworkxXGMMLWriter`
- `IgraphXGMMLWriter`

以 `NetworkxXGMMLWriter` 为例：

```python
from xgmml.writer.networkx_xgmml_writer import NetworkxXGMMLWriter

writer = NetworkxXGMMLWriter()
```

### 方法

通过实例的 `write` 方法写入 XGMML 文件：

```python
def write(
    self,
    graph: nx.MultiGraph,
    xgmml_path: str,
    **kwargs
)
```
