# Usage: make clean
clean:
	find zips -type f ! -name '.gitkeep' -delete
	find zips -type d ! -name 'zips' -delete
	find output -type f ! -name '.gitkeep' -delete
