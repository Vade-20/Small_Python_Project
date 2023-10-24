# Text-to-Speech Talker

This is a simple Python application that converts text into speech using the `pyttsx3` library and a graphical user interface (GUI) built with the `tkinter` library. The program provides the option to configure different aspects of the text-to-speech conversion, such as voice selection, speaking rate, and volume.

## Prerequisites

Before running this program, make sure you have the `pyttsx3` library installed. If it's not already installed, you can install it using `pip` (Python package manager). Open a terminal or command prompt and run the following command:

```sh
pip install pyttsx3
```

On macOS and Linux, you may need to use `pip3` instead of `pip` for Python 3.

## Application Features

### Main Screen

When you run the program, you will see the main screen, which consists of the following components:

- A text input area where you can enter the text you want to convert to speech.
- A "Speak" button to convert and speak the entered text.
- A "Settings" button to configure the voice, rate, and volume settings.

### Speak

Click the "Speak" button to convert and speak the text you've entered in the input area. The program will use the default voice settings unless you configure them in the settings.

### Settings

Click the "Settings" button to access the settings screen, where you can configure the following:

- **Voices**: You can choose from available voices for text-to-speech conversion.
- **Rate**: Adjust the speaking rate (words per minute).
- **Volume**: Adjust the volume of the speech (0 to 100).

After configuring the settings, click the "BACK" button to return to the main screen with the updated settings applied.

## Important Notes

- The `pyttsx3` library is used for text-to-speech conversion, so you may experience different behaviors depending on the installed speech engines and voices on your system.
- The default voice, rate, and volume settings are applied when you click the "Speak" button on the main screen.
- The program handles invalid input for the rate and volume settings. If you input non-numeric values, it won't proceed.
- Once the text-to-speech conversion process begins, there is no option to pause it or access the settings until the conversion has concluded. Accessing the settings becomes available once the conversion is finished.
