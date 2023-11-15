# Speech Recognition and OpenAI Whisper

This Python project demonstrates speech recognition using the `speech_recognition` library and utilizes OpenAI's Whisper model for transcribing speech.

## Installation

1. Clone the repository or download the project files.
2. Create a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use: venv\Scripts\activate
    ```
3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Ensure you have a microphone connected to your system.
2. Run the `speech.py` script:
    ```bash
    python speech.py
    ```
    This script listens for speech input for up to 120 seconds, transcribes it using OpenAI's Whisper model, and displays the transcribed text.

## File Structure

- `speech.py`: Main Python script for speech recognition and transcribing using the Whisper model.
- `requirements.txt`: Contains the required Python packages and their versions.
- `audio.wav`: Temporary file to save the recorded audio.

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
