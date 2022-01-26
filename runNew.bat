@echo off
echo **************环境文件删除启动***************
@echo on
cd d:
del /f/s/q D:\6\UIpython\report\tmp\*.json
del /f/s/q D:\6\UIpython\report\tmp\*.jpg
del /f/s/q D:\6\UIpython\report\report

@echo off
echo --------------环境文件删除已经完成，开始运行脚本————————————
@echo on

cd D:/6/UIpython
pytest -sq --alluredir=./report/tmp
allure generate  ./report/tmp -o ./report/report --clean