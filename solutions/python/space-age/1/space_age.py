class SpaceAge:
    earth_days = 365.25
    def __init__(self, seconds):
        self.seconds = seconds
    
    def on_mercury(self):
        return self.calculate_years(0.2408467)
    
    def on_venus(self):
        return self.calculate_years(0.61519726)

    def on_earth(self):
        return self.calculate_years(1)
    
    def on_mars(self):
        return self.calculate_years(1.8808158)
    
    def on_jupiter(self):
        return self.calculate_years(11.862615)
    
    def on_saturn(self):
        return self.calculate_years(29.447498)
    
    def on_uranus(self):
        return self.calculate_years(84.016846)
    
    def on_neptune(self):
        return self.calculate_years(164.79132)
    
    def calculate_years(self, multiplier):
        return round(self.seconds/(SpaceAge.earth_days * multiplier * 24 * 60 * 60), 2)

      
