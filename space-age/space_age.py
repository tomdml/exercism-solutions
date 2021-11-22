class SpaceAge:

    def __init__(self, seconds):
        self.seconds = seconds

        earthyearsbyplanet = {
            'earth': 1,
            'mercury': 0.2408467,
            'venus': 0.61519726,
            'mars': 1.8808158,
            'jupiter': 11.862615,
            'saturn': 29.447498,
            'uranus': 84.016846,
            'neptune': 164.79132
        }

        def maker(years):
            def _func():
                return round(self.seconds / 31557600 / years, 2)
            return _func

        for (planet, years) in earthyearsbyplanet.items():
            setattr(self, 'on_' + planet, maker(years))
