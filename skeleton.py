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
        """
        Description: Creates a new Crew Member object and adds to Crew Roster
        Params:
            name (str): Name of the Crew Member object
            role (str): Role of the Crew Member object
            experience (int): Years of experience in specific role
        Returns:
            None
        """
        self.crew.append(CrewMember(name, role, experience))

    def remove_member(self, name):
        """
        Description: Removes a Crew Member object from Crew Roster by name.
        Params:
            name (str): Name of Crew Member object
        Returns:
            None
        """
        for member in self.crew:
            if member.name == name:
                self.crew.remove(member)

    def list_crew(self):
        """
        Description: Prints all Crew Member objects from Crew Roster
        Params:
            None
        Returns:
            None
        """
        for member in self.crew:
            print(member.__str__())

# === TEST CODE ===

roster=CrewRoster() #Empty Crew roster created

    # TODO: Uncomment and implement methods
roster.add_member("Alice", "Engineer", 5)
roster.add_member("Bob", "Pilot", 10)
roster.list_crew()

roster.remove_member("Alice")
roster.list_crew()
