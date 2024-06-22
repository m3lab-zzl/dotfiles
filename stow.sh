#!/bin/bash

dotfiles_dir="$PWD"
excludes=(".git" ".DS_Store", ".pre-commit-config.yaml")

# Function to create symbolic links recursively
link_files() {
	local source_dir="$1"
	local target_dir="$2"

	# Ensure target directory exists
	mkdir -p "$target_dir"

	# Loop through all files and directories in source_dir, including hidden ones
	find "$source_dir" -mindepth 1 -maxdepth 1 | while read -r file; do
		local filename=$(basename "$file")

		# Skip excluded files and directories
		if [[ " ${excludes[@]} " =~ " $filename " ]]; then
			continue
		fi

		local target="$target_dir/$filename"

		if [ ! -e "$target" ]; then
			# Create symbolic link
			ln -s "$file" "$target"
			echo "Linked $filename to $target"
		fi

		# If it's a directory, recurse into it
		if [ -d "$file" ]; then
			link_files "$file" "$target"
		fi
	done
}

# Call the function to start linking from dotfiles_dir to $HOME
link_files "$dotfiles_dir" "$HOME"
