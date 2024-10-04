# Bangshow

![card_after_training](https://sprooc-pic.oss-cn-hangzhou.aliyuncs.com/pics/card_after_training.png)

**Select Language:**

- English / [中文](README.zh_CN.md)

## Overview

**Bangshow** is a command-line tool designed to display images of Bang Dream bands in a terminal. It provides a simple way to visualize your favorite characters and enhance your terminal experience.

## Features

- Display images of Bang Dream characters directly in your terminal.
- Lightweight and easy to use.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.x
- `chafa` (for image rendering in the terminal. If you have not, `install.sh` will help you install it)

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/sprooc/bangshow.git
   cd bangshow
   ```

2. **Run the Installation Script**:

   Execute the following command to set up a virtual environment and install the required packages:

   ```bash
   ./install.sh
   ```

   This script will:
   - Create a virtual environment in `~/.bangshow`.
   - Install the `bangshow` package.
   - Link the `bangshow` executable to `/usr/bin`, making it accessible globally.

## Usage

To display an image of a Bang Dream character or band, use the following command format:

```bash
bangshow [-h] [-u] [-s] [-d D] [-l] name [name ...]
```

### Description

**Bang Dream Images Display Tool**

#### Positional Arguments:
- **name**: Band or character name(s) to display.

#### Options:
- `-h, --help`: Show this help message and exit.
- `-u`: Update images.
- `-s`: Display images.
- `-d D`: Specify delay (in seconds) between image displays.
- `-l`: Loop playback of images.

### Examples

1. **Display a Character**:
   To display an image of a character named "Hina":
   ```bash
   bangshow Hina
   ```

2. **Display a Band**:
   To display an image of the band "Poppin'Party":
   ```bash
   bangshow "Poppin'Party"
   ```

3. **Update Images**:
   To update the images for a specific character:
   ```bash
   bangshow -u Hina
   ```

4. **Display Images with Delay**:
   To display images of "Kasumi" with a 2-second delay between each image:
   ```bash
   bangshow -d 2 Kasumi
   ```

5. **Loop Playback**:
   To display images of "Ran" in a loop:
   ```bash
   bangshow -l Ran
   ```

6. **Multiple Names**:
   To display images for multiple characters:
   ```bash
   bangshow Hina Kasumi Rimi
   ```

## Options

### Character Options

| Character  | Abbreviations           |
|------------|-------------------------|
| Kasumi     | ksm, kasumi             |
| Tae        | tae                     |
| Rimi       | rimi                    |
| Saya       | saya, saaya             |
| Arisa      | arisa, ars              |
| Ran        | ran                     |
| Moca       | moca, moka              |
| Himari     | himari, hmr             |
| Tomoe      | tomoe                   |
| Tsugumi    | tsugumi, tsugu          |
| Kokoro     | kokoro, kkr             |
| Kaoru      | kaoru                   |
| Hagumi     | hagumi, hgm             |
| Kanon      | kanon                   |
| Misaki     | misaki, msk             |
| Aya        | aya                     |
| Hina       | hina                    |
| Chisato    | chisato                 |
| Maya       | maya                    |
| Eve        | eve                     |
| Yukina     | yukina, ykn             |
| Sayo       | sayo                    |
| Lisa       | lisa                    |
| Ako        | ako                     |
| Rinko      | rinko                   |
| Mashiro    | mashiro, msr            |
| Toko       | toko                    |
| Nanami     | nanami, nnm             |
| Tsukushi   | tsukushi, tks           |
| Rui        | rui                     |
| Rei        | rei, layer              |
| Rokka      | rokka, lock             |
| Masuki     | masuki, masking         |
| Reona      | reona, pareo            |
| Chiyu      | chiyu, chuchu, chu2     |
| Tomori     | tomori, tmr             |
| Anon       | anon                    |
| Rana       | rana                    |
| Soyo       | soyo                    |
| Taki       | taki, rikki             |

### Band Options

| Band               | Abbreviations           |
|--------------------|-------------------------|
| Poppin'Party       | ppp                     |
| Afterglow          | ag                      |
| Pastel*Palettes    | PasPale, pp             |
| Roselia            | roselia, R              |
| Hello, Happy World!| hhw                     |
| Morfonica          | mofonica                |
| RAISE A SUILEN     | ras                     |
| MyGO!!!!!          | mygo                    |

## Acknowledgments

The images and materials used in this project are sourced from [BestDori](https://bestdori.com/).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or feedback, please reach out to [1127626033@qq.com].
