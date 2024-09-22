class MissionError(Exception):

    missions = ", ".join(["\033[1;32;38mk2\033[0m", "\033[1;32;38mkepler\033[0m"])

    def __init__(self, mission: str, *args: object) -> None:
        """Exception to catch the lack of space mission defined in the class

        Args:
            mission (str): No existing mission.
        """
        super().__init__(*args)
        self.mission = mission

    def __str__(self) -> str:
        colored_mission = f"\033[1;31;38m{self.mission}\033[0m"
        message = f"Mission: {colored_mission} is still \033[0;31;38mnot available\033[0m or doesn't exist.\n"
        message += f"\tplease, choose a valid one: {self.missions}"
        return message


class IdLengthError(Exception):
    len_mission = {"k2": 9}

    def __init__(self, mission: str, id_number: str, *args: object) -> None:
        super().__init__(*args)
        self.id_number = id_number
        self.mission = mission

    def __str__(self) -> str:
        message = (
            f"{self.mission} id object must have exaclty \033[0;31;38m{self.len_mission[self.mission]}"
            + f" characters\033[0m, {len(self.id_number)} characters provided."
        )
        return message
