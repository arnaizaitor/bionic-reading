# Usage: make clean
clean:
	find zips -type f ! -name '.gitkeep' -delete
	find zips -type d -delete
