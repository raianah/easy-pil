import os

from PIL import ImageFont
from typing_extensions import Literal

fonts_directory = os.path.join(os.path.dirname(__file__), "fonts")
fonts_path = {
    "caveat": {
        "regular": os.path.join(fonts_directory, "caveat", "caveat.ttf"),
        "bold": os.path.join(fonts_directory, "caveat", "caveat.ttf"),
        "italic": os.path.join(fonts_directory, "caveat", "caveat.ttf"),
        "light": os.path.join(fonts_directory, "caveat", "caveat.ttf"),
    },
    "montserrat": {
        "regular": os.path.join(
            fonts_directory, "montserrat", "montserrat_regular.ttf"
        ),
        "bold": os.path.join(fonts_directory, "montserrat", "montserrat_bold.ttf"),
        "italic": os.path.join(fonts_directory, "montserrat", "montserrat_italic.ttf"),
        "light": os.path.join(fonts_directory, "montserrat", "montserrat_light.ttf"),
        "semibold": os.path.join(fonts_directory, "montserrat", "montserrat_semibold.ttf")
    },
    "poppins": {
        "regular": os.path.join(fonts_directory, "poppins", "poppins_regular.ttf"),
        "bold": os.path.join(fonts_directory, "poppins", "poppins_bold.ttf"),
        "italic": os.path.join(fonts_directory, "poppins", "poppins_italic.ttf"),
        "light": os.path.join(fonts_directory, "poppins", "poppins_light.ttf"),
    },
}


class Font:
    """Font class

    Parameters
    ----------
    path : str
        Path of font
    size : int, optional
        Size of font, by default 10
    """

    def __init__(self, path: str, size: int = 10, **kwargs) -> None:
        self.font = ImageFont.truetype(path, size=size, **kwargs)

    @staticmethod
    def poppins(
        variant: Literal["regular", "bold", "italic", "light"] = "regular",
        size: int = 10,
    ):
        """Poppins font

        Parameters
        ----------
        variant : Literal["regular", "bold", "italic", "light"], optional
            Font variant, by default "regular"
        size : int, optional
            Font size, by default 10
        """
        return ImageFont.truetype(fonts_path["poppins"][variant], size=size)

    @staticmethod
    def caveat(
        variant: Literal["regular", "bold", "italic", "light"] = "regular",
        size: int = 10,
    ):
        """Caveat font

        Parameters
        ----------
        variant : Literal["regular", "bold", "italic", "light"], optional
            Font variant, by default "regular"
        size : int, optional
            Font size, by default 10
        """
        return ImageFont.truetype(fonts_path["caveat"][variant], size=size)

    @staticmethod
    def montserrat(
        variant: Literal["regular", "bold", "semibold", "italic", "light"] = "regular",
        size: int = 10,
        encoding: str = "unic"
    ):
        """Montserrat font

        Parameters
        ----------
        variant : Literal["regular", "bold", "italic", "light"], optional
            Font variant, by default "regular"
        size : int, optional
            Font size, by default 10
        """
        return ImageFont.truetype(fonts_path["montserrat"][variant], size=size, encoding=encoding)

    @staticmethod
    def sanskr(
        size: int = 10,
        encoding: str = "unic"
    ):
        """Sans Korean Font
        
        Parameters
        ----------
        size : int, optional
            Font size, by default 10
        """
        return ImageFont.truetype("./properties/sanskr.otf", size=size, encoding=encoding)

    @staticmethod
    def sanscn(
        size: int = 10,
        encoding: str = "unic"
    ):
        """Sans Chinese Font
        
        Parameters
        ----------
        size : int, optional
            Font size, by default 10
        """
        return ImageFont.truetype("./properties/sanscn.otf", size=size, encoding=encoding)

    @staticmethod
    def sansjp(
        size: int = 10,
        encoding: str = "unic"
    ):
        """Sans Japanese Font
        
        Parameters
        ----------
        size : int, optional
            Font size, by default 10
        """
        return ImageFont.truetype("./properties/sansjp.otf", size=size, encoding=encoding)

    @staticmethod
    def unisansheavy(
        size: int = 10,
        encoding: str = "unic"
    ):
        """Uni Sans Font
        
        Parameters
        ----------
        size : int, optional
            Font size, by default 10
        """
        return ImageFont.truetype(font="./properties/Uni Sans Heavy.otf", size=size, encoding=encoding)

