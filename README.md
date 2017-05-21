主程序为 `Sol.py`，外加三个模块 `Eros.py`, `Ganymede.py`, `Luna.py`，均在同一目录下。`Sol.py` 会按顺序下载包含关键词的所有应用，`Eros.py` 用来解析搜索列表，`Ganymede.py` 提取应用列表，`Luna.py` 解析应用的详细信息。运行主程序，会在程序目录下新建 `Pack` 目录，每个应用又会在 `Pack` 中建立自己的目录，其中包括 apk 文件、应用的图标文件、应用的酷安网页文件。

**注：使用的是 Python3，外加 Requests**