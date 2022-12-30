# lcexoplanet

## Ligth Curves for Exoplanets

**Documentation**: <a href="https://github.com/DiegoHS79/lcexoplanet">https://github.com/DiegoHS79/lcexoplanet</a>

**Source Code**: <a href="https://github.com/DiegoHS79/lcexoplanet" target="_blank">https://github.com/DiegoHS79/lcexoplanet</a>

---

This is a package to manage exoplanets light curves.

## Downloading FITS files

We can directly download files just providing the space mission and the ID number of the mission:

```python
from lcexoplanet.utils import SpaceMissionFitsDownload

SpaceMissionFitsDownload("k2", "220522664")
```

**Output**

```shell
You have selected: 220522664 object from K2 Space Mission
 ⤷ object available in c8: downloading ktwo220522664-c08_llc.fits into /Users/username/.lcexoplanet/fits/k2/c8
```

The package will create a folder structure into your local "username" to download a single FIT file.

If, for instance, the mission k2 have more than one FITS files in different campaigns, it will download all those files in its folders.
