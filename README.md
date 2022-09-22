# devtoolsai_demo_selenium_python
Sample project showing how to use SmartDriver with Appium python


# Setup

You need to first install the dependencies
```
python3 -m pip install -r requirements.txt
npm install appium
```

# Android
You also need to create an emulator with Anroid studio for instance

## Preparation
You need to run your Android emulator and run Appium. In two different windows
```
emulator -avd Pixel_4_API_29 # choose the AVD you created here
```
```
appium # run appium
```

In the script uiautomator2.py, customize the path to the APK with a path to your apk

## Running the test
We provide a sample test that does two things:
 - Shows how to ingest an element with traditional locator (MobileBy.id)
 - Shows how to use the find_by_ai method to prompt and label the text field visually

The test will click on the continue with email button then ask you to label the text field to type in the username

```
export DEVTOOLSAI_INTERACTIVE=1 # enables interactive mode / prompting
python3 uiautomator2.py
```

# iOS
## Preparation
You need to start the iOS simulator from Xcode, you can customize the emulator name in the script, but the default is 'iPhone 12 Pro Max' with iOS '14.4'

You also need to run Appium
```
appium
```
We provide a very basic sample ios .app file you can use. Otherwise you will need to get the .app or .ipa files for the apps you want to automate.
In the script ios.py, customize the path to the .app file


## Running the test

The test shows the method calls to find by xpath and find_by_ai, same ideas as Android, the first one will ingest visually the element and robustify the locator, the second one will prompt for you to draw a bounding box, you shoul draw it around 'Show alert'




