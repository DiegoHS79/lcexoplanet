import logging
from pathlib import Path
from typing import Literal

import requests
from bs4 import BeautifulSoup

from .exceptions import MissionError, IdLengthError

logger = logging.getLogger(__name__)


class SpaceMissionFitsDownload:
    K2_CAMPAIGNS = [
        "c0",
        "c1",
        "c2",
        "c3",
        "c4",
        "c5",
        "c6",
        "c7",
        "c8",
        "c9",
        "c102",
        "c111",
        "c112",
        "c12",
        "c13",
        "c14",
        "c15",
        "c16",
        "c17",
        "c18",
        "c19",
    ]

    def __init__(
        self,
        mission: Literal["k2", "kepler", "tess"],
        id_number: str,
        to_path: str = Path("~/.lcexoplanet/fits"),
    ) -> None:
        """Download astronomy FITs file for multiple space missions.

        Args:
            mission (Literal[k2, kepler, tess]): Space mission available.
            id_number (str): ID number that characterize the object for a specific mission.
            to_path (str, optional): Path where to download the FIT file.
                Defaults to ~/.lcexoplanet/fits.

        Raises:
            TypeError: Raises when Id number is not a string istance.
            IdLengthError: Raises when the length of the ID number doesn't fit for the space mission.
            MissionError: Raises if the mission is still not available.
        """
        self.mission = mission.lower()
        self.id_number = id_number
        if not isinstance(self.id_number, str):
            raise TypeError(f"{self.id_number} must be in string format.")

        self.to_path = Path(to_path, self.mission)
        print(self)
        # logger.info(self)

        if self.mission == "k2":
            if len(self.id_number) != 9:
                raise IdLengthError(self.mission, self.id_number)

            first_part = self.id_number[:4] + "00000"
            second_part = self.id_number[4:6] + "000"
            for campaign in self.K2_CAMPAIGNS:
                if campaign != "c8":
                    continue

                url = (
                    "http://archive.stsci.edu/missions/k2/lightcurves/"
                    f"{campaign}/{first_part}/{second_part}"
                )
                self.download_k2_fit(
                    url,
                    campaign,
                    self.id_number,
                    Path(self.to_path, campaign).expanduser(),
                )

        elif self.mission == "kepler":
            self.url = "http://archive.stsci.edu/missions/kepler/"

        elif self.mission == "tess":
            self.url = None

        else:
            raise MissionError(self.mission)

    def __str__(self) -> str:
        text = (
            f"You have selected: \033[1;32;38m{self.id_number}\033[0m "
            f"object from \033[1;32;38m{self.mission.upper()}\033[0m Space Mission"
        )
        return text

    @staticmethod
    def download_k2_fit(url: str, campaign: str, id_number: str, path: str):
        """Static method to download FITs file for K2 space mission.

        Args:
            url (str): Base URL from where to download the FIT file.
            campaign (str): k2 campaign number.
            id_number (str): ID number that characterize the object for a specific mission.
            path (str): Path where to download the FIT file.
        """
        print(path)
        if not path.exists():
            path.mkdir(parents=True, exist_ok=True)
        page = requests.get(url)
        if page.status_code == 200:
            print(
                f" \u2937 object available in \033[1;32;38m{campaign}\033[0m: ", end=""
            )
            soup = BeautifulSoup(page.content, "html.parser")
            for a in soup.findAll("a"):
                if id_number in a["href"]:
                    print(f"downloading \033[0;34;38m{a['href']}\033[0m into {path}")
                    fit_name = f"ktwo{id_number}-{campaign}_llc.fits"
                    fit = requests.get(url + f"/{fit_name}")
                    open(Path(path, fit_name), "wb").write(fit.content)
