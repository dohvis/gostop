class Card(object):
    def __init__(self, name, month, group):
        self.name = name
        self.month = month
        self.group = group

    def __repr__(self):
        return "{__class__.__name__}(name='{name}', month={month}, group={group})" \
            .format(__class__=self.__class__, **self.__dict__)

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if other is None:
            return False
        elif isinstance(other, self.__class__):
            return self.month == other.month and \
                   self.group == other.group
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.group < other.group
        return NotImplemented

    def __hash__(self):
        return hash(self.month) ^ hash(self.group)


class Month(object):
    JAN = 1
    FEB = 2
    MAR = 3
    APR = 4
    MAY = 5
    JUN = 6
    JUL = 7
    AUG = 8
    SEP = 9
    OCT = 10
    NOV = 11
    DEC = 12


class Group(object):
    BRIGHT = 1
    ANIMAL = 2
    RIBBON = 3
    JUNK = 4
    JUNK_2 = 5


CRANE = Card('송학 - 광', Month.JAN, Group.BRIGHT)
PINE_RED_POEM = Card('송학 - 홍단', Month.JAN, Group.RIBBON)
PINE = Card('송학 - 피', Month.JAN, Group.JUNK)

BUSH_WARBLER = Card('매조 - 끗', Month.FEB, Group.ANIMAL)
PLUM_RED_POEM = Card('매조 - 홍단', Month.FEB, Group.RIBBON)
PLUM = Card('매조 - 피', Month.FEB, Group.JUNK)

CURTAIN = Card('벚꽃 - 광', Month.MAR, Group.BRIGHT)
CHERRY_RED_POEM = Card('벚꽃 - 홍단', Month.MAR, Group.RIBBON)
CHERRY = Card('벚꽃 - 피', Month.MAR, Group.JUNK)

CUCKOO = Card('흑싸리 - 끗', Month.APR, Group.ANIMAL)
WISTERIA_RED = Card('흑싸리 - 초단', Month.APR, Group.RIBBON)
WISTERIA = Card('흑싸리 - 피', Month.APR, Group.JUNK)

BRIDGE = Card('난초 - 끗', Month.MAY, Group.ANIMAL)
IRIS_RED = Card('난초 - 초단', Month.MAY, Group.RIBBON)
IRIS = Card('난초 - 피', Month.MAY, Group.JUNK)

BUTTERFLY = Card('모란 - 끗', Month.JUN, Group.ANIMAL)
PEONY_BLUE_POEM = Card('모란 - 청단', Month.JUN, Group.RIBBON)
PEONY = Card('모란 - 피', Month.JUN, Group.JUNK)

BOAR = Card('홍싸리 - 끗', Month.JUL, Group.ANIMAL)
BUSH_CLOVER_RED = Card('홍싸리 - 초단', Month.JUL, Group.RIBBON)
BUSH_CLOVER = Card('홍싸리 - 피', Month.JUL, Group.JUNK)

MOON = Card('공산 - 광', Month.AUG, Group.BRIGHT)
GEESE = Card('공산 - 끗', Month.AUG, Group.ANIMAL)
PAMPAS_GRASS = Card('공산 - 피', Month.AUG, Group.JUNK)

CUP = Card('국진 - 끗(쌍피)', Month.SEP, (Group.ANIMAL, Group.JUNK_2))
CHRYSANTHEMUM_BLUE_PEOM = Card('국진 - 청단', Month.SEP, Group.RIBBON)
CHRYSANTHEMUM = Card('국진 - 피', Month.SEP, Group.JUNK)

DEER = Card('단풍 - 끗', Month.OCT, Group.ANIMAL)
MAPLE_BLUE_POEM = Card('단풍 - 청단', Month.OCT, Group.RIBBON)
MAPLE = Card('단풍 - 피', Month.OCT, Group.JUNK)

PHOENIX = Card('오동 - 광', Month.NOV, Group.BRIGHT)
PAULOWNIA = Card('오동 - 피', Month.NOV, Group.JUNK)
PAULOWNIA_2 = Card('오동 - 쌍피', Month.NOV, Group.JUNK_2)

RAIN = Card('비 - 광', Month.DEC, Group.BRIGHT)
SWALLOW = Card('비 - 끗', Month.DEC, Group.ANIMAL)
WILLOW_RED = Card('비 - 초단', Month.DEC, Group.RIBBON)
WILLOW_2 = Card('비 - 쌍피', Month.DEC, Group.JUNK_2)


ALL_CARDS = (
    CRANE, PINE_RED_POEM, PINE, PINE,
    BUSH_WARBLER, PLUM_RED_POEM, PLUM, PLUM,
    CURTAIN, CHERRY_RED_POEM, CHERRY, CHERRY,
    CUCKOO, WISTERIA_RED, WISTERIA, WISTERIA,
    BRIDGE, IRIS_RED, IRIS, IRIS,
    BUTTERFLY, PEONY_BLUE_POEM, PEONY, PEONY,
    BOAR, BUSH_CLOVER_RED, BUSH_CLOVER, BUSH_CLOVER,
    MOON, GEESE, PAMPAS_GRASS, PAMPAS_GRASS,
    CUP, CHRYSANTHEMUM_BLUE_PEOM, CHRYSANTHEMUM, CHRYSANTHEMUM,
    DEER, MAPLE_BLUE_POEM, MAPLE, MAPLE,
    PHOENIX, PAULOWNIA_2, PAULOWNIA, PAULOWNIA,
    RAIN, SWALLOW, WILLOW_RED, WILLOW_2
)
