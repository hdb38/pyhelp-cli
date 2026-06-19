# pyhelp-cli
## 这是什么？
pyhelp-cli 是我自己写的 Python 命令行工具，用来快速创建代码模板、批量管理文件，支持 Manim、Numpy模板一键生成。

## 运行前置条件
只需要安装 Python 环境，不需要额外复杂软件。

## 安装使用教程
1. 把代码仓库下载到本地
```bash
git clone https://github.com/hdb38/pyhelp-cli.git
```
2. 进入项目文件夹
```bash
cd pyhelp-cli
```
3. 本地安装工具
```bash
pip install -e .
```
4. 查看全部可用指令
```bash
pyhelp --help
```

## 全部命令介绍
1. clean-log — 清理程序日志文件
2. create-dir — 新建文件夹
3. create-file — 新建空白文件
4. gui — 打开图形可视化窗口
5. init-file — 根据模板一键生成代码文件（Manim、Numpy等）
6. init-list — 查看所有自带代码模板
7. remove-dir — 删除文件夹
8. remove-file — 删除单个文件
9. replace-file-name — 修改文件名
10. version — 查看工具当前版本

## 使用注意事项
1. gui 图形界面功能还在开发，部分功能不完善
2. remove-dir 删除文件夹时，文件夹里面所有文件会同步被清除，谨慎使用，避免误删重要内容

## 作者
hdb38 （GitHub / B 站 / 洛谷 账号同名）
