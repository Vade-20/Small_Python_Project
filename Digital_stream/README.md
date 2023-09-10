# Digital Stream 

## Introduction
This Python script generates a digital stream that resembles characters falling like raindrops in a terminal. It uses random values to create a visually appealing effect. You can adjust various parameters to customize the appearance of the stream.

## Usage
1. **Running the Script**: To run the script, simply execute it using Python. For example:
   ```
   python digital_stream.py
   ```

2. **Termination**: To stop the stream, press Ctrl+C.

## Customization
You can customize the appearance of the digital stream by modifying the following parameters in the script:

- `MIN_STREAM_SIZE`: Minimum length of a single stream.
- `MAX_STREAM_SIZE`: Maximum length of a single stream.
- `PAUSE`: The pause between displaying each frame of the stream.
- `DENSITY`: Density percentage, representing the percentage of the terminal's width to be filled with the stream. Adjust this to control how full the screen appears.

## Example
Here's an example of how the script can be configured:

```python
MIN_STREAM_SIZE = 6         # Minimum stream size
MAX_STREAM_SIZE = 14        # Maximum stream size
PAUSE = 0.1                 # Pause between frames
DENSITY = 10                # Density percentage (10% of terminal width)
```

## Dependencies
This script relies on the following Python modules:
- `time`
- `random` 
- `os`
