#!/bin/bash

pathName=demo.sh
# echo 是列印值，印出變數 pathName 內容 demo.sh
echo ${pathName}
unset pathName
# 空值
echo $(pathName)
