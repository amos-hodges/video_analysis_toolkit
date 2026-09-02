# Video Analysis Toolkit

A Python project for building practical video analysis utilities, with an initial focus on extracting and displaying basic video information.

## Current Features

The first version can:

- Accept a local video file path
- Open the video with OpenCV
- Display:
  - Frame rate (FPS)
  - Resolution
  - Frame count
  - Calculated video duration
- Handle invalid video files without crashing
- Format duration as `HH:MM:SS.mmm`

## Current Scope

This is an early learning and development project. The current goal is to build a small, useful foundation before adding more advanced video analysis features.

The first feature focuses on basic video properties and simple error handling.

## Planned Improvements

Possible future additions include:

- More robust video metadata
- Better input/path validation
- Frame extraction by frame number or timestamp
- Frame range extraction
- Variable frame rate handling
- Video timing analysis
- Manual measurement tools
- Speed calculations
- Object tracking
- Additional OpenCV-based analysis tools

## Known Limitations

- Video duration is currently calculated using:

  `frame_count / fps`

- This may not be reliable for every video, particularly variable-frame-rate files.
- OpenCV-reported FPS and frame count may require additional validation for more rigorous analysis.

## Requirements

- Python 3.14+
- OpenCV

Install dependencies with:

```bash
python -m pip install opencv-python