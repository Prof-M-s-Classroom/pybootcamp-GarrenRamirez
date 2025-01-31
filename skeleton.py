class CrewMember:

    def __init__(self, name, role, experience):
        self.name = name
        self.role = role
        self.experience = experience  # Years of experience

    def __str__(self):
        return f"{self.name} - {self.role} ({self.experience} yrs exp)"

class CrewRoster:

    def __init__(self):
        self.crew = []  # List of CrewMember objects

    def add_member(self, name, role, experience):
        """Creates a new crew member and adds to roster."""


    def remove_member(self, name):
        """Removes a crew member by name."""


    def list_crew(self):
        """Prints all crew members."""


# === TEST CODE ===

roster=CrewRoster() #Empty Crew roster created

    # TODO: Uncomment and implement methods
    # roster.add_member("Alice", "Engineer", 5)
    # roster.add_member("Bob", "Pilot", 10)
    # roster.list_crew()

    # roster.remove_member("Alice")
    # roster.list_crew()

print("Test Commit! :D PLZZ")