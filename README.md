
# Align View to Normal Add-on for Blender

This Blender add-on allows users to align the view to the selected normal in various directions from the right-click menu in edit mode. It provides an option to use either a pie menu or a list menu for the alignment operations.

## Features

- Align view to normal in top, bottom, front, back, right, and left directions.
- Switch between pie menu and list menu via add-on preferences.
- Integrated in the right-click context menu in edit mode.

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

## Preferences

You can switch between pie menu and list menu:

1. Go to `Edit > Preferences > Add-ons`.
2. Find the `Align View to Normal` add-on and click the arrow to expand its settings.
3. Choose your preferred menu type (Pie Menu or List Menu).

## Known Issues

- **Crash on Adjust Last Operation**: The add-on may cause Blender to crash when you try to change your selection in the "Adjust Last Operation" menu. This is a known issue and we are working to resolve it.

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please open an issue or create a pull request.

## License

This project is licensed under the Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0) license. See the [LICENSE](LICENSE) file for details.
