#!/bin/bash
if [ "$(uname)" = "Darwin" ]; then
	# Mac OS X 操作系统
    nohup ./go-cqhttp-v0.9.40-darwin-amd64
elif [ "$(expr substr $(uname -s) 1 5)" = "Linux" ]; then
	# GNU/Linux操作系统
    nohup ./go-cqhttp-v0.9.40-linux-386
elif [ "$(expr substr $(uname -s) 1 10)" = "MINGW64_NT" ]; then
	# Windows NT操作系统
    nohup ./go-cqhttp-v0.9.40-windows-amd64.exe
fi