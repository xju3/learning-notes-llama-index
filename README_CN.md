## Versions
- [En](README_EN.md)

## 书籍介绍:
* [building-data-driven-applicatinos-wth-llama-index](https://www.packtpub.com/en-us/product/building-data-driven-applications-with-llamaindex-9781835089507)

## 运行环境:
- 使用 .env 存储相对敏感信息，如数据库账号，OPENAI Key等
- 下面是.env的内容定义
```sh
    OLLAMA_API=http://localhost:11434
    OLLAMA_MODEL=mistral:latest
    MONGO_URI=mongodb://root:root@localhost
    PG_URI=postgresql://yourname:password@localhost:5433/db_naEn
    LLAMA_CLOUD_API_KEY=
    OPENAI_API_KEY=
```
- 你需要在代码目录下创建.env文件.

## 说明
* 推荐使用Python 3.11版本，其他版本未经测试
* env.py 是运行本地大模型环境(ollama)的基础设置
*  [llama-index-reader-index.ipynb](llama-index-reader-index.ipynb)  含盖本书的前1-5所讲述的知识内容,包括
    * reader, 
    * splitter, 
    * phaser, 
    * extractor, 
    * storage context 
    * doc & nodes & index persistence.