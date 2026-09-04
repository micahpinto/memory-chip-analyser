## Binary Pattern Analyser

A tool that analyzes bit patterns in binary files and provides detailed frequency statistics. Designed specifically for analyzing raw memory chip dumps.

**Available in two versions:**
- **CLI Version** (main branch) - Command-line interface
- **GUI Version** (gui-version branch) - Graphical user interface with tkinter

## Background & Use Case

This tool was developed to analyze binary dump files from memory chips read using hardware tools like the **XGecu Pro (XGpro)**. It examines the distribution of bit patterns within the raw binary data, which is useful for:

1. **Memory analysis** - Understanding bit pattern distribution in chip dumps
2. **Data recovery assessment** - Identifying patterns in erased memory
3. **Forensic analysis** - Analyzing bit-level patterns in binary data
4. **Quality control** - Detecting anomalies in memory chip data

The tool groups consecutive bits into configurable block sizes (2, 3, or 4 bits) and counts how often each possible pattern appears.

## Features

1. **Pattern Analysis** - Counts all possible bit patterns
2. **Frequency Statistics** - Shows occurrence count and percentage for each pattern
3. **Optimized Performance** - Efficient bit register-based processing
4. **File Support** - Works with any binary file (.bin, .img, etc.)
5. **Configurable Block Sizes** - Analyze 2-bit, 3-bit, or 4-bit patterns

## CLI Version (Main Branch)

**Description**

The command-line version provides a simple, lightweight interface with no GUI dependencies. Perfect for automation, scripting, or if you prefer terminal-based tools.

**Example output:**

```
File: chip_dump.bin
Block size: 2 bits

Pattern    Occurrences      Frequency
--------------------------------------
00                 12450      0.312450
01                 12500      0.312500
10                 12380      0.309500
11                 12670      0.317550

Total number of blocks: 50000
```

## GUI Version (gui-version Branch)

**Description**

The GUI version provides a graphical interface using tkinter. Perfect for users who prefer point-and-click interaction over command-line input.

A window will open with a user interface.

### Step-by-Step Guide (GUI Version)

1. **Select a File**
   - Click the **"Browse..."** button
   - Navigate to your binary file (.bin, .img, etc.)
   - Click **"Open"**
   - File path appears in the text field

2. **Choose Block Size**
   - Click the dropdown menu next to "Block Size"
   - Select from: **2**, **3**, or **4** bits
   - **2-bit blocks**: Analyzes patterns like `00`, `01`, `10`, `11`
   - **3-bit blocks**: Analyzes 8 possible patterns
   - **4-bit blocks**: Analyzes 16 possible patterns

3. **Run Analysis**
   - Click the **"Analyse"** button
   - Results appear in the text area below

**Example Output:**

```
Pattern    Occurrences      Frequency
--------------------------------------
00                 12450      0.312450
```

- Pattern `00` appears 12,450 times
- This represents 31.245% of all 2-bit blocks
