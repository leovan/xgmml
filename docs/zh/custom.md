---
icon: lucide/file-plus-corner
---

# 自定义

## 读取器

自定义读取器需要从 `XGMMLReader` 类继承，并实现 `_networkx_to` 方法：

```python
class XGMMLReader(Generic[T], ABC):
    def __init__(self, **kwargs):
        pass

    @abstractmethod
    def _networkx_to(self, graph: nx.MultiGraph, **kwargs) -> T:
        raise NotImplementedError()
```

该方法用于将从 XGMML 读取的 `nx.MultiGraph` 对象实例转换为自定义的类实例。`read` 方法中的 `kwargs` 参见将传递至 `_networkx_to` 方法中。

## 写入器

自定义写入器需要从 `XGMMLWriter` 类继承，并实现 `_to_networkx` 方法：

```python
class XGMMLWriter(Generic[T], ABC):
    def __init__(self, **kwargs):
        self._uuid = str(uuid.uuid4())
        self._element_maker = ElementMaker(nsmap=NAMESPACES)

    @abstractmethod
    def _to_networkx(self, graph: T, **kwargs) -> nx.MultiGraph:
        raise NotImplementedError()
```

该方法用于将自定的类实例转换为 `nx.MultiGraph` 对象实例，从而将其写入 XGMML 文件。`write` 方法中的 `kwargs` 参见将传递至 `_to_networkx` 方法中。
