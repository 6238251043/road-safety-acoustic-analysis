# road-safety-acoustic-analysis
# Multiresolution Acoustic Analysis for Road Safety

## Project Overview
This project focuses on analyzing traffic acoustic signals for road safety applications. 
Audio signals from road environments are captured using MEMS microphones connected to a Raspberry Pi system.

Signal processing techniques are applied to analyze the acoustic patterns and extract useful features for identifying traffic-related events.

## Technologies Used
- Python
- Raspberry Pi
- Signal Processing
- Machine Learning

## Methodology
1. Capture traffic sound signals using MEMS microphones.
2. Perform signal preprocessing and noise filtering.
3. Apply Short-Time Fourier Transform (STFT) for time-frequency analysis.
4. Extract acoustic features from spectrogram data.
5. Use a machine learning model to classify sound direction.

## Machine Learning Model
• Direction-based acoustic classification  
• Classes: Front, Left, Right, None  
• Model trained for 100 epochs  
• Learning rate scheduling applied  

## Training Results
Training Accuracy: 72.79%  
Validation Accuracy: 65.25%  
Best Validation Accuracy: 70.21%

### Direction-wise Performance
Front: 94.7%  
Left: 51.6%  
Right: 42.1%  
None: 70.6%

Observation:
• Strong front-direction detection  
• Lower side accuracy due to overlapping traffic sounds


## Features
- Real-time traffic sound acquisition
- Signal preprocessing
- Feature extraction from audio signals
- Classification of traffic sound patterns

## Applications
- Road safety monitoring
- Traffic analysis
- Smart city infrastructure
