## Binary Erasure Analyzer
A Python utility that analyzes binary files and calculates the percentage of 1 bits (erasure density) in the data.

**Description**
This script reads a binary (.bin) file and computes the percentage of 1 bits compared to the total number of bits in the file. This can be useful for understanding data density, compression analysis, or binary file statistics.

**Features**
1.Reads binary files efficiently
2.Converts binary data to bit representation
3.Calculates bit distribution (0s and 1s)
4.Displays erasure percentage with 2 decimal places

## Background & Use Case

This tool was developed to analyze binary dump files from erased memory chips. 
When memory chips are read using hardware tools like the **XGecu Pro (XGpro)**, the extracted data is in raw binary format. This script helps determine the 
erasure percentage—the density of `1` bits—which is useful for understanding data recovery and memory analysis workflows.

**Typical workflow:**
1. Read memory chip with XGpro or similar tool → generates .bin file
2. Run this analyzer → get erasure percentage statistics
3. Use results for data recovery assessment or forensic analysis
