class Instructor:
    """A class storing information of a Instructor

    === Public Attributes ===
    name: The name of an instructor

    === Private Attributes ===
    _id: the id of the instructor
    """
    name: str
    _id: int

    def __init__(self, name: str, set_id: int) -> None:
        self.name = name
        self._id = set_id

