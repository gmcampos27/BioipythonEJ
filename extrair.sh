#!/BIN/BASH
for file in *.gz; do
	gunzip -c "$file" > "${file/.gz}"
done
