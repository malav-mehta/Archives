'''
Angle Classifier
14 April, 2017
'''

import math


class Angle():
    def __init__(self, angle):
        self._angle_rad = float(math.radians(angle))
        self._angle_deg = angle
        self._type = self.classify_angle()

    def classify_angle(self):
        angle_type = ''
        a = self._angle_deg

        if a <= 0:
            angle_type = 'INVALID'
        elif a < 90:
            angle_type = 'acute'
        elif a == 90:
            angle_type = 'right'
        elif a > 90 and a < 180:
            angle_type = 'obtuse'
        elif a == 180:
            angle_type = 'straight'
        else:
            angle_type = 'reflex'

        return angle_type

    def __str__(self):
        return '{0:.3}deg or {1:.3}rad is a(n) [{2}] angle.'.format(self._angle_deg, self._angle_rad, self._type)


ang = input('[! to quit]  > ').strip()
while ang != '!':
    a = Angle(float(ang))
    print(str(a), end='\n\n')
    ang = input('[! to quit] >  ').strip()
