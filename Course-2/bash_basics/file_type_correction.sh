#!/bin/bash
path="test_files/"
for file in $path*.HTM; do
	name=$(basename "$file" .HTM)
	echo mv "$file" "$name.html"
done
