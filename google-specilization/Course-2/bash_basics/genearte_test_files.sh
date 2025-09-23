#!/bin/bash

if [ -d "test_files" ]; then
	echo "folder exists"
else
	mkdir "test_files"
fi

for name in file1.HTM file2.HTM file3.HTM; do
	touch "test_files/""$name"
done
