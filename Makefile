run: 
	clear
	python3 main.py
install:
	#linux: sudo apt-get install python-pip 
	pip3 install yfinance
	pip3 install pandas
	pip3 install matplotlib
	pip3 install matplotlib
push:
	git commit -a
	git push
	clear
help:
	echo "run, install, push"