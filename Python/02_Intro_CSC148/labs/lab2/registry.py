# When runners register for a race, they provide their name, email address and
# their speed category.
class Runner(object):
    name: str
    email: str
    speed_cate: str

    s1 = 'under 20 minutes'
    s2 = 'under 30 minutes'
    s3 = 'under 30 minutes'
    s4 = '40 minutes and over'

    def __init__(self, who: str, contact: str, speed: str):
        self.name = who
        self.email = contact
        self.speed_cate = speed


class Organizers(object):
    speed_runners: dict    # match the speed with the name
    runners_speed: dict   # match the name with the speed
    all_runners: list

    s1 = 'under 20 minutes'
    s2 = 'under 30 minutes'
    s3 = 'under 30 minutes'
    s4 = '40 minutes and over'

    def __init__(self, runner: Runner):
        self.speed_runners = {Organizers.s1: [], Organizers.s2: [],
                              Organizers.s3: [], Organizers.s4: []}
        self.runners_speed = {}
        self.all_runners = []
        self.all_runners.append(runner)

    def match_runner_speed(self):
        """Adding runner to the runners_list"""
        for runners in self.all_runners:
            self.runners_speed[runners.name] = runners.speed_cate

    def match_speed_runner(self):
        """Matching runner's name to their speed group in the runners_speed,
        meking sure we are ablt to get a list of runners in a given speed
        category"""
        for runners in self.all_runners:
            if runners.speed_cate == Organizers.s1:
                self.speed_runners[Organizers.s1].append(runners.name)
            elif runners.speed_cate == Organizers.s2:
                self.speed_runners[Organizers.s2].append(runners.name)
            elif runners.speed_cate == Organizers.s3:
                self.speed_runners[Organizers.s3].append(runners.name)
            elif runners.speed_cate == Organizers.s4:
                self.speed_runners[Organizers.s4].append(runners.name)

    def change_email(self, email: str, ):
        """Change the email adress for a runner if asked"""
