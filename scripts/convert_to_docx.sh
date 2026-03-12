#!/bin/bash

# PCRA Document Conversion Script
# Converts markdown files to DOCX format using pandoc
# 
# Prerequisites: 
#   1. Install pandoc: brew install pandoc
#   2. Install pandoc-crossref: brew install pandoc-crossref
#
# Usage: ./convert_to_docx.sh

set -e

echo "Converting PCRA documents to DOCX format..."

# Source directory
SRC_DIR="docs"
OUTPUT_DIR="docs"

# Files to convert
FILES=(
    "PCRA_Comprehensive_Guide.md"
    "PCRA_Prompt_Components.md"
    "PCRA_Example_Utterances.md"
)

# Convert each file
for file in "${FILES[@]}"; do
    if [ -f "$SRC_DIR/$file" ]; then
        output_name="${file%.md}.docx"
        echo "Converting: $file -> $output_name"
        pandoc "$SRC_DIR/$file" \
            -o "$OUTPUT_DIR/$output_name" \
            --standalone \
            --toc \
            --toc-depth=3 \
            --highlight-style=tango \
            -V maintitle="PCRA Documents" \
            -V title="$output_name"
        echo "✓ Created: $output_name"
    else
        echo "⚠ Warning: $file not found, skipping"
    fi
done

echo ""
echo "✅ Conversion complete! DOCX files are in the docs/ folder:"
ls -la "$OUTPUT_DIR"/*.docx 2>/dev/null || echo "No DOCX files found"