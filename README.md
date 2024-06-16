
# Align View to Normal Add-on for Blender

This Blender add-on allows users to align the view to the selected normal in various directions from the right-click menu in edit mode. It provides an option to use either a pie menu or a list menu for the alignment operations.

## Features

- Align view to normal in top, bottom, front, back, right, and left directions.
- Switch between pie menu and list menu via add-on preferences.
- Integrated in the right-click context menu in edit mode.
- Shortcut Key: Use `Ctrl + Shift + A` to open the alignment menu quickly.

## Installation

### Installing from Python File

1. Download the `align_view_to_normal.py` file.
2. Open Blender and go to `Edit > Preferences > Add-ons`.
3. Click on `Install...` and select the downloaded `align_view_to_normal.py` file.
4. Enable the add-on by checking the box next to its name.

### Installing from ZIP File

1. Download the ZIP file:
   - [Download the ZIP file directly](https://github.com/flyinggoatman/blender-align-view-addon/raw/main/align_view_to_normal_with_pie_menu.zip)
   - Or, download the repository as a ZIP from GitHub.
2. Open Blender and go to `Edit > Preferences > Add-ons`.
3. Click on `Install...` and select the downloaded ZIP file.
4. Enable the add-on by checking the box next to its name.

## Usage

1. In edit mode, select at least one face, edge, or vertex.
2. Right-click to open the context menu.
3. Choose `Align View to Normal` and select the desired direction.
4. Alternatively, use `Ctrl + Shift + A` to open the alignment menu quickly.

![Gif of how to change settings and use addon](./images/Gif%20of%20how%20to%20change%20settings%20and%20use%20addon.gif)

## Preferences

You can switch between pie menu and list menu:

1. Go to `Edit > Preferences > Add-ons`.
2. Find the `Align View to Normal` add-on and click the arrow to expand its settings.
3. Choose your preferred menu type (Pie Menu or List Menu).

![list menu preview when you control shift a](./images/list%20menu%20preview%20when%20you%20control%20shift%20a.png)
![list menu preview when you right click](./images/list%20menu%20preview%20when%20you%20right%20click.png)
![pie menu preview when you control shift a](./images/pie%20menu%20preview%20when%20you%20control%20shift%20a.png)

## Known Issues

- **Crash on Adjust Last Operation**: The add-on may cause Blender to crash when you try to change your selection in the "Adjust Last Operation" menu. This is a known issue and I am working to resolve it.

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please open an issue or create a pull request.

## License

This project is licensed under the Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0) license. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

I developed this add-on with the assistance of AI to help understand and make the coding and documentation process easier. I value transparency and believe in openly sharing the tools and methods used in the creation of this project. I wanted a tool to do this specific thing and made it for my own personal use.

Thank you for using the Align View to Normal add-on. I look forward to your feedback!
