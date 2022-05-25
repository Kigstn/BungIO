from __future__ import annotations

import attr


@attr.s
class BaseModel:
    @classmethod
    def from_dict(cls, data: dict) -> BaseModel:
        """
        Convert json data to this model

        Args:
            data: The json representation of the model, usually received by bungie

        Returns:
            The model
        """

        # todo

    def to_dict(self) -> dict:
        """
        Convert this model to json data

        Returns:
            A json representation of this model
        """

        # todo
