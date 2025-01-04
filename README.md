Dataset for OggDude's character generator 2.3.4.0.

## Installation

Create a folder where you will put both the Character Generator and the dataset. Create two subfolders, one called `character_generator` and the other called `custom_dataset`.

### OggDude's Character Generator installation

Download the [OggDude's Character Generator](https://www.swrpgcommunity.com/gm-resources/apps-dice-utilities/oggdudes-generator) zip file and unzip it inside the `character_generator` folder. Executables and other files should be unzipped right into the `character_generator` folder, not into a subfolder.

### Custom dataset setup

Now you need to download the dataset. You can obtain it in two ways:

1. Download the `DataCustom` zip file directly from the [Releases section](https://github.com/Septaris/OggDudes-Custom-Dataset-SW/releases/). Unzip the file and move the `DataCustom` folder into the `custom_dataset` folder.
2. Download or clone the source code from this repository and keep only the `DataCustom` folder. 

### Linking the dataset

Run the Character Generator launcher `SWCharGenLauncher.exe` and set the `Data Path` to the `custom_dataset` folder. If you prefer, you can use a relative path, but you will need to check the `Make path relative to install directory` checkbox.

## Usage

The Character Generator is now ready to use with the custom dataset. You will see the full description of the species, careers, specializations, etc. in the appropriate tabs.

## Data Imports in Foundry VTT

To import the majority of item data into Foundry VTT, you can use the OggDude dataset importer. Follow these steps:

1. From within your world, select **Compendium Packs**.
2. Click **OggDude Dataset Importer** at the bottom of the list.
5. Use the zipped `DataCustom` file:
   - Select your zipped data file using the "Choose File" file picker.
   - Click **Load File**.
6. Select the types of data you'd like to import.
7. Click **Start Import**.

The imported data will be added to a series of compendiums.

### Notes

- **Blank Compendiums**: If any of the compendiums are blank, it often indicates an issue with your dataset. However, if you're using the dev branch of the system, it could also be a bug. Bring it up in the system's Discord channel.
- **Do NOT Lock Compendiums**: Avoid locking the imported compendiums. Doing so will prevent you from importing PCs or NPCs from OggDude's dataset.

For more details, refer to the [Star Wars FFG Foundry VTT Wiki](https://github.com/StarWarsFoundryVTT/StarWarsFFG/wiki/Getting-started#importing-oggdude-data).

## Contributing

If you want to contribute to the dataset, you can do so by forking the repository, making changes, and creating a pull request.

## Acknowledgements

The dataset's quality is almost entirely because of the hard work of @nlx3647 and @AvDalfsen. Thank you both for your dedication and effort. And thanks to all the contributors who have helped (and will help) improve the dataset.

And of course, thanks to OggDude for creating the Character Generator and making it available to the community.
