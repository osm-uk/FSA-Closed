#!/usr/bin/env bash

sort --unique --numeric-sort --output=data/out_file.csv data/out_file.csv

git diff --exit-code data/out_file.csv
if [ $? -eq 1 ]; then
	git config user.email "github-actions[bot]@users.noreply.github.com"
	git config user.name "GitHub Actions"
	git add -A data/out_file.csv
	git commit -m "Sort"
	git push
fi
