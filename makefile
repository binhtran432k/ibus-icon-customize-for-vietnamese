help:
	@echo Cách dùng:  "make [OPTIONS] [c=[0x000000-0xffffff]]"
	@echo 
	@echo Options: Mô tả
	@echo - install: Cài đặt thư mục hiện tại làm thư mục chứa icon chỉ cần chạy 1 lần.
	@echo - default: Thay đổi icon thành mặc định.
	@echo - flag: Thay đổi icon thành lá cờ.
	@echo - flag-circle: Thay đổi icon thành lá cờ bo tròn.
	@echo - color c=[0x000000-0xffffff]: Thay đổi icon thành icon mặc định với màu được chỉ định.
	@echo - text c=[0x000000-0xffffff]: Thay đổi icon thành chữ với màu được chỉ định.
	@echo - help: Hiện ra hộp thoại này.

install:
	@if ! [ "$(shell id -u)" = 0 ];then \
	    echo "Bạn phải là root để có thể cài đặt"; \
	    exit 1; \
	fi
	python geticon.py
	python install.py &&\
	ibus restart
default:
	python geticon.py default &&\
	ibus restart

flag:
	python geticon.py flag &&\
	ibus restart

flagcircle:
	python geticon.py flag-circle &&\
	ibus restart

color:
	python geticon.py color $c &&\
	ibus restart

text:
	python geticon.py text $c &&\
	ibus restart

papirustext:
	python geticon.py text 0xd3dae2 &&\
	ibus restart

papirus:
	python geticon.py color 0xd3dae2 &&\
	ibus restart

restart:
	ibus restart

