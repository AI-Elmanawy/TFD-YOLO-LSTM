# TFD-YOLO Live Tomato Freshness Detection Android Application

## Description
This Android application is designed to perform live object detection using the **YOLOv12s lightweight model**. YOLOv12 (You Only Look Once version 12) is the latest version of the YOLO family, renowned for its real-time object detection capabilities. This app brings that functionality to Android devices, specifically tailored for **Tomato Freshness Detection (TFD)**.

## Getting Started

This project is a fork and modification of the excellent base repository: [https://github.com/surendramaran/YOLOv8-TfLite-Object-Detector](https://github.com/surendramaran/YOLOv8-TfLite-Object-Detector ).

To set up and run this application, follow these steps:

1.  **Clone the Repository:**
    ```bash
    git clone [Your Repository URL Here]
    ```
2.  **Open in Android Studio:** Import the project into Android Studio.
3.  **Enable USB Debugging:** Connect your Android device (e.g., Samsung Note 20 Ultra) and ensure **USB Debugging** is enabled in Developer Options.

## Model and Label Replacement

This application is pre-configured to use a custom YOLOv12s model for tomato freshness detection. If you wish to use a different model, follow these steps:

1.  **Prepare Files:** Ensure your custom model is in the **TensorFlow Lite (`.tflite`)** format and your labels are in a plain text file (`.txt`), with one class name per line.
2.  **Replace Files:** Place your new model and labels file into the project's assets folder:
    `app/src/main/assets/`
3.  **Rename Files:** **Crucially, rename your new files to:**
    *   `model.tflite`
    *   `labels.txt`
4.  **Code Check (YOLOv12 Specific):** If your YOLOv12 model's output structure differs from the original YOLOv8 model, you may need to adjust the output parsing logic in the `Detector.kt` file.

## Build and Run

1.  **Sync Gradle:** Click the **Sync Project with Gradle Files** button in Android Studio.
2.  **Run:** Select your connected device and click the **Run 'app'** button (the green play icon).

## Citation

If you use this application or the underlying model in your research, please cite the following publication:

**Title:** 

**DOI:** 