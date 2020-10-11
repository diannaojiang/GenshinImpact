# Genshin Impact datamine

scripts and instructions to extract assets of the game Genshin Impact by miHoYo

## Requirements

* [CBT2 files](https://autopatchhk.yuanshen.com/client_app/pc_plus19/Genshin_0.7.1.zip)
* [Genshin_CB2_Decrypt by blueffie](https://mega.nz/file/Bx1Q3K5a#_CXIyHIufVIrUovtfUTgGhI7yqHxVqTe51FbCHnj7Ak)
* [Python 3.6+](https://www.python.org/) with [UnityPy](https://github.com/K0lb3/UnityPy)

## Instructions

1. download and unpack the CBT2 files
2. run Genshin_CB2_Decrypt and open ``\StreamingAssets\AssetBundles`` of the extracted files
3. copy unpack.py into ``\StreamingAssets\AssetBundles`` and run it
4. profit - check ``\StreamingAssets\AssetBundles\export``

## Sources

* [zenhax - Genshin Impact Closed Beta (.blk file)](https://zenhax.com/viewtopic.php?f=9&t=14172)