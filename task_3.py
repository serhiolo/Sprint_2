class PointsForPlace:
    def __init__(self):
        self.points = 0

    @staticmethod
    def get_points_for_place(place):
        
        place = int(place)
        if place > 100: 
            return "Баллы начисляются только первым 100 участникам"
        elif place < 1:
            return 'Спортсмен не может занять нулевое или отрицательное место'
        else:
            points = 101 - place
            return points

class PointsForMeters:
    
    def __init__(self):
        self.points = 0
        
    @staticmethod
    def get_points_for_meters(meters):
        meters = int(meters)
        if meters < 0:
            return 'Количество метров не может быть отрицательным'
        else:
            points = meters * 0.5
            return points 
        
class TotalPoints(PointsForPlace, PointsForMeters):
    
    def __init__(self):
        PointsForPlace.__init__(self)
        PointsForMeters.__init__(self)
    
    
    def get_total_points(self, meters, place):  
        points_place = super().get_points_for_place(place)
        points_meters = super().get_points_for_meters(meters)


#я нашел в интернете такой метод проверки, но мы вроде такого не проходили:
        if isinstance(points_place, str):
            return points_place
        if isinstance(points_meters, str):
            return points_meters

        total = points_place + points_meters
        return total

points_for_place = PointsForPlace()
print(points_for_place.get_points_for_place(10))

points_for_meters = PointsForMeters()
print(points_for_meters.get_points_for_meters(10))

total_points = TotalPoints()
print(total_points.get_points_for_place(10))
print(total_points.get_points_for_meters(10))
print(total_points.get_total_points(-1, 0))